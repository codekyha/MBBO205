# Proje teslimi KVKK / etik kontrol listesi

- [ ] Veri kümesinde doğrudan kimlik (ad, TC kimlik no, telefon, e-posta) yok veya geri döndürülemez biçimde anonimleştirilmiş.
- [ ] Gerçek kişilerden veri toplandıysa aydınlatma metni ve açık rıza kaydı mevcut.
- [ ] Veri, Türkiye dışındaki bir bulut hizmetine aktarıldıysa hukuki dayanak raporda belirtilmiş; aksi hâlde yerel işleme (Ollama/MinIO) tercih edilmiş.
- [ ] Hassas kategoriler (sağlık, din, etnik köken vb.) model girdisi olarak kullanılmıyor; vekil değişkenler tartışılmış.
- [ ] Model kartı dolduruldu; kapsam dışı kullanımlar yazıldı.
- [ ] Alt gruplar arası performans farkı ölçüldü ve raporlandı.
- [ ] Git deposunda `.env`, anahtar, parola, kişisel veri dosyası yok (`git log -p | grep -i parola` ile kontrol).
- [ ] Demo verisi sentetik veya anonim; sunumda gerçek kişi görünmüyor.
