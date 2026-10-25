# MBBO205 Bulut Bilişim ve Yapay Zekâ — Kod Tabanı, Ders Notları ve Sunumlar

Bu depo, dersin 15 haftalık uygulama (lab) içeriğinin tamamını, ders not ve sunumlarını haftalık paketler hâlinde içerir.
Her `haftaNN_*` dizini kendi `README.md` dosyasında o haftanın amacını, gerekli komutları, beklenen
çıktıyı ve lab görevini açıklar. Tüm kodlar Linux (Ubuntu 22.04/24.04) üzerinde test edilmiştir.

## Dizin yapısı

| Dizin | Konu | Araçlar |
|---|---|---|
| `hafta01_linux` | Linux ve kabuk temelleri | bash, grep, awk, sed, ps |
| `hafta02_python` | Python, sanal ortam, NumPy/pandas | venv, pip |
| `hafta03_etl` | Veri toplama, ETL, veri kalitesi | requests, pandas |
| `hafta04_eda` | Keşifsel veri analizi ve görselleştirme | pandas, matplotlib |
| `hafta05_ml` | Denetimli öğrenme: sınıflandırma, regresyon | scikit-learn |
| `hafta06_degerlendirme` | Model değerlendirme, çapraz doğrulama, hiperparametre | scikit-learn |
| `hafta07_denetimsiz` | Kümeleme, boyut indirgeme, ara sınav hazırlığı | scikit-learn |
| `hafta08_docker` | Konteynerler: Docker temelleri | docker |
| `hafta09_api` | Model dağıtımı: FastAPI + Docker Compose | fastapi, uvicorn, docker compose |
| `hafta10_bulut` | Bulut hizmet modelleri, S3 uyumlu depolama, ölçekleme | MinIO, boto3, nginx |
| `hafta11_derin` | Derin öğrenme ve Hugging Face | PyTorch, transformers |
| `hafta12_llm` | Yerel büyük dil modelleri: Ollama, istem mühendisliği | ollama |
| `hafta13_rag` | RAG ve bellek yönetimi | scikit-learn, ollama |
| `hafta14_mlops` | MLOps: izleme, model kartı, etik/KVKK, CI/CD | git, pytest, GitHub Actions |
| `hafta15_proje` | Proje sunumları, onarım tatbikatı, final hazırlığı | — |
| `ortak` | Tüm haftaların paylaştığı yardımcı modüller ve veri üretici | — |

## Hızlı başlangıç

```bash
# 1. Depoyu açın
cd mbbo205-kod

# 2. Sanal ortam ve temel bağımlılıklar (hafta 2–7, 13–14 için yeterli)
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3. Ortak örnek veri kümesini üretin (hafta 3–7, 9, 14 bunu kullanır)
python ortak/veri_uret.py

# 4. Bir haftanın tamamını çalıştırın
make hafta05
```

Ağır bağımlılıklar (PyTorch, transformers, boto3) ilgili haftanın `requirements.txt` dosyasında ayrıdır;
yalnızca o haftaya gelince kurun. Docker ve Ollama gerektiren haftalar için kurulum komutları ilgili
README içinde verilmiştir.

## Makefile hedefleri

```bash
make kur          # .venv oluşturur ve requirements.txt kurar
make veri         # ortak/veri_uret.py ile örnek veri üretir
make hafta01 ... make hafta15
make test         # hafta14 birim testlerini çalıştırır
make temizle      # üretilen çıktı dosyalarını (cikti/, *.pkl, *.png) siler
```

## Genel kurallar

- Her betik, bulunduğu haftanın dizininden çalıştırılır (`cd haftaNN_* && python 01_xxx.py`).
- Üretilen dosyalar `cikti/` alt dizinine yazılır; bu dizin Git'e eklenmez (`.gitignore`).
- Betikler internet erişimi olmadan da çalışacak biçimde tasarlanmıştır: dış kaynak erişilemezse
  yerel örnek veriye düşer ve bunu ekrana yazar.
- Hata alırsanız önce ilgili README'nin "Sorun giderme" bölümüne bakın.

## Lisans

Ders materyali olarak MIT lisansıyla paylaşılır; öğrenciler kendi projelerinde serbestçe kullanabilir. Bu materyaller, her ne şekilde olursa olsun hiçbir garanti verilmeksizin "olduğu gibi" sunulmaktadır; yazar, bunların kullanımından doğabilecek hiçbir sorumluluğu kabul etmez.
