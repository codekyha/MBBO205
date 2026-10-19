#!/usr/bin/env python3
"""HTTP API'den veri çekme; ağ yoksa yerel yedek."""
import json, os
import pandas as pd
import requests

URL = "https://api.open-meteo.com/v1/forecast?latitude=41.01&longitude=28.98&current=temperature_2m,relative_humidity_2m"
YEDEK = os.path.join("veri", "ornek_api.json")

def cek(url: str, zaman_asimi: float = 5.0):
    try:
        r = requests.get(url, timeout=zaman_asimi)
        r.raise_for_status()
        j = r.json()
        c = j["current"]
        print("API'den alındı:", c)
        return [{"id": 0, "sehir": "Istanbul", "sicaklik": c["temperature_2m"],
                 "nem": c["relative_humidity_2m"], "zaman": c["time"]}]
    except Exception as e:
        print(f"UYARI: API erişilemedi ({type(e).__name__}); yerel yedek kullanılıyor: {YEDEK}")
        with open(YEDEK, encoding="utf-8") as f:
            return json.load(f)

if __name__ == "__main__":
    kayitlar = cek(URL)
    df = pd.DataFrame(kayitlar)
    df["zaman"] = pd.to_datetime(df["zaman"])
    os.makedirs("cikti", exist_ok=True)
    df.to_csv("cikti/hava.csv", index=False)
    print(df)
    print("cikti/hava.csv yazıldı")
