# ortak/ — Paylaşılan modüller

| Dosya | Görev |
|---|---|
| `veri_uret.py` | `veri/musteri.csv` (1 000 satır, sınıflandırma + regresyon hedefli sentetik müşteri verisi) ve `veri/kirli_musteri.csv` (ETL dersi için kasıtlı bozulmuş sürüm) üretir. |
| `yardimci.py` | Haftalık betiklerin ortak kullandığı yükleme, bölme ve raporlama fonksiyonları. |

## Komutlar

```bash
python ortak/veri_uret.py            # kök dizinden
python ortak/veri_uret.py --n 5000   # daha büyük veri
```

Veri sözlüğü (`veri/musteri.csv`):

| Sütun | Tür | Açıklama |
|---|---|---|
| `musteri_id` | int | Benzersiz kimlik |
| `yas` | int | 18–75 |
| `gelir` | float | Aylık gelir (TL) |
| `kidem_ay` | int | Müşteri olma süresi |
| `aylik_islem` | int | Aylık işlem sayısı |
| `sehir` | kategori | Istanbul, Ankara, Izmir, Bursa, Antalya |
| `segment` | kategori | Bireysel, KOBI, Kurumsal |
| `harcama` | float | Regresyon hedefi: aylık harcama (TL) |
| `ayrildi` | 0/1 | Sınıflandırma hedefi: müşteri kaybı (churn) |
