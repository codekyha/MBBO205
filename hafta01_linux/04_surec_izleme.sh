#!/usr/bin/env bash
# Süreç ve kaynak izleme
set -eu
echo "=== En çok bellek kullanan 5 süreç ==="; ps aux --sort=-%mem | head -6
echo "=== Yük ortalaması ==="; cat /proc/loadavg
echo "=== Bellek (MB) ==="; free -m | awk 'NR==2{print "toplam:",$2," kullanılabilir:",$7}'
echo "=== Arka plan süreç örneği ==="
mkdir -p "$(dirname "$0")/cikti"
nohup bash -c 'for i in 1 2 3; do echo "adım $i"; sleep 1; done' > "$(dirname "$0")/cikti/arka_plan.log" 2>&1 &
PID=$!
echo "başlatıldı PID=$PID"; wait $PID
echo "bitti; çıktı:"; cat "$(dirname "$0")/cikti/arka_plan.log"
