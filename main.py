import random
from src.data_loader import load_data
from src.preprocessing import clean_data
from src.recommender import build_user_items, generate_recommendations

def main():
    print("=" * 65)
    print("  PERSONALIZED E-COMMERCE PRODUCT RECOMMENDATION SYSTEM")
    print("=" * 65)

   
    df_raw = load_data("data/Online_Retail.csv")
    df_clean, item_map = clean_data(df_raw)
    user_items = build_user_items(df_clean)

    
    eligible_users = {
        u: items for u, items in user_items.items() if len(items) >= 24
    }

    print(f"\nToplam Müşteri Sayısı: {len(user_items)}")
    print(f"24+ Ürün Almış Müşteri Sayısı: {len(eligible_users)}")

    
    while True:
        # Rastgele 5 örnek müşteri ID'si seçip kullanıcıya fikir verelim
        sample_ids = random.sample(list(eligible_users.keys()), 5)
        print("\n" + "-" * 65)
        print(f" Deneyebileceğiniz Örnek Müşteri ID'leri: {sample_ids}")
        print("-" * 65)
        
        user_input = input("Öneri üretmek istediğiniz Müşteri ID (Çıkış için 'q'): ").strip()

        if user_input.lower() in ['q', 'exit', 'cikis']:
            print("\nProgramdan çıkılıyor. İyi çalışmalar!")
            break

        if not user_input.isdigit():
            print(" Lütfen geçerli bir sayısal ID girin.")
            continue

        target_user = int(user_input)

        
        if target_user not in user_items:
            print(f" '{target_user}' numaralı müşteri sistemde bulunamadı!")
            continue

        target_purchases = user_items[target_user]
        print(f"\n SEÇİLEN MÜŞTERİ: {target_user}")
        print(f" Bu Müşterinin Satın Aldığı Farklı Ürün Sayısı: {len(target_purchases)}")

        # Geçmişte aldığı ilk 3 ürünü örnek olarak göster
        print("🛒 Geçmiş Alışverişlerinden Bazıları:")
        for sample_item in list(target_purchases)[:3]:
            print(f"   • [{sample_item}] {item_map.get(sample_item, 'Bilinmeyen Ürün')}")

        
        recs, similar_users = generate_recommendations(user_items, target_user)

        
        print("\n EN ÇOK BENZEYEN DİĞER MÜŞTERİLER (Ortak Ürün >= 24):")
        if not similar_users:
            print("   (Yeterli ortak ürüne sahip benzer müşteri bulunamadı.)")
        else:
            for u in similar_users:
                print(f"   • Müşteri: {u['user']:<6} | Jaccard Benzerliği: {u['similarity']:.4f} | Ortak Ürün: {u['common_count']}")

        
        print("\n KİŞİSELLEŞTİRİLMİŞ ÜRÜN ÖNERİLERİ:")
        print("." * 65)
        if not recs:
            print("   Bu müşteri için kriterlere uygun yeni bir ürün önerisi çıkarılamadı.")
        else:
            for rank, (item_code, score) in enumerate(recs, 1):
                item_name = item_map.get(item_code, "Bilinmeyen Ürün")
                print(f"   {rank}. [{item_code}] {item_name} (Öneri Gücü: {score:.4f})")
        print("." * 65)

if __name__ == "__main__":
    main()