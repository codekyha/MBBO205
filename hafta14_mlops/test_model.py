import glob, os, sys, joblib, numpy as np, pytest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol
from sklearn.metrics import roc_auc_score

@pytest.fixture(scope="module")
def paket():
    m = sorted(glob.glob(os.path.join(os.path.dirname(__file__), "cikti", "model_v*.pkl")))
    if not m: pytest.skip("model yok: önce egit_ve_kaydet.py")
    return joblib.load(m[-1])

def test_sema(paket):
    X, _ = ozellik_hedef(veri_yukle()); assert list(X.columns) == paket["sutunlar"]

def test_deterministik(paket):
    X, _ = ozellik_hedef(veri_yukle()); a = paket["model"].predict_proba(X[:50]); b = paket["model"].predict_proba(X[:50]); assert np.allclose(a, b)

def test_en_dusuk_auc(paket):
    X, y = ozellik_hedef(veri_yukle()); _, Xt, _, yt = bol(X, y); assert roc_auc_score(yt, paket["model"].predict_proba(Xt)[:, 1]) >= 0.65
