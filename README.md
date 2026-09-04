# 🛒 Personalized E-Commerce Product Recommendation System
> **User-Based Collaborative Filtering Engine using Jaccard Similarity**

Bu proje, gerçek e-ticaret işlem verilerini (**UCI Online Retail**) kullanarak kullanıcıların satın alma davranışlarını analiz eden ve **Kullanıcı Tabanlı İşbirlikçi Filtreleme (User-Based Collaborative Filtering)** yaklaşımıyla kişiselleştirilmiş ürün önerileri sunan bir makine öğrenmesi / veri madenciliği motorudur.

---

## 📌 Proje Akış Şeması (Flowchart)

```mermaid
flowchart TD
    A[Ham E-Ticaret Verisi: Online_Retail.csv] --> B[Veri Temizleme: Eksik ID, İptal 'C', Negatif Miktar Filtresi]
    B --> C[Tekil Kullanıcı - Ürün Sepet Kümelerinin Çıkarılması]
    C --> D[Hedef Müşteri ID Seçimi]
    D --> E[Tüm Müşterilerin Sepetleriyle Karşılaştırma]
    E --> F{Ortak Ürün Sayısı >= 24 ?}
    F -- Hayır --> G[Kullanıcıyı Atla]
    F -- Evet --> H[Jaccard Benzerlik Skorunu Hesapla]
    H --> I[En Benzer Top-K Müşteriyi Sırala]
    I --> J[Benzer Kişilerin Aldığı Ürünleri Havuzda Topla]
    J --> K[Hedef Müşterinin Zaten Aldığı Ürünleri Çıkar]
    K --> L[Benzerlik Ağırlıklı Öneri Puanlarını Hesapla]
    L --> M[🎯 Kişiselleştirilmiş Top-N Ürün Önerisi]

    personalized-recommendation-engine/
│
├── data/
│   └── Online_Retail.csv          # E-ticaret veri seti
│
├── src/
│   ├── __init__.py                # Paket tanımlayıcı
│   ├── data_loader.py             # CSV / Excel okuma modülü
│   ├── preprocessing.py          # Veri temizleme ve mapping
│   ├── similarity.py             # Jaccard benzerlik algoritması
│   ├── recommender.py            # Öneri ve filtreleme motoru
│   └── evaluation.py             # Değerlendirme metrikleri
│
├── .gitignore                     # Git tarafından yok sayılacak dosyalar
├── requirements.txt               # Gerekli Python kütüphaneleri
├── README.md                      # Proje dokümantasyonu
└── main.py                        # İnteraktif terminal uygulaması