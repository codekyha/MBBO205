#!/usr/bin/env python3
"""Python istemcisi ve gecikme ölçümü."""
import argparse, time, statistics, requests
ap = argparse.ArgumentParser(); ap.add_argument("--url", default="http://localhost:8000"); ap.add_argument("--n", type=int, default=100)
a = ap.parse_args()
ornek = {"yas": 34, "gelir": 28000, "kidem_ay": 6, "aylik_islem": 3, "sehir": "Istanbul", "segment": "Bireysel"}
print("sağlık:", requests.get(f"{a.url}/saglik", timeout=5).json())
sureler = []
for _ in range(a.n):
    t = time.perf_counter(); r = requests.post(f"{a.url}/tahmin", json=ornek, timeout=5); sureler.append((time.perf_counter() - t) * 1000)
    r.raise_for_status()
sureler.sort()
print(f"{a.n} istek: ortalama {statistics.mean(sureler):.1f} ms, medyan {statistics.median(sureler):.1f} ms, p95 {sureler[int(.95*a.n)-1]:.1f} ms")
print("son yanıt:", r.json(), "| sunucu:", r.headers.get("X-Sunucu"))
