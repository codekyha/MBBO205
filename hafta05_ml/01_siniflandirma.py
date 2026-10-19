#!/usr/bin/env python3
"""Churn sınıflandırması: lojistik regresyon ve rastgele orman."""
import os, sys, joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol, cikti_dizini

df = veri_yukle(); X, y = ozellik_hedef(df, "ayrildi"); Xe, Xt, ye, yt = bol(X, y)
C = cikti_dizini(__file__)
modeller = {
    "lojistik": Pipeline([("olcek", StandardScaler()), ("m", LogisticRegression(max_iter=1000))]),
    "rastgele_orman": RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1),
}
sonuc = []
for ad, m in modeller.items():
    m.fit(Xe, ye); p = m.predict(Xt); pr = m.predict_proba(Xt)[:, 1]
    sonuc.append({"model": ad, "dogruluk": accuracy_score(yt, p), "f1": f1_score(yt, p), "roc_auc": roc_auc_score(yt, pr)})
tablo = pd.DataFrame(sonuc).round(3); print(tablo.to_string(index=False))
en_iyi = tablo.sort_values("roc_auc").iloc[-1]["model"]
joblib.dump({"model": modeller[en_iyi], "sutunlar": list(X.columns)}, f"{C}/model_churn.pkl")
print(f"\nen iyi model: {en_iyi} -> cikti/model_churn.pkl")
rf = modeller["rastgele_orman"]
print("\nözellik önemleri (RF):")
print(pd.Series(rf.feature_importances_, index=X.columns).sort_values(ascending=False).round(3).head(8).to_string())
