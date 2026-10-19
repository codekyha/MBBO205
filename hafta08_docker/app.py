#!/usr/bin/env python3
"""Konteyner içinde çalışan örnek: sentetik veri üretir, model eğitir, kaydeder."""
import os, time, joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score

n_est = int(os.environ.get("N_ESTIMATORS", 200))
rng = np.random.default_rng(42)
X = rng.normal(size=(4000, 8)); y = (X[:, 0] + 0.5 * X[:, 1] ** 2 - X[:, 2] + rng.normal(0, .5, 4000) > 0).astype(int)
Xe, Xt, ye, yt = train_test_split(X, y, test_size=.2, random_state=42)
t = time.perf_counter(); m = RandomForestClassifier(n_estimators=n_est, random_state=42, n_jobs=-1).fit(Xe, ye)
print(f"konteyner içi eğitim: n_estimators={n_est}, süre {time.perf_counter()-t:.2f} s, test AUC {roc_auc_score(yt, m.predict_proba(Xt)[:,1]):.3f}")
os.makedirs("cikti", exist_ok=True); joblib.dump(m, "cikti/model.pkl")
print("model -> /app/cikti/model.pkl   (dışarı almak için: -v $(pwd)/cikti:/app/cikti)")
print("ana makine kimliği:", os.uname().nodename)
