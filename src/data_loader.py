import pandas as pd
import os

def load_data(file_path="data/Online_Retail.csv"):
    """
    Online_Retail.csv veya .xlsx dosyasını okur.
    """
    if not os.path.exists(file_path):
        for alt_path in ["data/Online Retail.csv", "data/Online Retail.xlsx", "data/online_retail.csv"]:
            if os.path.exists(alt_path):
                file_path = alt_path
                break
        else:
            raise FileNotFoundError(f"Veri dosyası bulunamadı: {file_path}")
        
    print(f"Veri yükleniyor: {file_path}")
    if file_path.endswith(".csv"):
        try:
            df = pd.read_csv(file_path, encoding="ISO-8859-1")
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding="utf-8")
    else:
        df = pd.read_excel(file_path)
        
    print(f"Ham veri  yüklendi Boyut: {df.shape}")
    return df