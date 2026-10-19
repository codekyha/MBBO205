# Ara sınav hazırlığı (Hafta 1–7)

Ağırlık: ara sınav %40 (önerilen: %70 yazılı + %30 Lab 1–7).

## Konu listesi
1. Linux: dosya sistemi, izinler, boru hatları (`grep | awk | sort | uniq`), süreç/bellek izleme.
2. Python: sanal ortam, veri yapıları, NumPy yayın kuralları, pandas süzme/gruplama.
3. ETL: eksik/uç değer stratejileri, tip dönüşümü, şema doğrulama, veri kalitesi ölçütleri.
4. EDA: betimsel istatistik, korelasyon, dağılım biçimleri, sınıf dengesi.
5. Denetimli öğrenme: eğitim/test ayrımı, ölçekleme, lojistik regresyon, ağaç toplulukları, metrikler.
6. Değerlendirme: k-katlı CV, aşırı/eksik öğrenme, hiperparametre arama, ROC/eşik seçimi.
7. Denetimsiz: k-means ve $k$ seçimi, silüet, PCA ve açıklanan varyans.

## Örnek sorular
- `awk '$6>=500 {print $3}' sunucu.log | sort -u | wc -l` komutu ne hesaplar?
- 100 pozitif, 900 negatif örnekli bir veri kümesinde her şeyi negatif tahmin eden modelin doğruluğu,
  kesinliği ve duyarlılığı nedir? Hangi metrik bu modeli ele verir?
- $k$-katlı çapraz doğrulamada $k$ artınca sapma ve varyans nasıl değişir?
- Silüet skoru $s=(b-a)/\max(a,b)$ formülünde $a$ ve $b$ nedir; $s\to 1$ ve $s\to -1$ ne anlama gelir?
- PCA'da ilk iki bileşen varyansın %60'ını açıklıyorsa 5 boyutlu veriyi 2 boyuta indirgemek hangi
  durumda kabul edilebilir?

## Komut özeti (sınavda sorulabilir)
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python betik.py --parametre deger
free -m | awk 'NR==2{print $7}'
df -h /
ps aux --sort=-%mem | head
```
