from src.similarity import jaccard_similarity

MIN_COMMON_ITEMS = 24
TOP_K_USERS = 5
TOP_N_RECOMMENDATIONS = 5

def build_user_items(df):

    return df.groupby("CustomerID")["StockCode"].apply(set).to_dict()

def find_similar_users(user_items, target_user, min_common=MIN_COMMON_ITEMS, top_k=TOP_K_USERS):
    """
    Hedef kullanıcıya en benzer kullanıcıları ve benzerlik skorlarını bulur.
    """
    if target_user not in user_items:
        return []

    target_items = user_items[target_user]
    similarities = []

    for other_user, other_items in user_items.items():
        if other_user == target_user:
            continue

        common_items = target_items.intersection(other_items)
        
        
        if len(common_items) < min_common:
            continue

        score = jaccard_similarity(target_items, other_items)
        similarities.append({
            "user": other_user,
            "similarity": score,
            "common_count": len(common_items)
        })

   
    similarities.sort(key=lambda x: x["similarity"], reverse=True)
    return similarities[:top_k]

def generate_recommendations(user_items, target_user, min_common=MIN_COMMON_ITEMS, top_k=TOP_K_USERS, top_n=TOP_N_RECOMMENDATIONS):
    """
    Hedef kullanıcı için benzer kullanıcıların sepetlerinden ürün önerisi üretir.
    """
    if target_user not in user_items:
        return [], []

    target_items = user_items[target_user]
    similar_users = find_similar_users(user_items, target_user, min_common, top_k)

    recommendation_scores = {}

    for sim_user in similar_users:
        u_id = sim_user["user"]
        weight = sim_user["similarity"]

        for item in user_items[u_id]:
          
            if item in target_items:
                continue

            
            recommendation_scores[item] = recommendation_scores.get(item, 0.0) + weight

    
    sorted_recs = sorted(recommendation_scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_recs[:top_n], similar_users