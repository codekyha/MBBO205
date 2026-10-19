# Hafta 11 — Derin öğrenme temelleri ve Hugging Face

## Amaç
PyTorch ile çok katmanlı algılayıcı (MLP): tensörler, otomatik türev, eğitim döngüsü, GPU/CPU seçimi;
Hugging Face `transformers` ile hazır modellerin (duygu analizi, sıfır-atış sınıflandırma) kullanımı.
Hugging Face indirmeleri internet gerektirir; çevrimdışıysa betik bunu bildirir.

## İçerik
| Dosya | Konu |
|---|---|
| `01_mlp_torch.py` | Müşteri verisinde MLP ile churn; kayıp eğrisi (PNG); scikit-learn ile karşılaştırma |
| `02_hf_pipeline.py` | Türkçe duygu analizi ve sıfır-atış sınıflandırma boru hatları |
| `03_ince_ayar_iskelet.py` | Küçük bir Türkçe metin kümesinde ince ayar iskeleti (isteğe bağlı, GPU önerilir) |

## Kurulum
```bash
# CPU sürümü (küçük, çoğu bilgisayar için yeterli)
pip install torch --index-url https://download.pytorch.org/whl/cpu
pip install transformers datasets
# GPU (CUDA 12.x) varsa:
pip install torch --index-url https://download.pytorch.org/whl/cu124
python -c "import torch; print(torch.cuda.is_available())"
```

## Komutlar
```bash
cd hafta11_derin
python 01_mlp_torch.py --epok 30 --lr 1e-3
python 02_hf_pipeline.py
HF_HOME=~/.cache/hf python 02_hf_pipeline.py        # önbellek konumu
python 03_ince_ayar_iskelet.py --epok 1              # isteğe bağlı
```

## Beklenen çıktı
MLP test AUC değeri rastgele ormana yakın (±0,03) olmalı; `cikti/kayip_egrisi.png` düşen bir
eğitim kaybı gösterir. HF boru hattı üç örnek cümle için etiket ve güven skoru yazar (temsilî).

## Lab 11 görevi
1. Gizli katman sayısını ve `dropout` oranını değiştirip aşırı öğrenmeyi kayıp eğrisinde gösterin.
2. `02_hf_pipeline.py` içindeki modeli başka bir Türkçe modelle değiştirin; sonuç farkını tartışın.
3. Eğitim süresini CPU'da ölçün; `torch.set_num_threads` ile iş parçacığı sayısının etkisini raporlayın.

## Sorun giderme
- `OSError: Can't load ... offline`: ağ yok veya model adı yanlış; önce `huggingface-cli download <model>`.
- Bellek yetersiz (`Killed`): Hafta 13 `02_bellek.py` açıklamasına bakın; parti boyutunu küçültün.
