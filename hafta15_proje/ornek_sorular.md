# Çözümlü örnek sorular

**B1.** Test kümesinde TP=80, FP=40, FN=20, TN=860. Kesinlik, duyarlılık ve $F_1$ hesaplayın.
*Çözüm:* $P=80/120=0{,}667$; $R=80/100=0{,}80$; $F_1=2(0{,}667)(0{,}80)/(1{,}467)=0{,}727$.

**B2.** 7 milyar parametreli bir modelin fp16 ve 4-bit nicemlenmiş ağırlık boyutunu hesaplayın; 16 GB RAM'li
makinede hangisi çalışır?
*Çözüm:* fp16: $7\times10^9\times2=14$ GB (işletim sistemi ve bağlamla sığmaz); Q4: $7\times10^9\times0{,}5=3{,}5$ GB (çalışır).

**B3.** Referans dağılımda bir kutuda pay 0,10, yeni veride 0,25 ise bu kutunun PSI katkısı nedir?
*Çözüm:* $(0{,}25-0{,}10)\ln(2{,}5)=0{,}15\times0{,}916=0{,}137$.

**B4.** Günde 50 000 istek, istek başına 100 ms ve 512 MB bellek; sunucusuz birim fiyat 0,20 USD/milyon çağrı ve
$1{,}67\times10^{-5}$ USD/GB-s. Aylık maliyet? VM 0,04 USD/saat ile karşılaştırın.
*Çözüm:* çağrı: $1{,}5\times10^6/10^6\times0{,}20=0{,}30$; hesap: $1{,}5\times10^6\times0{,}1\times0{,}5\times1{,}67\times10^{-5}=1{,}25$; toplam $\approx1{,}55$ USD. VM: $0{,}04\times730=29{,}2$ USD. Bu hacimde sunucusuz çok daha ucuz; kesişme $\approx 10^6$ istek/gün civarında.

**C1.** Bir eğitim betiği ekrana yalnızca `Killed` yazıp çıktı; `dmesg` çıktısında `Out of memory: Killed process 4321 (python)` var. Ne oldu, üç çözüm önerin.
*Çözüm:* Çekirdek OOM-killer süreci SIGKILL ile sonlandırdı; Python istisna üretemedi. Çözümler: parti/parça boyutunu küçültme, float32→float16 veya `np.memmap`, swap ekleme/daha büyük makine; Docker'da `--memory` sınırını kontrol etme.

**C2.** `docker compose ps` çıktısında `api` servisi `Restarting (1)` döngüsünde. İlk üç komutunuz?
*Çözüm:* `docker compose logs api` (hata mesajı), `docker compose config` (compose doğrulama), `docker run -it --rm <imaj> bash` ile elle başlatıp hatayı yeniden üretme.

**D1.** Bir belediye, su sayacı verisinden kaçak tüketimi tahmin eden sistem istiyor. Veri kişisel, sunucular Türkiye'de olmalı,
günlük 20 000 tahmin yapılacak. Uçtan uca tasarım yapın.
*Çözüm (ana başlıklar):* veri: anonimleştirilmiş abone no, tüketim serileri, şema doğrulama (H3); model: temel kural + gradyan artırma,
CV ve maliyete dayalı eşik (H5–6); dağıtım: FastAPI + Docker Compose, yerel/Türkiye bölgesi, nesne depolama (H9–10); izleme: PSI ve tahmin oranı uyarısı,
yeniden eğitim tetikleyicisi (H14); KVKK: yurt içi işleme, model kartı, insan onayı olmadan yaptırım yok (H14); açıklanabilirlik: özellik önemleri (H5).
