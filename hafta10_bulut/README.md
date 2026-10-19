# Hafta 10 — Bulut hizmet modelleri, nesne depolama ve ölçekleme

## Amaç
IaaS/PaaS/SaaS ayrımı, bölge/erişilebilirlik bölgesi, nesne depolama (S3 API), yatay ölçekleme ve
yük dengeleme. Bulut sağlayıcı hesabı gerektirmeden MinIO (S3 uyumlu) ile yerel laboratuvar.
Gerçek bulut çıktıları ders notlarında temsilîdir; aşağıdaki her şey yerelde çalışır.

## İçerik
| Dosya | Konu |
|---|---|
| `docker-compose.yml` | MinIO (S3 uyumlu depolama) + Hafta 9 API'sinin 3 kopyası + nginx yük dengeleyici |
| `s3_yukle.py` | `boto3` ile kova oluşturma, model ve veri yükleme/indirme, imzalı URL |
| `yuk_testi.py` | Eşzamanlı istekle yük dengeleyici testi; kopya başına istek dağılımı |
| `maliyet_hesabi.py` | Basit TCO: sanal makine vs. sunucusuz vs. yerel sunucu karşılaştırması |
| `bulut_cli_notlari.md` | AWS/GCP/Azure CLI eşdeğer komutları (hesap gerektirir, isteğe bağlı) |

## Komutlar
```bash
pip install boto3
cd hafta10_bulut
docker compose up -d                       # MinIO :9000 (API) :9001 (konsol, minioadmin/minioadmin)
python s3_yukle.py                         # kova + yükleme + listeleme + imzalı URL
python yuk_testi.py --n 300                # nginx :8080 üzerinden 3 api kopyası
python maliyet_hesabi.py --istek_gun 50000 --ay 12
docker compose down -v
```
MinIO konsolu: http://localhost:9001

## Beklenen çıktı
`s3_yukle.py` kovayı, yüklenen nesneleri ve 1 saat geçerli imzalı URL'yi yazar; `yuk_testi.py`
üç kopya arasında yaklaşık eşit (round-robin) dağılım gösterir.

## Lab 10 görevi
1. MinIO'da sürümleme (versioning) açıp aynı nesneyi iki kez yükleyin; sürümleri listeleyin.
2. Bir kopyayı durdurun (`docker compose stop api-2`); yük testi ne gösterir? Sağlık kontrolünün rolünü açıklayın.
3. Maliyet betiğine GPU'lu sanal makine seçeneği ekleyin (saatlik fiyatı sağlayıcı sayfasından alın; kaynağı belirtin).

## Sorun giderme
- `EndpointConnectionError`: MinIO henüz hazır değil; `docker compose ps` ile `healthy` bekleyin.
- Hafta 9 modeli yoksa `cd ../hafta09_api && python egit.py`.
