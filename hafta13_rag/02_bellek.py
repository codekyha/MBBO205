#!/usr/bin/env python3
"""Bellek tüketimini ölçme, OOM'u güvenli canlandırma ve parçalı işleme ile çözüm."""
import argparse, os, resource, time
import numpy as np

def rss_mb() -> float:
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024  # Linux: KB -> MB

ap = argparse.ArgumentParser(); ap.add_argument("--sinir_mb", type=float, default=0, help="0 = sınırsız; aşılınca MemoryError")
ap.add_argument("--parcali", action="store_true"); ap.add_argument("--n", type=int, default=20000); a = ap.parse_args()
print(f"başlangıç RSS: {rss_mb():.0f} MB   (free -m ile sistem belleğini karşılaştırın)")
if a.parcali:
    print(f"\n== Parçalı işleme: {a.n}x{a.n} benzerlik matrisi yerine satır blokları ==")
    X = np.random.default_rng(0).random((a.n, 64), dtype=np.float32); X /= np.linalg.norm(X, axis=1, keepdims=True)
    en_yakin = np.empty(a.n, dtype=np.int64); t = time.perf_counter()
    for i in range(0, a.n, 1000):
        blok = X[i:i+1000] @ X.T; np.fill_diagonal(blok[:, i:i+1000], -1); en_yakin[i:i+1000] = blok.argmax(axis=1)
    print(f"tamamlandı: {time.perf_counter()-t:.1f} s, en yüksek RSS {rss_mb():.0f} MB (tam matris {a.n*a.n*4/1e6:.0f} MB isterdi)")
    raise SystemExit
print("\n== Kademeli ayırma ==\n   n        matris MB     RSS MB")
bloklar = []
for n in (2000, 4000, 8000, 12000, 16000, 20000):
    gerek = n * n * 4 / 1e6
    if a.sinir_mb and rss_mb() + gerek > a.sinir_mb:
        print(f"{n:6d}  {gerek:10.0f}   -> sınır {a.sinir_mb:.0f} MB aşılacak: MemoryError (gerçekte çekirdek süreci 'Killed' ile sonlandırırdı)")
        raise MemoryError("sanal OOM")
    bloklar.append(np.ones((n, n), dtype=np.float32)); print(f"{n:6d}  {gerek:10.0f}  {rss_mb():8.0f}")
print("\nNot: Gerçek OOM'da Python istisna üretemez; çekirdek SIGKILL gönderir, ekranda yalnızca 'Killed' görünür, kayıt `dmesg`/`journalctl -k` içindedir.")
print("Çareler: parti/parça boyutu, float32/float16, bellek eşlemeli dosya (np.memmap), swap, daha büyük makine, Docker'da --memory sınırını gözden geçirme.")
