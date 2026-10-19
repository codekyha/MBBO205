#!/usr/bin/env python3
"""PyTorch MLP ile churn sınıflandırması."""
import argparse, os, sys, time
import numpy as np
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
import torch, torch.nn as nn
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import roc_auc_score
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, ozellik_hedef, bol, cikti_dizini

ap = argparse.ArgumentParser(); ap.add_argument("--epok", type=int, default=30); ap.add_argument("--lr", type=float, default=1e-3)
ap.add_argument("--gizli", type=int, default=64); ap.add_argument("--dropout", type=float, default=0.2); a = ap.parse_args()
cihaz = "cuda" if torch.cuda.is_available() else "cpu"; print("cihaz:", cihaz)
df = veri_yukle(); X, y = ozellik_hedef(df); Xe, Xt, ye, yt = bol(X, y); C = cikti_dizini(__file__)
sc = StandardScaler().fit(Xe)
te = lambda A: torch.tensor(np.asarray(A, dtype=np.float32), device=cihaz)
Xe_t, Xt_t, ye_t = te(sc.transform(Xe)), te(sc.transform(Xt)), te(ye.to_numpy()).unsqueeze(1)
model = nn.Sequential(nn.Linear(X.shape[1], a.gizli), nn.ReLU(), nn.Dropout(a.dropout),
                      nn.Linear(a.gizli, a.gizli // 2), nn.ReLU(), nn.Linear(a.gizli // 2, 1)).to(cihaz)
opt = torch.optim.Adam(model.parameters(), lr=a.lr); kayip_fn = nn.BCEWithLogitsLoss()
veri = torch.utils.data.DataLoader(torch.utils.data.TensorDataset(Xe_t, ye_t), batch_size=64, shuffle=True)
kayiplar, t0 = [], time.perf_counter()
for e in range(a.epok):
    model.train(); toplam = 0
    for xb, yb in veri:
        opt.zero_grad(); k = kayip_fn(model(xb), yb); k.backward(); opt.step(); toplam += k.item() * len(xb)
    kayiplar.append(toplam / len(Xe_t))
    if (e + 1) % 5 == 0: print(f"epok {e+1:3d}  kayıp {kayiplar[-1]:.4f}")
model.eval()
with torch.no_grad(): pr = torch.sigmoid(model(Xt_t)).cpu().numpy().ravel()
print(f"\nsüre {time.perf_counter()-t0:.1f} s, test AUC (MLP): {roc_auc_score(yt, pr):.3f}")
plt.figure(figsize=(5, 3.5)); plt.plot(kayiplar); plt.xlabel("epok"); plt.ylabel("BCE kaybı"); plt.title("Eğitim kaybı"); plt.tight_layout()
plt.savefig(f"{C}/kayip_egrisi.png", dpi=120); torch.save(model.state_dict(), f"{C}/mlp.pt"); print("cikti/kayip_egrisi.png, cikti/mlp.pt yazıldı")
