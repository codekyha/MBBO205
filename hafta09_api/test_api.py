from fastapi.testclient import TestClient
from api import app
c = TestClient(app)
ORNEK = {"yas": 34, "gelir": 28000, "kidem_ay": 6, "aylik_islem": 3, "sehir": "Istanbul", "segment": "Bireysel"}

def test_saglik():
    assert c.get("/saglik").json()["durum"] == "ok"

def test_tahmin():
    r = c.post("/tahmin", json=ORNEK); assert r.status_code == 200
    j = r.json(); assert 0 <= j["ayrilma_olasiligi"] <= 1 and j["tahmin"] in (0, 1)

def test_gecersiz():
    assert c.post("/tahmin", json={**ORNEK, "yas": -5}).status_code == 422
    assert c.post("/tahmin", json={**ORNEK, "sehir": "Paris"}).status_code == 422
