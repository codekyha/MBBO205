"""FastAPI model servisi."""
import os, socket
from typing import Literal
import joblib, pandas as pd
from fastapi import FastAPI, HTTPException, Response
from pydantic import BaseModel, Field

MODEL_YOLU = os.environ.get("MODEL_YOLU", "model/model_churn.pkl")
app = FastAPI(title="MBBO205 Churn Servisi", version="1.0")
_paket = None

def paket():
    global _paket
    if _paket is None:
        if not os.path.exists(MODEL_YOLU):
            raise HTTPException(503, f"model bulunamadı: {MODEL_YOLU} (önce `python egit.py`)")
        _paket = joblib.load(MODEL_YOLU)
    return _paket

class Musteri(BaseModel):
    yas: int = Field(ge=18, le=100)
    gelir: float = Field(ge=0)
    kidem_ay: int = Field(ge=0, le=240)
    aylik_islem: int = Field(ge=0)
    sehir: Literal["Istanbul", "Ankara", "Izmir", "Bursa", "Antalya"]
    segment: Literal["Bireysel", "KOBI", "Kurumsal"]

def ozellik(m: list[Musteri], sutunlar: list[str]) -> pd.DataFrame:
    df = pd.DataFrame([x.model_dump() for x in m])
    X = pd.get_dummies(df, columns=["sehir", "segment"])
    return X.reindex(columns=sutunlar, fill_value=0)

@app.get("/saglik")
def saglik():
    return {"durum": "ok", "model_var": os.path.exists(MODEL_YOLU), "sunucu": socket.gethostname()}

@app.post("/tahmin")
def tahmin(m: Musteri, response: Response):
    p = paket(); pr = float(p["model"].predict_proba(ozellik([m], p["sutunlar"]))[0, 1])
    response.headers["X-Sunucu"] = socket.gethostname()
    return {"ayrilma_olasiligi": round(pr, 3), "tahmin": int(pr >= .5), "model": p["ad"]}

@app.post("/tahmin/toplu")
def toplu(ms: list[Musteri]):
    if len(ms) > 1000:
        raise HTTPException(413, "en fazla 1000 kayıt")
    p = paket(); pr = p["model"].predict_proba(ozellik(ms, p["sutunlar"]))[:, 1]
    return {"n": len(ms), "ayrilma_olasiligi": [round(float(x), 3) for x in pr]}
