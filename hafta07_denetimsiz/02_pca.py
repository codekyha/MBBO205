#!/usr/bin/env python3
"""PCA ile boyut indirgeme ve 2B görselleştirme."""
import os, sys
import numpy as np, pandas as pd
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, SAYISAL, cikti_dizini

df = veri_yukle(); C = cikti_dizini(__file__)
ozellik = SAYISAL + ["harcama"]; Xs = StandardScaler().fit_transform(df[ozellik])
pca = PCA().fit(Xs); ev = pca.explained_variance_ratio_
print("açıklanan varyans:", np.round(ev, 3), " kümülatif:", np.round(np.cumsum(ev), 3))
print("\nbileşen yükleri:\n", pd.DataFrame(pca.components_[:2].T, index=ozellik, columns=["PC1", "PC2"]).round(3))
Z = pca.transform(Xs)[:, :2]
renk = pd.read_csv(f"{C}/kumeler.csv")["kume"] if os.path.exists(f"{C}/kumeler.csv") else df["ayrildi"]
plt.figure(figsize=(6, 5)); plt.scatter(Z[:, 0], Z[:, 1], c=renk, s=8, cmap="tab10"); plt.xlabel(f"PC1 ({ev[0]:.0%})"); plt.ylabel(f"PC2 ({ev[1]:.0%})")
plt.title("PCA izdüşümü"); plt.tight_layout(); plt.savefig(f"{C}/pca.png", dpi=120); print("cikti/pca.png yazıldı")
