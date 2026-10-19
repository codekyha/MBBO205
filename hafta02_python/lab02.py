"""Lab 2 — fonksiyonları doldurun; `pytest -q test_lab02.py` ile kontrol edin."""
import numpy as np
import pandas as pd

def normalize(x: np.ndarray) -> np.ndarray:
    """Min-max normalizasyon: (x - min) / (max - min). Sabit dizi için sıfır dizisi döndür."""
    r = x.max() - x.min()
    return np.zeros_like(x, dtype=float) if r == 0 else (x - x.min()) / r

def kelime_sayac(metin: str) -> dict:
    """Küçük harfe çevirip noktalama olmadan kelime sayımı döndür."""
    temiz = "".join(c.lower() if c.isalnum() or c.isspace() else " " for c in metin)
    sayac: dict = {}
    for k in temiz.split():
        sayac[k] = sayac.get(k, 0) + 1
    return sayac

def en_yuksek_k(df: pd.DataFrame, sutun: str, k: int) -> pd.DataFrame:
    """`sutun` değerine göre azalan sıralı ilk k satır (indeks sıfırlanmış)."""
    return df.sort_values(sutun, ascending=False).head(k).reset_index(drop=True)
