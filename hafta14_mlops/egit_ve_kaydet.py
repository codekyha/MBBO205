#!/usr/bin/env python3
"""Sürümlü model kaydı: model + meta veri (veri sağlaması, metrikler, ortam)."""
import argparse, hashlib, json, os, platform, sys, datetime, joblib, sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score, f1_score
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol, cikti_dizini, VERI

ap = argparse.ArgumentParser(); ap.add_argument("--surum", default="1.0.0"); a = ap.parse_args()
df = veri_yukle(); X, y = ozellik_hedef(df); Xe, Xt, ye, yt = bol(X, y); C = cikti_dizini(__file__)
m = RandomForestClassifier(n_estimators=300, random_state=42, n_jobs=-1).fit(Xe, ye); pr = m.predict_proba(Xt)[:, 1]
meta = {"surum": a.surum, "tarih": datetime.datetime.now().isoformat(timespec="seconds"),
        "veri_sha256": hashlib.sha256(open(VERI, "rb").read()).hexdigest()[:16], "n_egitim": len(Xe), "n_test": len(Xt),
        "ozellikler": list(X.columns), "metrik": {"roc_auc": round(float(roc_auc_score(yt, pr)), 4), "f1": round(float(f1_score(yt, pr >= .5)), 4)},
        "ortam": {"python": platform.python_version(), "sklearn": sklearn.__version__},
        "egitim_dagilimi": {k: {"ort": float(Xe[k].mean()), "std": float(Xe[k].std())} for k in ["yas", "gelir", "kidem_ay", "aylik_islem"]}}
joblib.dump({"model": m, "sutunlar": list(X.columns), "meta": meta}, f"{C}/model_v{a.surum}.pkl")
json.dump(meta, open(f"{C}/meta.json", "w"), indent=2, ensure_ascii=False)
print(json.dumps(meta["metrik"]), "->", f"cikti/model_v{a.surum}.pkl, cikti/meta.json")
