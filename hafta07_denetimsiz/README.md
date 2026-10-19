# Hafta 7 — Denetimsiz öğrenme ve ara sınav hazırlığı

## Amaç
Etiketsiz veriden yapı çıkarma: k-ortalamalar ile müşteri bölütleme (dirsek ve silüet ile $k$ seçimi),
PCA ile boyut indirgeme ve görselleştirme. Haftanın ikinci bölümü ara sınav (Lab 1–7) tekrarıdır.

## İçerik
| Dosya | Konu |
|---|---|
| `01_kmeans.py` | Ölçekleme → k-means; dirsek (inertia) ve silüet grafiği; küme profilleri |
| `02_pca.py` | PCA; açıklanan varyans; 2B izdüşüm (küme renkli) |
| `ara_sinav_hazirlik.md` | Konu listesi, örnek sorular ve komut özeti |

## Komutlar
```bash
cd hafta07_denetimsiz
python 01_kmeans.py --kmax 8
python 02_pca.py
```

## Beklenen çıktı
Silüet skoru genelde küçük $k$ (2–4) değerlerinde en yüksek; dirsek ve silüet farklı $k$ önerebilir, bu tartışma ödevin parçasıdır. Küme profilleri segment yapısıyla
(Bireysel/KOBI/Kurumsal) kısmen örtüşür. PCA'da ilk iki bileşen varyansın ~%55–65'ini açıklar.

## Lab 7 görevi
1. `kidem_ay` ve `aylik_islem` ile yalnız iki özellikli k-means çalıştırıp kümeleri yorumlayın.
2. PCA bileşen yüklerini (loadings) yazdırın; ilk bileşen hangi özelliklerin birleşimi?
3. Küme etiketini Hafta 5 sınıflandırıcısına özellik olarak ekleyin; AUC değişti mi?
