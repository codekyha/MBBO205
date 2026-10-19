# Hafta 15 — Proje sunumları, onarım tatbikatı ve final hazırlığı

## Amaç
Dönem projelerinin sunumu ve değerlendirmesi; "arkadaşının sistemini onar" tatbikatıyla hata ayıklama
pratiği; final sınavına hazırlık (kavram haritası, formül kartı, format, örnek sorular).

## İçerik
| Dosya | Konu |
|---|---|
| `proje_rubrigi.md` | 100 puanlık rubrik ve sunum düzeni |
| `proje_sablonu/` | Takımların klonlayacağı proje iskeleti (`README`, dizinler, `Makefile`, model kartı bağlantısı) |
| `onarim_tatbikati/` | Kasıtlı bozulmuş dört küçük sistem; her birinde en az bir hata (`cozumler.md` eğitmen için) |
| `final_formati.md` | Sınav formatı, süre, bölüm ağırlıkları |
| `formul_karti.md` | Sınavda verilecek formül kartı |
| `ornek_sorular.md` | Çözümlü örnek sorular |

## Komutlar
```bash
cd hafta15_proje
cp -r proje_sablonu ~/benim-projem && cd ~/benim-projem && git init
# Onarım tatbikatı (her dizin için):
cd onarim_tatbikati/sistem1 && python calistir.py     # hatayı bul, düzelt, nedenini yaz
cd ../sistem2 && docker compose up                     # (Docker gerektirir)
cd ../sistem3 && bash calistir.sh
cd ../sistem4 && python calistir.py
```

## Sunum düzeni
10 dakika sunum + 5 dakika soru; sıra: problem ve veri (2 dk) → ETL ve model (3 dk) → canlı demo (3 dk) → model
kartı/KVKK ve takım süreci (2 dk). Demo çalışmazsa kayıt (ekran videosu) kabul edilir; puan kesintisi yoktur
ancak sorular canlı sistem üzerinden sorulur.

## Teslim
Git deposu bağlantısı [Git deposu], son commit tarihi sunum gününden önce [Tarih, saat]; depo kökünde `README.md`,
`model_karti.md`, `Makefile` ve çalışan `make demo` hedefi zorunludur.
