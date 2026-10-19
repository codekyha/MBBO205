# Hafta 5 — Denetimli öğrenme: sınıflandırma ve regresyon

## Amaç
scikit-learn boru hattı (`Pipeline`) disipliniyle eğitim/test ayrımı, ölçekleme, kategorik kodlama;
müşteri kaybı için sınıflandırma, aylık harcama için regresyon. Modeller `cikti/` altına `joblib`
ile kaydedilir ve Hafta 9'da servis edilir.

## İçerik
| Dosya | Konu |
|---|---|
| `01_siniflandirma.py` | Lojistik regresyon vs. rastgele orman; doğruluk, F1, ROC-AUC |
| `02_regresyon.py` | Doğrusal regresyon vs. gradyan artırma; MAE, RMSE, $R^2$ |

## Komutlar
```bash
cd hafta05_ml
python 01_siniflandirma.py          # cikti/model_churn.pkl
python 02_regresyon.py              # cikti/model_harcama.pkl
```

## Beklenen çıktı
Sentetik veride rastgele orman için ROC-AUC ≈ 0,70–0,80, regresyon için $R^2$ ≈ 0,85–0,95
beklenir (veri üretim tohumuna bağlı küçük sapmalar normaldir). Ekranda özellik önemleri listelenir.

## Lab 5 görevi
1. `class_weight="balanced"` ekleyince F1 nasıl değişiyor? Tabloya ekleyin.
2. `gelir` özelliğini çıkarıp modeli yeniden eğitin; AUC düşüşünü yorumlayın.
3. Regresyonda hedefi `log1p(harcama)` yapıp RMSE'yi orijinal ölçekte raporlayın.

## Sorun giderme
- `FileNotFoundError ... musteri.csv`: kökte `python ortak/veri_uret.py`.
- Uyarı `ConvergenceWarning`: `max_iter` değerini artırın (betikte 1000).
