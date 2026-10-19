#!/usr/bin/env python3
"""k-katlı çapraz doğrulama ve öğrenme eğrisi."""
import os, sys
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, cross_val_score, learning_curve
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, cikti_dizini

df = veri_yukle(); X, y = ozellik_hedef(df); C = cikti_dizini(__file__)
m = RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)
for k in (3, 5, 10):
    cv = StratifiedKFold(n_splits=k, shuffle=True, random_state=42)
    s = cross_val_score(m, X, y, cv=cv, scoring="roc_auc")
    print(f"{k:2d}-katlı ROC-AUC: {s.mean():.3f} ± {s.std():.3f}   katlar: {np.round(s, 3)}")
n, tr, te = learning_curve(m, X, y, cv=5, scoring="roc_auc", train_sizes=np.linspace(.1, 1, 6), n_jobs=-1)
plt.figure(figsize=(6, 4)); plt.plot(n, tr.mean(1), "o-", label="eğitim"); plt.plot(n, te.mean(1), "s-", label="doğrulama")
plt.fill_between(n, te.mean(1) - te.std(1), te.mean(1) + te.std(1), alpha=.2)
plt.xlabel("eğitim örneği"); plt.ylabel("ROC-AUC"); plt.legend(); plt.title("Öğrenme eğrisi"); plt.tight_layout()
plt.savefig(f"{C}/ogrenme_egrisi.png", dpi=120); print("cikti/ogrenme_egrisi.png yazıldı")
