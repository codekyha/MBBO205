#!/usr/bin/env python3
"""Harcama regresyonu: doğrusal regresyon ve gradyan artırma."""
import os, sys, joblib
import numpy as np, pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol, cikti_dizini

df = veri_yukle(); X, y = ozellik_hedef(df, "harcama"); Xe, Xt, ye, yt = bol(X, y)
C = cikti_dizini(__file__)
modeller = {
    "dogrusal": Pipeline([("olcek", StandardScaler()), ("m", LinearRegression())]),
    "gradyan_artirma": GradientBoostingRegressor(n_estimators=300, max_depth=3, learning_rate=0.05, random_state=42),
}
sonuc = []
for ad, m in modeller.items():
    m.fit(Xe, ye); p = m.predict(Xt)
    sonuc.append({"model": ad, "MAE": mean_absolute_error(yt, p),
                  "RMSE": np.sqrt(mean_squared_error(yt, p)), "R2": r2_score(yt, p)})
tablo = pd.DataFrame(sonuc).round(3); print(tablo.to_string(index=False))
en_iyi = tablo.sort_values("R2").iloc[-1]["model"]
joblib.dump({"model": modeller[en_iyi], "sutunlar": list(X.columns)}, f"{C}/model_harcama.pkl")
print(f"\nen iyi model: {en_iyi} -> cikti/model_harcama.pkl")
