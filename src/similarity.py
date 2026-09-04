def jaccard_similarity(set_a, set_b):
    """
    İki küme arasındaki Jaccard benzerlik katsayısını hesaplar.
    Jaccard(A, B) = |A ∩ B| / |A ∪ B|
    """
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)

    if not union:
        return 0.0

    return len(intersection) / len(union)