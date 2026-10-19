#!/usr/bin/env python3
"""NumPy vektörel işlemler ve pandas DataFrame temelleri."""
import time
import numpy as np
import pandas as pd

N = 1_000_000
x = np.random.default_rng(0).random(N)
t0 = time.perf_counter(); s1 = sum(v * v for v in x); t1 = time.perf_counter()
s2 = np.dot(x, x); t2 = time.perf_counter()
print(f"döngü: {t1-t0:.3f} s   numpy: {t2-t1:.4f} s   hız oranı ≈ {(t1-t0)/(t2-t1):.0f}x   (sonuç farkı {abs(s1-s2):.2e})")

A = np.arange(12).reshape(3, 4)
print("A=\n", A)
print("satır ortalaması:", A.mean(axis=1), "  sütun toplamı:", A.sum(axis=0))
print("yayın (broadcasting) A - satır ort.:\n", A - A.mean(axis=1, keepdims=True))

df = pd.DataFrame({
    "sehir": ["Istanbul", "Ankara", "Izmir", "Istanbul", "Ankara", "Izmir"],
    "yas": [25, 41, 33, 52, 29, 38],
    "harcama": [1200, 800, 950, 2100, 640, 1330],
})
print("\nilk satırlar:\n", df.head(3))
print("\nyas>30 ve harcama>900:\n", df[(df.yas > 30) & (df.harcama > 900)])
print("\nşehre göre ortalama:\n", df.groupby("sehir")[["yas", "harcama"]].mean().round(1))
df["harcama_std"] = (df.harcama - df.harcama.mean()) / df.harcama.std()
print("\nstandartlaştırılmış harcama:\n", df[["sehir", "harcama_std"]].round(2))
