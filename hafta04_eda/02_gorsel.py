#!/usr/bin/env python3
"""EDA grafikleri (başsız sunucuda da çalışır)."""
import os, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, SAYISAL, cikti_dizini

df = veri_yukle(); C = cikti_dizini(__file__)

plt.figure(figsize=(6, 4)); plt.hist(df.gelir, bins=40, color="steelblue"); plt.xlabel("gelir (TL)"); plt.ylabel("frekans")
plt.title("Gelir dağılımı"); plt.tight_layout(); plt.savefig(f"{C}/hist_gelir.png", dpi=120); plt.close()

plt.figure(figsize=(6, 4))
gruplar = [df.loc[df.segment == s, "harcama"] for s in ["Bireysel", "KOBI", "Kurumsal"]]
plt.boxplot(gruplar); plt.xticks([1, 2, 3], ["Bireysel", "KOBI", "Kurumsal"]); plt.ylabel("harcama (TL)")
plt.title("Segmente göre harcama"); plt.tight_layout(); plt.savefig(f"{C}/kutu_harcama_segment.png", dpi=120); plt.close()

plt.figure(figsize=(6, 4)); plt.scatter(df.gelir, df.harcama, s=6, alpha=.5, c=df.ayrildi, cmap="coolwarm")
plt.xlabel("gelir"); plt.ylabel("harcama"); plt.title("Gelir–harcama (renk: churn)")
plt.tight_layout(); plt.savefig(f"{C}/dagilim_gelir_harcama.png", dpi=120); plt.close()

k = df[SAYISAL + ["harcama", "ayrildi"]].corr().to_numpy()
plt.figure(figsize=(5.5, 4.5)); plt.imshow(k, cmap="RdBu_r", vmin=-1, vmax=1); plt.colorbar()
et = SAYISAL + ["harcama", "ayrildi"]; plt.xticks(range(len(et)), et, rotation=45); plt.yticks(range(len(et)), et)
for i in range(len(et)):
    for j in range(len(et)):
        plt.text(j, i, f"{k[i,j]:.2f}", ha="center", va="center", fontsize=7)
plt.title("Korelasyon"); plt.tight_layout(); plt.savefig(f"{C}/korelasyon.png", dpi=120); plt.close()
print("yazıldı:", ", ".join(sorted(os.listdir(C))))
