#!/usr/bin/env python3
"""Veri kayması izleme: PSI ve KS testi; tahmin dağılımı uyarısı."""
import argparse, glob, os, sys, joblib
import numpy as np, pandas as pd
from scipy.stats import ks_2samp
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, SAYISAL

def psi(ref: np.ndarray, yeni: np.ndarray, kutu: int = 10) -> float:
    kenar = np.quantile(ref, np.linspace(0, 1, kutu + 1)); kenar[0], kenar[-1] = -np.inf, np.inf
    r = np.histogram(ref, kenar)[0] / len(ref) + 1e-6; y = np.histogram(yeni, kenar)[0] / len(yeni) + 1e-6
    return float(np.sum((y - r) * np.log(y / r)))

ap = argparse.ArgumentParser(); ap.add_argument("--yeni_veri", default=None); a = ap.parse_args()
ref = veri_yukle()
if a.yeni_veri: yeni = pd.read_csv(a.yeni_veri); print("yeni veri:", a.yeni_veri)
else:
    rng = np.random.default_rng(1); yeni = ref.sample(400, random_state=1).copy()
    yeni["gelir"] *= rng.uniform(1.4, 1.8, len(yeni)); yeni["kidem_ay"] = (yeni["kidem_ay"] * .6).astype(int); print("yeni veri: simülasyon (gelir ↑, kıdem ↓)")
print(f"\n{'özellik':12s} {'PSI':>7s} {'KS p':>9s}  durum")
for k in SAYISAL:
    p = psi(ref[k].to_numpy(), yeni[k].to_numpy()); ks = ks_2samp(ref[k], yeni[k]).pvalue
    durum = "UYARI: belirgin kayma" if p > .25 else ("izle" if p > .1 else "ok")
    print(f"{k:12s} {p:7.3f} {ks:9.2e}  {durum}")
modeller = sorted(glob.glob("cikti/model_v*.pkl"))
if modeller:
    pk = joblib.load(modeller[-1]); Xr, _ = ozellik_hedef(ref); Xy, _ = ozellik_hedef(yeni); Xy = Xy.reindex(columns=pk["sutunlar"], fill_value=0)
    pr_ref = pk["model"].predict_proba(Xr)[:, 1]; pr_yeni = pk["model"].predict_proba(Xy)[:, 1]
    print(f"\ntahmin dağılımı ({os.path.basename(modeller[-1])}): referans ort {pr_ref.mean():.3f} / yeni ort {pr_yeni.mean():.3f}  PSI {psi(pr_ref, pr_yeni):.3f}")
    if abs(pr_yeni.mean() - pr_ref.mean()) > .1: print("UYARI: pozitif tahmin oranı %10'dan fazla değişti; yeniden eğitim değerlendirilmeli")
else: print("\n(model yok; önce egit_ve_kaydet.py)")
