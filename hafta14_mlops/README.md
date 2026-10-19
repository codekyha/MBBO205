# Hafta 14 — MLOps: izleme, model kartı, etik/KVKK, Git ve CI/CD

## Amaç
Modelin yaşam döngüsü: sürümleme, otomatik test, sürekli bütünleştirme, üretimde izleme (veri kayması),
model kartı ve KVKK uyumu. Bu haftanın çıktıları proje teslimine doğrudan girer (rubrik: Model kartı/etik/KVKK 15,
Takım ve Git 15).

## İçerik
| Dosya | Konu |
|---|---|
| `egit_ve_kaydet.py` | Model + meta veri (sürüm, veri sağlaması, metrikler) → `cikti/model_v*.pkl`, `cikti/meta.json` |
| `izleme.py` | Yeni gelen veride özellik dağılım kayması (PSI, KS testi) ve tahmin dağılımı uyarısı |
| `model_karti.md` | Doldurulacak model kartı şablonu (Mitchell vd. 2019 şemasına göre) |
| `kvkk_kontrol_listesi.md` | Proje teslimi için KVKK/etik kontrol listesi |
| `test_model.py` | Birim testleri: şema, deterministiklik, en düşük AUC eşiği |
| `.github/workflows/ci.yml` | Her `push`'ta test çalıştıran GitHub Actions akışı |
| `git_komutlari.md` | Takım çalışması için Git komut rehberi (dal, PR, çatışma) |
| `pre-commit-config.yaml` | Biçim ve lint kancaları (`pip install pre-commit`) |

## Komutlar
```bash
cd hafta14_mlops
python egit_ve_kaydet.py --surum 1.0.0
python izleme.py                                   # kayma simülasyonu ile
python izleme.py --yeni_veri ../veri/musteri.csv   # gerçek yeni veri ile
pytest -q
# Git / CI
git init && git add . && git commit -m "ilk sürüm"
cp -r .github ../.github                           # CI dosyasını depo köküne
pre-commit install && pre-commit run --all-files
```

## Beklenen çıktı
`izleme.py` kaydırılmış veride `gelir` için PSI > 0,25 (uyarı) ve KS p-değeri < 0,05 raporlar;
`pytest` üç testi geçer; CI akışı GitHub'da yeşil olur.

## Lab 14 görevi
1. `model_karti.md` dosyasını Hafta 5 modeli için eksiksiz doldurun.
2. İzleme betiğine tahmin dağılımı için bir uyarı eşiği ekleyin ve testini yazın.
3. Takım deposunda bir özellik dalı açıp PR ile birleştirin; inceleme yorumlarını ekran görüntüsüyle teslim edin.

## Sorun giderme
- `pytest` modeli bulamıyorsa önce `egit_ve_kaydet.py`.
- CI'da `veri/musteri.csv` yoksa akış `ortak/veri_uret.py` ile üretir (bkz. `ci.yml`).
