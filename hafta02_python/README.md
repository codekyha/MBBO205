# Hafta 2 — Python, sanal ortam, NumPy ve pandas

## Amaç
Yapay zekâ iş akışının dili olan Python'da sanal ortam disiplini, temel veri yapıları, dosya
okuma/yazma ve NumPy/pandas ile vektörel hesaplama.

## İçerik
| Dosya | Konu |
|---|---|
| `01_temeller.py` | Fonksiyon, sözlük, liste üreteci, `json`, `argparse`, hata yönetimi |
| `02_numpy_pandas.py` | Dizi işlemleri, yayın (broadcasting), DataFrame süzme, gruplama |
| `lab02.py` | Lab iskeleti (boş fonksiyonlar, testleri geçecek biçimde doldurulur) |
| `test_lab02.py` | Lab için otomatik kontrol |

## Komutlar
```bash
# Sanal ortam (kök dizinde bir kez)
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

cd hafta02_python
python 01_temeller.py --ad "Ayşe" --tekrar 3
python 02_numpy_pandas.py
pytest -q test_lab02.py        # lab kontrolü
```

## Beklenen çıktı
`02_numpy_pandas.py` 1 000 000 elemanlı dizide döngü ile NumPy vektörel toplamın süre farkını
(tipik olarak 50–100 kat) ve küçük bir DataFrame üzerinde şehir bazlı ortalama tabloyu yazar.

## Lab 2 görevi
`lab02.py` içindeki üç fonksiyonu doldurun: `normalize` (min-max), `kelime_sayac` (metin → sözlük),
`en_yuksek_k` (DataFrame'de sütuna göre ilk k satır). `pytest -q test_lab02.py` tamamen geçmeli.

## Sorun giderme
- `ModuleNotFoundError: numpy`: sanal ortam etkin değil; `source .venv/bin/activate`.
- `pip install` çok yavaşsa `pip install -i https://pypi.org/simple ...` ile yansıyı sabitleyin.
