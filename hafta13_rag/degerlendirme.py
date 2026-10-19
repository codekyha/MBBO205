#!/usr/bin/env python3
"""Geri getirme isabeti: her soru için doğru belge ilk k içinde mi?"""
import argparse, importlib.util, os
spec = importlib.util.spec_from_file_location("rag", os.path.join(os.path.dirname(__file__), "01_rag.py")); rag = importlib.util.module_from_spec(spec); spec.loader.exec_module(rag)
ap = argparse.ArgumentParser(); ap.add_argument("--k", type=int, default=3); ap.add_argument("--boyut", type=int, default=400); a = ap.parse_args()
sorular = [("Ara sınavın ağırlığı nedir?", "ders_bilgi.md"), ("Final kaç dakika?", "ders_bilgi.md"), ("Git kullanımı kaç puan?", "proje_rubrigi.md"),
           ("Sunum süresi ne kadar?", "proje_rubrigi.md"), ("Yurt dışı aktarım için ne gerekir?", "kvkk_notu.md"), ("Model kartında ne olmalı?", "kvkk_notu.md")]
parcalar, kaynak = [], []
for ad, m in rag.METIN.items():
    for p in rag.parcala(m, a.boyut): parcalar.append(p); kaynak.append(ad)
isabet = 0
for soru, dogru in sorular:
    sonuc = rag.geri_getir(soru, parcalar, a.k, False, ""); bulunan = [kaynak[parcalar.index(p)] for p, _ in sonuc]
    ok = dogru in bulunan; isabet += ok; print(f"{'OK ' if ok else 'YOK'} {soru:40s} -> {bulunan[0]}")
print(f"\nhit@{a.k}: {isabet}/{len(sorular)} = {isabet/len(sorular):.2f}  (parça boyutu {a.boyut})")
