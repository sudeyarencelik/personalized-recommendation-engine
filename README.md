# 🛒 Personalized E-Commerce Product Recommendation System
> **User-Based Collaborative Filtering Engine using Jaccard Similarity**

Bu proje, gerçek e-ticaret işlem verilerini (**UCI Online Retail**) kullanarak kullanıcıların satın alma davranışlarını analiz eden ve **Kullanıcı Tabanlı İşbirlikçi Filtreleme (User-Based Collaborative Filtering)** yaklaşımıyla kişiselleştirilmiş ürün önerileri sunan bir makine öğrenmesi / veri madenciliği motorudur.

---

### Proje Akış Şeması (Flowchart)

```mermaid
flowchart TD
    A[Ham E-Ticaret Verisi: Online_Retail.csv] --> B[Veri Temizleme: Eksik ID, İptal C, Negatif Miktar Filtresi]
    B --> C[Tekil Kullanıcı - Ürün Sepet Kümelerinin Çıkarılması]
    C --> D[Hedef Müşteri ID Seçimi]
    D --> E[Tüm Müşterilerin Sepetleriyle Karşılaştırma]
    E --> F{Ortak Ürün Sayısı >= N ?}
    F -- Hayır --> G[Kullanıcıyı Atla]
    F -- Evet --> H[Jaccard Benzerlik Skorunu Hesapla]
    H --> I[En Benzer Top-K Müşteriyi Sırala]
    I --> J[Önerilmeyen Ürünleri Havuzla]
    J --> K[Skorlayıp Sıralı Liste Döndür]
```

###  Proje Dizin Yapısı

```text
personalized-recommendation-engine/
├── data/
│   └── Online_Retail.csv
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── similarity.py
│   └── recommender.py
├── app.py
├── main.py
├── exploration.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```
