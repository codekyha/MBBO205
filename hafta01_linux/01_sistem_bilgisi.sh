#!/usr/bin/env bash
# Sistem bilgisi özeti
set -euo pipefail
echo "=== Dağıtım ==="; (cat /etc/os-release 2>/dev/null | grep PRETTY_NAME) || uname -a
echo "=== Çekirdek ==="; uname -r
echo "=== CPU ==="; nproc; (grep -m1 "model name" /proc/cpuinfo || true)
echo "=== Bellek (MB) ==="; free -m | awk 'NR==2{printf "toplam=%s kullanılan=%s boş=%s\n",$2,$3,$4}'
echo "=== Disk ==="; df -h / | tail -1
echo "=== Kullanıcı / dizin ==="; whoami; pwd
echo "=== GPU (varsa) ==="; (command -v nvidia-smi >/dev/null && nvidia-smi --query-gpu=name,memory.total --format=csv) || echo "GPU yok veya nvidia-smi kurulu değil"
