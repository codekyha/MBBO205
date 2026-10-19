#!/usr/bin/env bash
# Dizin ağacı, izinler ve sembolik bağ
set -euo pipefail
cd "$(dirname "$0")"
rm -rf cikti && mkdir -p cikti/proje/{veri,model,log}
echo "ham veri" > cikti/proje/veri/ham.csv
cp cikti/proje/veri/ham.csv cikti/proje/veri/yedek.csv
ln -sf ../veri/ham.csv cikti/proje/model/girdi.csv
chmod 640 cikti/proje/veri/ham.csv        # sahip rw, grup r, diğer -
chmod 750 cikti/proje/model
echo "=== Ağaç ==="; find cikti -print | sed 's|[^/]*/|  |g'
echo "=== İzinler ==="; ls -l cikti/proje/veri cikti/proje/model
echo "=== Bağ hedefi ==="; readlink -f cikti/proje/model/girdi.csv
echo "=== Boyut ==="; du -sh cikti
