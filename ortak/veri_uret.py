#!/usr/bin/env python3
"""Sentetik müşteri verisi üretir: temiz ve kasıtlı kirletilmiş iki sürüm."""
import argparse, os
import numpy as np
import pandas as pd

def uret(n: int, tohum: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(tohum)
    yas = rng.integers(18, 76, n)
    gelir = np.round(rng.lognormal(mean=10.2, sigma=0.45, size=n), 2)
    kidem = rng.integers(1, 121, n)
    islem = rng.poisson(12, n)
    sehir = rng.choice(["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"], n, p=[.4, .2, .15, .15, .1])
    segment = rng.choice(["Bireysel", "KOBI", "Kurumsal"], n, p=[.6, .3, .1])
    seg_kat = pd.Series(segment).map({"Bireysel": 1.0, "KOBI": 1.6, "Kurumsal": 2.5}).to_numpy()
    harcama = np.round(0.18 * gelir * seg_kat + 25 * islem + rng.normal(0, 400, n), 2)
    harcama = np.clip(harcama, 50, None)
    # churn olasılığı: düşük kıdem, düşük işlem ve yüksek gelir -> daha yüksek risk
    lojit = 1.4 - 0.03 * kidem - 0.12 * islem + 0.00004 * gelir + rng.normal(0, 0.3, n)
    p = 1 / (1 + np.exp(-lojit))
    ayrildi = (rng.random(n) < p).astype(int)
    return pd.DataFrame({
        "musteri_id": np.arange(1, n + 1), "yas": yas, "gelir": gelir, "kidem_ay": kidem,
        "aylik_islem": islem, "sehir": sehir, "segment": segment,
        "harcama": harcama, "ayrildi": ayrildi,
    })

def kirlet(df: pd.DataFrame, tohum: int = 7) -> pd.DataFrame:
    """ETL dersi için: eksik değer, yinelenen satır, uç değer, tutarsız yazım, yanlış tip."""
    rng = np.random.default_rng(tohum)
    k = df.copy()
    k.loc[rng.choice(k.index, 40, replace=False), "gelir"] = np.nan
    k.loc[rng.choice(k.index, 25, replace=False), "yas"] = np.nan
    k.loc[rng.choice(k.index, 5, replace=False), "gelir"] = 9_999_999.0
    k.loc[rng.choice(k.index, 5, replace=False), "yas"] = 150
    k.loc[rng.choice(k.index, 30, replace=False), "sehir"] = "istanbul "
    k.loc[rng.choice(k.index, 20, replace=False), "sehir"] = "İSTANBUL"
    k["gelir"] = k["gelir"].astype(object)
    k.loc[rng.choice(k.index, 15, replace=False), "gelir"] = "12.500,00"
    k = pd.concat([k, k.sample(30, random_state=1)], ignore_index=True)
    return k.sample(frac=1, random_state=3).reset_index(drop=True)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=1000)
    ap.add_argument("--cikti", default=os.path.join(os.path.dirname(__file__), "..", "veri"))
    a = ap.parse_args()
    os.makedirs(a.cikti, exist_ok=True)
    df = uret(a.n)
    df.to_csv(os.path.join(a.cikti, "musteri.csv"), index=False)
    kirlet(df).to_csv(os.path.join(a.cikti, "kirli_musteri.csv"), index=False)
    print(f"{a.n} satır üretildi -> {os.path.abspath(a.cikti)}/musteri.csv, kirli_musteri.csv")
    print(f"churn oranı: {df.ayrildi.mean():.3f}")
