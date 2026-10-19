# Hafta 13 — RAG (geri getirme destekli üretim) ve bellek yönetimi

## Amaç
LLM'in bilmediği kurum içi belgeleri, modeli yeniden eğitmeden yanıtlara katmak: parçalama (chunking),
gömme (embedding) veya TF-IDF ile geri getirme, bağlam oluşturma ve üretim. İkinci bölüm, yapay zekâ iş
yüklerinde en sık görülen üretim hatası olan bellek tükenmesini (`Killed`, OOM) ve çarelerini inceler.

## İçerik
| Dosya | Konu |
|---|---|
| `01_rag.py` | `METIN` sözlüğündeki ders belgeleri → parçalama → TF-IDF (varsayılan) veya Ollama gömme → kosinüs benzerliği → bağlamlı istem. Ollama yoksa yalnızca geri getirme sonuçlarını gösterir. |
| `02_bellek.py` | Bellek kullanımını adım adım ölçer; `--sinir` ile sanal sınır koyup OOM davranışını güvenli biçimde canlandırır; parça parça (chunked) işleme ile çözüm |
| `belgeler/` | Örnek kurum içi belgeler (`.md`); `METIN` sözlüğü buradan da yüklenebilir |
| `degerlendirme.py` | Basit RAG değerlendirmesi: soru–cevap çiftlerinde geri getirme isabeti (hit@k) |

## Komutlar
```bash
cd hafta13_rag
python 01_rag.py --soru "Ara sınavın ağırlığı nedir?"            # TF-IDF geri getirme
python 01_rag.py --soru "Proje rubriğinde Git kaç puan?" --gomme   # Ollama gömme (ollama pull nomic-embed-text)
python 01_rag.py --soru "KVKK açısından nelere dikkat edilmeli?" --model llama3.2:3b
python degerlendirme.py --k 3
python 02_bellek.py                      # kademeli bellek ölçümü
python 02_bellek.py --sinir_mb 300       # yapay sınır: OOM'u güvenli canlandır
python 02_bellek.py --parcali            # çözüm: parçalı işleme
```

## Beklenen çıktı
`01_rag.py` en yakın 3 parçayı benzerlik skoruyla listeler ve (Ollama varsa) bağlamlı yanıt üretir.
`02_bellek.py` matris boyutu ile RSS belleği tablosunu yazar; `--sinir_mb` ile sınır aşıldığında
betik gerçek bir OOM yerine `MemoryError` fırlatır ve kernel'in `Killed` mesajının nedenini açıklar.
`--parcali` aynı işi sabit bellekle tamamlar.

## Lab 13 görevi
1. `belgeler/` içine kendi ders notunuzdan bir sayfa ekleyin; üç soru yazıp hit@3 ölçün.
2. Parça boyutunu 200, 500 ve 1000 karakter yapıp isabeti karşılaştırın.
3. `dmesg | grep -i "out of memory"` ile gerçek bir OOM kaydının nasıl göründüğünü (varsa) raporlayın; `ulimit -v` ile sanal bellek sınırı koyup Hafta 11 MLP'sini çalıştırın.

## Sorun giderme
- `Killed` yazıp çıkan betik: çekirdek OOM-killer; `free -m`, `dmesg`, parti boyutu küçültme, `swap` ekleme.
- `nomic-embed-text` yoksa `--gomme` olmadan çalıştırın; TF-IDF yerel ve yeterlidir.
