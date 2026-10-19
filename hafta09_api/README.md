# Hafta 9 — Model dağıtımı: FastAPI servisi ve Docker Compose

## Amaç
Eğitilmiş modeli HTTP üzerinden sunmak: FastAPI ile `/tahmin` uç noktası, girdi doğrulama
(`pydantic`), sağlık kontrolü, otomatik belge (`/docs`); Docker Compose ile servis + ters vekil
(nginx) birlikte ayağa kaldırma.

## İçerik
| Dosya | Konu |
|---|---|
| `egit.py` | Hafta 5 ile aynı veri üzerinde churn modelini eğitir → `model/model_churn.pkl` |
| `api.py` | FastAPI uygulaması: `/saglik`, `/tahmin`, `/tahmin/toplu` |
| `istek.sh` | `curl` ile örnek istekler |
| `istemci.py` | Python `requests` istemcisi; 200 istek ile gecikme ölçümü |
| `Dockerfile`, `docker-compose.yml`, `nginx.conf` | Dağıtım |
| `test_api.py` | `TestClient` ile birim testleri |

## Komutlar
```bash
cd hafta09_api
python egit.py                                     # model/model_churn.pkl

# A) Yerel (Docker'sız)
uvicorn api:app --reload --port 8000
# başka bir terminalde:
bash istek.sh
python istemci.py --n 200
pytest -q test_api.py

# B) Docker Compose (api + nginx :8080)
docker compose up --build -d
curl -s localhost:8080/saglik
bash istek.sh 8080
docker compose logs -f api
docker compose down
```

## Beklenen çıktı
`POST /tahmin` yanıtı: `{"ayrilma_olasiligi": 0.27, "tahmin": 0, "model": "rastgele_orman"}`.
`istemci.py` ortalama gecikmeyi (yerelde tipik olarak 5–20 ms) ve p95 değerini yazar.

## Lab 9 görevi
1. Hafta 5 regresyon modelini `/harcama` uç noktası olarak ekleyin.
2. `docker compose up --scale api=3` ile üç kopya çalıştırın; nginx'in yük dağıttığını `X-Sunucu` başlığından gösterin.
3. Geçersiz girdi (negatif yaş) için 422 döndüğünü testle doğrulayın.

## Sorun giderme
- `model bulunamadı`: önce `python egit.py`.
- 8000/8080 portu doluysa `--port` veya `docker-compose.yml` port eşlemesini değiştirin.
