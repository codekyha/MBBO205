# Model kartı — [Model adı] v[sürüm]

## 1. Model ayrıntıları
- Geliştiren: [takım üyeleri], MBBO205, [tarih]
- Model türü: [ör. RandomForestClassifier, 300 ağaç]
- Girdi özellikleri: [liste] · Çıktı: [ör. müşteri kaybı olasılığı]
- Sürüm ve depo: [Git deposu], etiket `v[sürüm]`, meta sağlaması `[meta.json veri_sha256]`

## 2. Amaçlanan kullanım
- Birincil kullanım: [ör. kampanya önceliklendirme]
- Kullanıcılar: [kim]
- Kapsam dışı kullanım: [ör. kredi kararı, bireysel yaptırım]

## 3. Veri
- Kaynak, toplama tarihi, boyut: [...]
- Ön işleme: [Hafta 3 ETL adımları]
- Bilinen eksiklikler / temsil sorunları: [ör. Antalya örneklemi az]

## 4. Değerlendirme
| Metrik | Test | Not |
|---|---|---|
| ROC-AUC | [...] | 5-katlı CV: [...] ± [...] |
| F1 (eşik [...]) | [...] | eşik maliyet analizine göre seçildi |
- Alt gruplara göre performans (şehir/segment): [tablo] — belirgin fark varsa açıklayın.

## 5. Etik ve KVKK
- Kişisel veri: [var/yok]; hukuki dayanak: [açık rıza / anonimleştirme]
- Yurt dışına aktarım: [yok / 6698 md. 9 kapsamında değerlendirildi]
- Yanlılık riski: [hangi özellikler vekil (proxy) olabilir] ve alınan önlem
- İnsan gözetimi: [kararların nasıl denetlendiği]

## 6. Sınırlılıklar ve bakım
- Veri kayması izleme: PSI eşiği [...], yeniden eğitim tetikleyicisi [...]
- Bilinen başarısızlık durumları: [...]
