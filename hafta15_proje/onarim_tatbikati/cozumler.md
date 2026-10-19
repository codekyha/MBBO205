# Çözümler (eğitmen)

1. **sistem1** — Türkçe sayı biçimi (`1.250,50`) `to_numeric` ile NaN olur; `sum()` NaN'ları atlar, çıktı yanıltıcı. Düzeltme:
   `pd.read_csv(..., sep=";", thousands=".", decimal=",")`. Önleme: Hafta 3 kalite raporu (eksik % > 0 uyarısı).
2. **sistem2** — Port eşlemesi `8080:80` ama sunucu 8000 dinliyor; `8080:8000` olmalı. Önleme: `docker compose logs`, sağlık kontrolü.
3. **sistem3** — `LOG = sunucu.log` bash'te atama değil komut çağrısıdır (boşluk); `$LOG` boş kalır, `grep` stdin bekler/boş döner.
   `LOG=sunucu.log` olmalı; ayrıca `set -euo pipefail` tanımsız değişkeni erken yakalardı.
4. **sistem4** — Eğitimde `StandardScaler` kullanıldı, üretimde ham veri verildi (train/serve skew). `m.predict_proba(sc.transform(Xy))` veya
   `Pipeline` kullanımı. Önleme: Hafta 9'daki gibi ölçekleyiciyi modelle birlikte kaydetmek, Hafta 14 şema testi.
