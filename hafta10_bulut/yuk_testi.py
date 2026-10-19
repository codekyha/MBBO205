#!/usr/bin/env python3
"""Yük dengeleyici arkasındaki kopyalara istek dağılımı."""
import argparse, time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import requests
ap = argparse.ArgumentParser(); ap.add_argument("--url", default="http://localhost:8080"); ap.add_argument("--n", type=int, default=300); ap.add_argument("--es", type=int, default=10)
a = ap.parse_args()
ornek = {"yas": 34, "gelir": 28000, "kidem_ay": 6, "aylik_islem": 3, "sehir": "Istanbul", "segment": "Bireysel"}
def istek(_):
    t = time.perf_counter(); r = requests.post(f"{a.url}/tahmin", json=ornek, timeout=10)
    return r.headers.get("X-Sunucu", "?"), r.status_code, time.perf_counter() - t
t0 = time.perf_counter()
with ThreadPoolExecutor(a.es) as ex: sonuc = list(ex.map(istek, range(a.n)))
sure = time.perf_counter() - t0
print(f"{a.n} istek, {a.es} eşzamanlı: {sure:.2f} s, {a.n/sure:.0f} istek/s")
print("kopya dağılımı:", dict(Counter(s for s, _, _ in sonuc)))
print("durum kodları:", dict(Counter(k for _, k, _ in sonuc)))
print(f"ortalama gecikme: {1000*sum(g for *_, g in sonuc)/a.n:.1f} ms")
