#!/usr/bin/env bash
# Günlükteki 5xx hatalarını sayıp rapor.txt dosyasına yazması bekleniyor
LOG = sunucu.log
grep -E " 5[0-9]{2} " $LOG | wc -l > rapor.txt
echo "rapor yazıldı: $(cat rapor.txt) hata"
