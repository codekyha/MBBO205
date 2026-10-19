"""Hafta 9 api.py örnek alınarak doldurulacak."""
from fastapi import FastAPI
app = FastAPI()
@app.get("/saglik")
def saglik(): return {"durum": "ok"}
