#!/usr/bin/env bash
# Hafta 8 ders akışı — adım adım çalıştırın (set -x komutları ekrana yazar)
set -ex
docker --version
docker build -t mbbo205/hafta08 .
docker run --rm mbbo205/hafta08
docker run --rm -e N_ESTIMATORS=50 mbbo205/hafta08
mkdir -p cikti && docker run --rm -v "$(pwd)/cikti:/app/cikti" mbbo205/hafta08 && ls -l cikti
docker build -f Dockerfile.multistage -t mbbo205/hafta08-ms .
docker images | grep hafta08
docker history mbbo205/hafta08 | head
