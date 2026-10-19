#!/usr/bin/env python3
"""Python temelleri: fonksiyon, veri yapıları, dosya ve JSON, argparse, hata yönetimi."""
import argparse, json, os
from collections import Counter

def selamla(ad: str, tekrar: int = 1) -> list[str]:
    return [f"Merhaba {ad}, MBBO205'e hoş geldin! ({i+1})" for i in range(tekrar)]

def istatistik(sayilar: list[float]) -> dict:
    if not sayilar:
        raise ValueError("boş liste")
    n = len(sayilar); ort = sum(sayilar) / n
    var = sum((x - ort) ** 2 for x in sayilar) / n
    return {"n": n, "ortalama": round(ort, 3), "std": round(var ** 0.5, 3),
            "min": min(sayilar), "max": max(sayilar)}

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description="Hafta 2 temeller")
    ap.add_argument("--ad", default="Öğrenci")
    ap.add_argument("--tekrar", type=int, default=1)
    a = ap.parse_args()
    for s in selamla(a.ad, a.tekrar):
        print(s)
    veri = [3.5, 7.2, 1.8, 9.9, 4.4, 6.1]
    print("istatistik:", istatistik(veri))
    kelimeler = "bulut bilişim ve yapay zekâ bulut üzerinde yapay zekâ".split()
    print("kelime sayımı:", dict(Counter(kelimeler)))
    os.makedirs("cikti", exist_ok=True)
    with open("cikti/ozet.json", "w", encoding="utf-8") as f:
        json.dump({"istatistik": istatistik(veri), "kelimeler": Counter(kelimeler)}, f, ensure_ascii=False, indent=2)
    print("cikti/ozet.json yazıldı")
    try:
        istatistik([])
    except ValueError as e:
        print("yakalanan hata:", e)
