#!/usr/bin/env python3
"""Kirli müşteri verisini temizler (Transform) ve yükler (Load)."""
import os, sys
import numpy as np
import pandas as pd
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import KOK

GIRDI = os.path.join(KOK, "veri", "kirli_musteri.csv")

def tr_sayi(v):
    """'12.500,00' → 12500.0 ; sayı ise olduğu gibi."""
    if isinstance(v, str) and "," in v:          # Türkçe biçim: binlik '.', ondalık ','
        v = v.replace(".", "").replace(",", ".")
    try:
        return float(v)
    except (TypeError, ValueError):
        return np.nan

def temizle(df: pd.DataFrame) -> pd.DataFrame:
    n0 = len(df)
    df = df.drop_duplicates(subset="musteri_id"); print(f"yinelenen satır: {n0-len(df)} silindi")
    df["gelir"] = df["gelir"].map(tr_sayi)
    df["sehir"] = df["sehir"].str.strip().str.replace("İ", "I").str.capitalize()
    tutarsiz = (~df["sehir"].isin(["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"])).sum()
    print(f"şehir yazımı düzeltildi; hâlâ tanınmayan: {tutarsiz}")
    uc_yas = df["yas"] > 100; uc_gelir = df["gelir"] > 500_000
    df.loc[uc_yas, "yas"] = np.nan; df.loc[uc_gelir, "gelir"] = np.nan
    print(f"uç değer -> NaN: yas {int(uc_yas.sum())}, gelir {int(uc_gelir.sum())}")
    eksik = df[["yas", "gelir"]].isna().sum()
    print(f"eksik değer (dolduruluyor): {eksik.to_dict()}")
    df["yas"] = df["yas"].fillna(df["yas"].median()).round().astype(int)
    df["gelir"] = df.groupby("segment")["gelir"].transform(lambda s: s.fillna(s.median()))
    return df.sort_values("musteri_id").reset_index(drop=True)

if __name__ == "__main__":
    df = pd.read_csv(GIRDI)
    print(f"girdi: {df.shape}")
    temiz = temizle(df)
    os.makedirs("cikti", exist_ok=True)
    temiz.to_csv("cikti/temiz_musteri.csv", index=False)
    print(f"çıktı: {temiz.shape} -> cikti/temiz_musteri.csv")
    print(temiz.describe().round(1))
