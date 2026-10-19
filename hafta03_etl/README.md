# Hafta 3 — Veri toplama, ETL ve veri kalitesi

## Amaç
Gerçek projelerde zamanın büyük kısmı veri toplama ve temizlemeye gider. Bu hafta bir HTTP
kaynağından veri çekme (çevrimdışı yedekli), kirli CSV'yi temizleme (Extract–Transform–Load) ve
veri kalitesi raporu üretme.

## İçerik
| Dosya | Konu |
|---|---|
| `01_veri_cek.py` | `requests` ile JSON API'den çekme; ağ yoksa `veri/ornek_api.json` yedeği |
| `02_temizle.py` | `veri/kirli_musteri.csv` → tip dönüşümü, eksik/uç değer, tutarsız yazım, yinelenen satır |
| `03_kalite_raporu.py` | Eksiklik, benzersizlik, aralık ve şema kontrolleri; Markdown rapor |
| `sema.yaml` | Beklenen şema (sütun tipi ve aralıkları) |

## Komutlar
```bash
python ortak/veri_uret.py          # kökten, kirli veriyi üretir
cd hafta03_etl
python 01_veri_cek.py
python 02_temizle.py               # cikti/temiz_musteri.csv
python 03_kalite_raporu.py         # cikti/kalite_raporu.md
```

## Beklenen çıktı
`02_temizle.py` her adımda kaç satırın etkilendiğini yazar (ör. 30 yinelenen satır, 65 eksik
değer, 10 uç değer). `03_kalite_raporu.py` temiz veri için şema ihlali 0 raporlamalıdır.

## Lab 3 görevi
1. `02_temizle.py` içine `kidem_ay` için mantıksal kontrol ekleyin (yas×12'den büyük olamaz).
2. `sema.yaml` dosyasına `harcama` için bir üst sınır ekleyin ve raporun bunu yakaladığını gösterin.
3. Temiz veriyi hem CSV hem Parquet olarak kaydedin; boyutları karşılaştırın (`pip install pyarrow`).

## Sorun giderme
- API erişilemiyorsa betik yerel yedeğe düşer ve bunu ekrana yazar; bu bir hata değildir.
- `12.500,00` gibi Türkçe sayı biçimi için `02_temizle.py` içindeki `tr_sayi` fonksiyonuna bakın.
