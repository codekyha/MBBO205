"""Haftalık betiklerin ortak yardımcıları."""
import os
import pandas as pd
from sklearn.model_selection import train_test_split

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
VERI = os.path.join(KOK, "veri", "musteri.csv")
SAYISAL = ["yas", "gelir", "kidem_ay", "aylik_islem"]
KATEGORIK = ["sehir", "segment"]

def veri_yukle(yol: str = VERI) -> pd.DataFrame:
    if not os.path.exists(yol):
        raise FileNotFoundError("Önce kök dizinde `python ortak/veri_uret.py` çalıştırın.")
    return pd.read_csv(yol)

def ozellik_hedef(df: pd.DataFrame, hedef: str = "ayrildi"):
    X = pd.get_dummies(df[SAYISAL + KATEGORIK], columns=KATEGORIK, drop_first=True)
    y = df[hedef]
    return X, y

def bol(X, y, test=0.2, tohum=42):
    katmanli = y if y.nunique() <= 10 else None
    return train_test_split(X, y, test_size=test, random_state=tohum, stratify=katmanli)

def cikti_dizini(dosya: str) -> str:
    """Çağıran betiğin yanındaki cikti/ dizinini oluşturur ve döndürür."""
    yol = os.path.join(os.path.dirname(os.path.abspath(dosya)), "cikti")
    os.makedirs(yol, exist_ok=True)
    return yol
