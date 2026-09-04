import streamlit as st
import pandas as pd
from src.data_loader import load_data
from src.preprocessing import clean_data
from src.recommender import build_user_items, generate_recommendations

st.set_page_config(
    page_title="E-Commerce Recommendation System",
    layout="wide"
)

st.title("E-Commerce Product Recommendation System")
st.caption("User-Based Collaborative Filtering with Jaccard Similarity")
st.markdown("---")

@st.cache_data
def load_and_prepare():
    df_raw = load_data("data/Online_Retail.csv")
    df_clean, item_map = clean_data(df_raw)
    user_items = build_user_items(df_clean)
    return df_clean, item_map, user_items

df_clean, item_map, user_items = load_and_prepare()

# 24+ urun satin almis kullanicilari listele
eligible_users = [u for u, items in user_items.items() if len(items) >= 24]

# --- Sol Panel (Kontroller) ---
st.sidebar.subheader("Parametreler")
selected_user = st.sidebar.selectbox("Hedef CustomerID:", options=eligible_users)
min_common = st.sidebar.number_input("Minimum Ortak Urun Sayisi:", min_value=1, value=24, step=1)
top_k = st.sidebar.slider("Benzer Kullanici Sayisi (Top-K):", min_value=1, max_value=10, value=5)
top_n = st.sidebar.slider("Onerilecek Urun Sayisi (Top-N):", min_value=1, max_value=10, value=5)

run_button = st.sidebar.button("Onerileri Hesapla")

# --- Ana Ekran ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader(f"Musteri #{selected_user} Profili")
    user_basket = list(user_items[selected_user])
    
    st.write(f"**Toplam Satin Alinan Tekil Urun:** {len(user_basket)}")
    
    # Satin alinan urunlerin tablosu
    basket_data = [
        {"StockCode": code, "Description": item_map.get(code, "N/A")}
        for code in user_basket
    ]
    st.dataframe(pd.DataFrame(basket_data), height=300, use_container_width=True)

with col2:
    st.subheader("Oneri Sonuclari")
    
    if run_button:
        recs, similar_users = generate_recommendations(
            user_items,
            selected_user,
            min_common=min_common,
            top_k=top_k,
            top_n=top_n
        )

        if not recs:
            st.warning("Belirlenen filtre kriterlerine uygun benzer kullanici veya oneri bulunamadi.")
        else:
            st.write("**Önerilen Urunler:**")
            rec_data = [
                {
                    "Sira": i,
                    "StockCode": code,
                    "Urun Adi": item_map.get(code, "N/A"),
                    "Oneri Skoru": f"{score:.4f}"
                }
                for i, (code, score) in enumerate(recs, 1)
            ]
            st.dataframe(pd.DataFrame(rec_data), use_container_width=True, hide_index=True)

            st.write("**Referans Alinan Benzer Musteriler:**")
            sim_data = [
                {
                    "CustomerID": u["user"],
                    "Jaccard Benzerligi": f"{u['similarity']:.4f}",
                    "Ortak Urun Sayisi": u["common_count"]
                }
                for u in similar_users
            ]
            st.dataframe(pd.DataFrame(sim_data), use_container_width=True, hide_index=True)
    else:
        st.info("Sol panelden parametreleri belirleyip 'Onerileri Hesapla' butonuna basiniz.")