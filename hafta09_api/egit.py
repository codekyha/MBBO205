#!/usr/bin/env python3
"""Servis edilecek churn modelini eğitir (Hafta 5 ile aynı özellikler)."""
import os, sys, joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol

df = veri_yukle(); X, y = ozellik_hedef(df); Xe, Xt, ye, yt = bol(X, y)
m = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1).fit(Xe, ye)
print(f"test AUC: {roc_auc_score(yt, m.predict_proba(Xt)[:,1]):.3f}")
os.makedirs("model", exist_ok=True)
joblib.dump({"model": m, "sutunlar": list(X.columns), "ad": "rastgele_orman"}, "model/model_churn.pkl")
print("model/model_churn.pkl yazıldı")
