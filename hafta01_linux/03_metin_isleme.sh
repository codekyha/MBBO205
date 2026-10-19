#!/usr/bin/env bash
# grep / awk / sed / sort / uniq ile log analizi
set -eu
cd "$(dirname "$0")"
LOG=veri/sunucu.log
echo "=== Toplam satır ==="; wc -l < "$LOG"
echo "=== Durum kodu dağılımı ==="; awk '{print $6}' "$LOG" | sort | uniq -c | sort -rn
echo "=== En çok istek alan 5 uç nokta ==="; awk '{print $5}' "$LOG" | sort | uniq -c | sort -rn | head -5
echo "=== 5xx hataları ==="; grep -E ' 5[0-9]{2} ' "$LOG" | head -3
echo "=== Ortalama yanıt süresi (ms) ==="; awk '{s+=$7; n++} END{printf "%.1f\n", s/n}' "$LOG"
echo "=== IP maskeleme (sed) ==="; sed -E 's/([0-9]+\.[0-9]+\.[0-9]+)\.[0-9]+/\1.xxx/' "$LOG" | head -3
mkdir -p cikti
awk '$6>=500' "$LOG" > cikti/hatalar.log
echo "5xx satırları cikti/hatalar.log dosyasına yazıldı ($(wc -l < cikti/hatalar.log) satır)"
