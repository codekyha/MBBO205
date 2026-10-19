# Hafta 4 — Keşifsel veri analizi (EDA) ve görselleştirme

## Amaç
Modellemeden önce veriyi anlamak: dağılımlar, korelasyonlar, sınıf dengesi, kategori etkileri.
Çıktılar `cikti/` altına PNG ve Markdown olarak yazılır; sunucuda (başsız) da çalışır.

## İçerik
| Dosya | Konu |
|---|---|
| `01_ozet.py` | Betimsel istatistik, korelasyon matrisi, hedef oranları (Markdown rapor) |
| `02_gorsel.py` | Histogram, kutu grafiği, dağılım grafiği, korelasyon ısı haritası (PNG) |

## Komutlar
```bash
cd hafta04_eda
python 01_ozet.py             # cikti/eda_ozet.md
python 02_gorsel.py           # cikti/*.png
ls cikti/
```

## Beklenen çıktı
Dört PNG: `hist_gelir.png`, `kutu_harcama_segment.png`, `dagilim_gelir_harcama.png`,
`korelasyon.png`; raporda `harcama`–`gelir` korelasyonunun pozitif ve `ayrildi`–`kidem_ay`
korelasyonunun negatif olduğu görülmelidir.

## Lab 4 görevi
1. `ayrildi` oranını şehir ve segment kırılımında çubuk grafik olarak çizin.
2. `gelir` için log dönüşümü uygulayıp histogramı karşılaştırın; hangisi daha simetrik, neden?
3. Bir bulgu seçip tek paragraf yorum yazın (`cikti/yorum.md`).

## Sorun giderme
- `matplotlib` görüntü penceresi açmaya çalışıyorsa betik zaten `Agg` arka ucunu seçer; yine de
  sorun olursa `MPLBACKEND=Agg python 02_gorsel.py`.
