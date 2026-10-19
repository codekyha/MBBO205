# Hafta 6 — Model değerlendirme, çapraz doğrulama ve hiperparametre arama

## Amaç
Tek bir test bölmesine güvenmenin tehlikesi; k-katlı çapraz doğrulama, öğrenme eğrisi, ızgara ve
rastgele arama, karışıklık matrisi / ROC / kesme eşiği seçimi.

## İçerik
| Dosya | Konu |
|---|---|
| `01_capraz_dogrulama.py` | 5-katlı katmanlı CV, ortalama ± std; öğrenme eğrisi (PNG) |
| `02_hiperparametre.py` | `GridSearchCV` vs. `RandomizedSearchCV`; süre ve skor karşılaştırması |
| `03_karisiklik_matrisi.py` | Karışıklık matrisi, ROC eğrisi, eşik taraması ile iş maliyeti optimizasyonu |

## Komutlar
```bash
cd hafta06_degerlendirme
python 01_capraz_dogrulama.py
python 02_hiperparametre.py --n_iter 20
python 03_karisiklik_matrisi.py --fn_maliyet 500 --fp_maliyet 50
```

## Beklenen çıktı
CV skorlarının std değeri 0,02–0,05 civarında; rastgele arama benzer skora ızgara aramanın
yaklaşık üçte biri sürede ulaşır; eşik taraması 0,5'ten farklı (genelde daha düşük) bir en iyi eşik verir.

## Lab 6 görevi
1. Katlama sayısını 3, 5, 10 yapıp std değişimini yorumlayın.
2. Arama uzayına `min_samples_leaf` ekleyin.
3. Kendi maliyet senaryonuzu (FN ve FP maliyeti) tanımlayıp en iyi eşiği raporlayın.

## Sorun giderme
- Arama çok uzun sürüyorsa `--n_iter` düşürün veya `n_jobs=-1` ile tüm çekirdekleri kullanın.
