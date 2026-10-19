#!/usr/bin/env python3
"""k-means ile müşteri bölütleme; dirsek ve silüet ile k seçimi."""
import argparse, os, sys
import pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, SAYISAL, cikti_dizini

ap = argparse.ArgumentParser(); ap.add_argument("--kmax", type=int, default=8); a = ap.parse_args()
df = veri_yukle(); C = cikti_dizini(__file__)
Xs = StandardScaler().fit_transform(df[SAYISAL + ["harcama"]])
ks = range(2, a.kmax + 1); inertia, sil = [], []
for k in ks:
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(Xs)
    inertia.append(km.inertia_); sil.append(silhouette_score(Xs, km.labels_))
    print(f"k={k}: inertia={km.inertia_:.0f}  silüet={sil[-1]:.3f}")
en_k = list(ks)[sil.index(max(sil))]; print(f"\nen yüksek silüet: k={en_k}")
fig, ax = plt.subplots(1, 2, figsize=(10, 4)); ax[0].plot(ks, inertia, "o-"); ax[0].set_title("Dirsek"); ax[0].set_xlabel("k")
ax[1].plot(ks, sil, "s-"); ax[1].set_title("Silüet"); ax[1].set_xlabel("k"); plt.tight_layout(); plt.savefig(f"{C}/k_secimi.png", dpi=120)
km = KMeans(n_clusters=en_k, n_init=10, random_state=42).fit(Xs); df["kume"] = km.labels_
print("\nküme profilleri:\n", df.groupby("kume")[SAYISAL + ["harcama", "ayrildi"]].mean().round(1))
print("\nküme × segment:\n", pd.crosstab(df.kume, df.segment))
df[["musteri_id", "kume"]].to_csv(f"{C}/kumeler.csv", index=False); print("\ncikti/kumeler.csv, cikti/k_secimi.png yazıldı")
