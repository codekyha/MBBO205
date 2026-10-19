# Hafta 1 — Linux ve kabuk temelleri

## Amaç
Dersin tüm uygulamaları Linux kabuğunda yürür. Bu hafta dosya sistemi, izinler, metin işleme boru hatları
ve süreç izleme komutlarını, yapay zekâ iş yüklerinin ihtiyaç duyduğu bağlamda (veri dosyaları, log
inceleme, bellek/CPU takibi) öğreniyoruz.

## İçerik
| Betik | Konu |
|---|---|
| `01_sistem_bilgisi.sh` | Çekirdek, CPU, bellek, disk, dağıtım bilgisi |
| `02_dosya_islemleri.sh` | Dizin ağacı oluşturma, kopyalama, izinler (`chmod`), sembolik bağ |
| `03_metin_isleme.sh` | `grep`, `awk`, `sed`, `sort`, `uniq`, `cut` ile log analizi |
| `04_surec_izleme.sh` | `ps`, `top -b`, `free`, `df`, `nohup`, arka plan süreçleri |
| `veri/sunucu.log` | Örnek sunucu günlüğü (lab için) |

## Komutlar
```bash
cd hafta01_linux
chmod +x *.sh                 # çalıştırma izni (bir kez)
./01_sistem_bilgisi.sh
./02_dosya_islemleri.sh
./03_metin_isleme.sh
./04_surec_izleme.sh
```
Tüm betikler kökten `make hafta01` ile de çalışır.

## Beklenen çıktı
`03_metin_isleme.sh` örnek günlükten HTTP durum kodu dağılımını ve en çok istek alan 5 uç noktayı
listeler; `04_surec_izleme.sh` toplam/kullanılabilir belleği MB cinsinden yazar.

## Lab 1 görevi (teslim: `lab01_cevap.txt`)
1. `veri/sunucu.log` içinde 5xx hatası üreten benzersiz IP adreslerini sayın.
2. Saat 14:00–15:00 arasındaki istekleri `awk` ile süzün ve dosyaya yazın.
3. Sisteminizin toplam RAM'ini ve boş disk alanını tek satırlık bir komutla yazdırın.
Her madde için kullandığınız komutu ve çıktının ilk 3 satırını cevap dosyasına ekleyin.

## Sorun giderme
- `Permission denied`: `chmod +x betik.sh` veya `bash betik.sh`.
- `free`/`top` yoksa (`procps` eksik): `sudo apt install procps`.
- WSL kullanıyorsanız `/mnt/c` altında değil, `~` altında çalışın; dosya izinleri orada doğru davranır.
