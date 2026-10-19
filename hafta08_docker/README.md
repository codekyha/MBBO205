# Hafta 8 — Konteynerler: Docker temelleri

## Amaç
"Benim makinemde çalışıyor" sorununun çözümü: imaj, konteyner, katmanlar, hacim (volume), ağ.
Hafta 5 modelini bir imaja paketleyip çalıştırıyoruz. Bu haftanın çıktıları (imaj boyutu, derleme
süresi) makineye bağlıdır; ders notlarında temsilî olarak işaretlenmiştir.

## İçerik
| Dosya | Konu |
|---|---|
| `Dockerfile` | Çok aşamalı olmayan, `python:3.12-slim` tabanlı basit imaj |
| `Dockerfile.multistage` | Çok aşamalı (builder + runtime) imaj; boyut karşılaştırması için |
| `app.py` | Konteyner içinde çalışan tahmin betiği (model yoksa kendisi eğitir) |
| `.dockerignore` | İmaja girmeyecek dosyalar |
| `komutlar.sh` | Ders sırasında kullanılan Docker komutlarının sıralı listesi |

## Kurulum (Ubuntu)
```bash
sudo apt update && sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list >/dev/null
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo usermod -aG docker $USER && newgrp docker      # sudo'suz kullanım
docker run --rm hello-world                           # doğrulama
```

## Komutlar
```bash
cd hafta08_docker
docker build -t mbbo205/hafta08 .                 # imaj oluştur
docker run --rm mbbo205/hafta08                   # çalıştır (model eğitir, tahmin yapar)
docker run --rm -e N_ESTIMATORS=50 mbbo205/hafta08         # ortam değişkeni ile parametre
docker run --rm -v $(pwd)/cikti:/app/cikti mbbo205/hafta08  # modeli dışarı kaydet (hacim)
docker build -f Dockerfile.multistage -t mbbo205/hafta08-ms .
docker images | grep hafta08                      # boyut karşılaştır
docker run -it --rm mbbo205/hafta08 bash          # konteyner içine gir
docker ps -a; docker logs <id>; docker rm <id>; docker rmi mbbo205/hafta08
```

## Beklenen çıktı
`docker run` ekrana test AUC değerini ve `/app/cikti/model.pkl` yolunu yazar. Çok aşamalı imaj
tek aşamalıdan belirgin biçimde küçüktür (temsilî: ~%30–40 daha küçük).

## Lab 8 görevi
1. `Dockerfile` içinde `COPY` sırasını değiştirip katman önbelleğinin (cache) etkisini `docker build` sürelerinde gösterin.
2. `--memory=256m` sınırıyla konteyneri çalıştırın; `N_ESTIMATORS=2000` ile ne olur? (`docker inspect <id> | grep OOMKilled`)
3. İmajı `docker save` ile `.tar` olarak dışa aktarın ve boyutunu `docker images` ile karşılaştırın.

## Sorun giderme
- `permission denied ... docker.sock`: `sudo usermod -aG docker $USER` sonrası oturumu yeniden açın.
- `no space left on device`: `docker system prune -a`.
- Kurumsal ağda imaj çekilemiyorsa `/etc/docker/daemon.json` içine yansı (mirror) tanımlayın.
