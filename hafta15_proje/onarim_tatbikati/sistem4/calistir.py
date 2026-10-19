import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
rng = np.random.default_rng(0)
X = rng.normal(size=(500, 3)) * [1, 100, 1000]; y = (X[:, 0] + X[:, 1] / 100 > 0).astype(int)
sc = StandardScaler().fit(X); m = LogisticRegression().fit(sc.transform(X), y)
# Üretim: yeni veri geliyor
Xy = rng.normal(size=(5, 3)) * [1, 100, 1000]
print("tahmin olasılıkları:", m.predict_proba(Xy)[:, 1].round(3))   # ölçekleme unutuldu
print("gerçek:", (Xy[:, 0] + Xy[:, 1] / 100 > 0).astype(int))
