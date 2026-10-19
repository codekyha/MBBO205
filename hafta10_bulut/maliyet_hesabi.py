#!/usr/bin/env python3
"""Basit toplam sahip olma maliyeti (TCO) karşılaştırması. Fiyatlar temsilîdir; güncel listeyi sağlayıcıdan alın."""
import argparse
ap = argparse.ArgumentParser(); ap.add_argument("--istek_gun", type=int, default=20000); ap.add_argument("--ay", type=int, default=12)
ap.add_argument("--ms_istek", type=float, default=50, help="istek başına işlem süresi (ms)")
a = ap.parse_args()
istek_ay = a.istek_gun * 30
vm_saat = 0.04          # 2 vCPU / 4 GB sanal makine, USD/saat (temsilî)
sunucusuz_milyon = 0.20 # milyon çağrı başına (temsilî)
sunucusuz_gb_s = 0.0000166667  # GB-saniye başına (temsilî)
yerel_sunucu = 1500     # tek seferlik donanım USD; 36 ay amortisman
elektrik_ay = 15
vm = vm_saat * 24 * 30 * a.ay
sl = (istek_ay / 1e6 * sunucusuz_milyon + istek_ay * (a.ms_istek / 1000) * 0.5 * sunucusuz_gb_s) * a.ay
yerel = yerel_sunucu / 36 * a.ay + elektrik_ay * a.ay
print(f"{a.ay} ay, günde {a.istek_gun:,} istek, {a.ms_istek} ms/istek")
for ad, m in [("Sanal makine (IaaS, 7/24)", vm), ("Sunucusuz (FaaS)", sl), ("Yerel sunucu (amortisman+elektrik)", yerel)]:
    print(f"  {ad:38s} ≈ {m:8.0f} USD")
print("Not: sunucusuz maliyeti istek hacmiyle doğrusal artar; VM sabittir. Kesişme noktasını --istek_gun ile arayın.")
