import pandas as pd

def clean_data(df):
    """
    Veriyi temizler ve müşteri-ürün ilişkisini tekilleştirir.
    """
    
    df = df.dropna(subset=["CustomerID"]).copy()
    df["CustomerID"] = df["CustomerID"].astype(int)

   
    df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
    df = df[df["Quantity"] > 0]
    df = df[df["UnitPrice"] > 0]

  
    df["Description"] = df["Description"].astype(str).str.strip()

   
    item_map = (
        df.groupby("StockCode")["Description"]
        .last()
        .to_dict()
    )

    
    df_unique = df[["CustomerID", "StockCode"]].drop_duplicates()

    return df_unique, item_map