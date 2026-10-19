# [Proje adı]

Takım: [isimler] · MBBO205 2026–2027 Güz · Depo: [URL]

## Problem
[Bir paragraf: iş problemi, hedef metrik, başarı ölçütü]

## Çalıştırma
```bash
make kur      # ortam
make veri     # veri indir/üret
make etl      # temizle -> veri/temiz.csv
make egit     # model -> model/
make demo     # servis + örnek istek
make test     # testler
```

## Dizinler
`veri/` ham ve temiz veri (büyük dosyalar Git'e girmez) · `etl/` · `model/` · `servis/` (FastAPI + Dockerfile) ·
`rapor/` (model kartı, kalite raporu, sunum) · `tests/`

## Model kartı
Bkz. `rapor/model_karti.md`
