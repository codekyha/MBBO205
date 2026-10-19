#!/usr/bin/env python3
"""Izgara ve rastgele hiperparametre araması."""
import argparse, os, sys, time
from scipy.stats import randint
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol

ap = argparse.ArgumentParser(); ap.add_argument("--n_iter", type=int, default=15); a = ap.parse_args()
df = veri_yukle(); X, y = ozellik_hedef(df); Xe, Xt, ye, yt = bol(X, y)
m = RandomForestClassifier(random_state=42, n_jobs=-1)
izgara = {"n_estimators": [100, 300], "max_depth": [4, 8, None], "min_samples_split": [2, 10]}
t = time.perf_counter(); g = GridSearchCV(m, izgara, cv=3, scoring="roc_auc", n_jobs=-1).fit(Xe, ye)
print(f"Izgara   : {len(g.cv_results_['params'])} kombinasyon, {time.perf_counter()-t:.1f} s, CV AUC {g.best_score_:.3f}, test AUC {g.score(Xt, yt):.3f}\n   {g.best_params_}")
dagilim = {"n_estimators": randint(50, 400), "max_depth": [3, 5, 8, 12, None], "min_samples_split": randint(2, 20), "max_features": ["sqrt", 0.5, None]}
t = time.perf_counter(); r = RandomizedSearchCV(m, dagilim, n_iter=a.n_iter, cv=3, scoring="roc_auc", random_state=42, n_jobs=-1).fit(Xe, ye)
print(f"Rastgele : {a.n_iter} deneme, {time.perf_counter()-t:.1f} s, CV AUC {r.best_score_:.3f}, test AUC {r.score(Xt, yt):.3f}\n   {r.best_params_}")
