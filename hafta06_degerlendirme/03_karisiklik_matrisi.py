#!/usr/bin/env python3
"""Karışıklık matrisi, ROC ve maliyete dayalı eşik seçimi."""
import argparse, os, sys
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, classification_report
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol, cikti_dizini

ap = argparse.ArgumentParser(); ap.add_argument("--fn_maliyet", type=float, default=500); ap.add_argument("--fp_maliyet", type=float, default=50)
a = ap.parse_args()
df = veri_yukle(); X, y = ozellik_hedef(df); Xe, Xt, ye, yt = bol(X, y); C = cikti_dizini(__file__)
m = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1).fit(Xe, ye); pr = m.predict_proba(Xt)[:, 1]
print("eşik 0.5 için rapor:\n", classification_report(yt, pr >= .5, digits=3))
print("karışıklık matrisi [[TN FP],[FN TP]]:\n", confusion_matrix(yt, pr >= .5))
esikler = np.linspace(.05, .95, 91); maliyet = []
for e in esikler:
    tn, fp, fn, tp = confusion_matrix(yt, pr >= e).ravel(); maliyet.append(fn * a.fn_maliyet + fp * a.fp_maliyet)
en = esikler[int(np.argmin(maliyet))]
print(f"\nFN={a.fn_maliyet}, FP={a.fp_maliyet} için en düşük maliyetli eşik: {en:.2f} (maliyet {min(maliyet):.0f}; eşik 0.5'te {maliyet[45]:.0f})")
fpr, tpr, _ = roc_curve(yt, pr)
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(fpr, tpr, label=f"AUC={roc_auc_score(yt, pr):.3f}"); ax[0].plot([0, 1], [0, 1], "--", c="gray"); ax[0].set_xlabel("FPR"); ax[0].set_ylabel("TPR"); ax[0].legend(); ax[0].set_title("ROC")
ax[1].plot(esikler, maliyet); ax[1].axvline(en, c="r", ls="--"); ax[1].set_xlabel("eşik"); ax[1].set_ylabel("toplam maliyet"); ax[1].set_title("Eşik taraması")
plt.tight_layout(); plt.savefig(f"{C}/roc_ve_esik.png", dpi=120); print("cikti/roc_ve_esik.png yazıldı")
