# Hafta 12 — Yerel büyük dil modelleri: Ollama ve istem mühendisliği

## Amaç
Bulut API'sine bağımlı olmadan, veriyi dışarı çıkarmadan (KVKK) yerel LLM çalıştırma; Ollama REST
API'si; sıcaklık, bağlam penceresi ve sistem istemi; az-örnekli (few-shot), zincirleme düşünme ve
yapılandırılmış (JSON) çıktı istemleri; basit değerlendirme. Ollama çıktıları donanıma göre değişir;
notlarda temsilîdir.

## İçerik
| Dosya | Konu |
|---|---|
| `01_ollama_api.py` | `/api/generate` ve `/api/chat` çağrıları; akış (stream) ve parametreler; token/s ölçümü |
| `02_istem_muhendisligi.py` | Beş istem kalıbının aynı görevdeki çıktılarını karşılaştırır |
| `03_json_cikti.py` | Müşteri yorumlarından yapılandırılmış JSON çıkarma ve şema doğrulama |
| `istemler/` | Sistem ve görev istemleri (düzenlenebilir metin dosyaları) |
| `Modelfile` | Dersin özelleştirilmiş modeli (`mbbo205-asistan`) |

## Kurulum
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve &                      # servis (systemd kuruluysa otomatik)
ollama pull llama3.2:3b             # ~2 GB; 8 GB RAM yeterli
ollama pull qwen2.5:7b              # Türkçe daha iyi; 16 GB RAM önerilir
ollama list
ollama create mbbo205-asistan -f Modelfile
ollama run mbbo205-asistan "Bulut bilişimde IaaS ile PaaS farkı nedir?"
```

## Komutlar
```bash
cd hafta12_llm
python 01_ollama_api.py --model llama3.2:3b --sicaklik 0.2
python 02_istem_muhendisligi.py --model llama3.2:3b
python 03_json_cikti.py --model llama3.2:3b
OLLAMA_HOST=http://sunucu:11434 python 01_ollama_api.py     # uzak sunucu
```

## Beklenen çıktı
`01_ollama_api.py` üretim hızını (CPU'da tipik olarak 5–20 token/s, GPU'da 50+) yazar.
`03_json_cikti.py` üç yorumdan `{"duygu": ..., "konu": ..., "aciliyet": ...}` üretir ve şemaya göre geçerlilik raporu verir.

## Lab 12 görevi
1. Sıcaklığı 0, 0,7 ve 1,2 yapıp aynı istemde çıktıların değişkenliğini üç tekrarla ölçün.
2. `istemler/sistem.txt` dosyasını değiştirerek asistanın yalnızca Türkçe ve en fazla 3 cümleyle yanıt vermesini sağlayın.
3. `03_json_cikti.py` ile 20 yorum işleyin; geçersiz JSON oranını ve yeniden deneme stratejisini raporlayın.

## Sorun giderme
- `connection refused`: `ollama serve` çalışmıyor; `systemctl status ollama` veya elle başlatın.
- Model çok yavaşsa daha küçük model (`:1b`) veya `num_ctx` düşürün.
- Bellek hatası (`Killed` / `out of memory`): Hafta 13 `02_bellek.py` açıklaması.
