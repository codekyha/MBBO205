#!/usr/bin/env python3
"""Aynı görev için beş istem kalıbı."""
import argparse, sys
from ollama_istemci import hazir, uret, HOST
ap = argparse.ArgumentParser(); ap.add_argument("--model", default="llama3.2:3b"); a = ap.parse_args()
if not hazir(): sys.exit(f"Ollama erişilemiyor ({HOST}).")
yorum = "Ürün iki hafta geç geldi, kutu ezikti ama cihaz sorunsuz çalışıyor; destek hattı ilgilendi."
kaliplar = {
  "1 Doğrudan": f"Bu yorumun duygusu nedir? {yorum}",
  "2 Rol + biçim": f"Sen bir müşteri deneyimi analistisin. Yorumu 'olumlu/olumsuz/karışık' olarak etiketle ve tek cümle gerekçe ver.\nYorum: {yorum}",
  "3 Az-örnekli": "Yorum: Kargo hızlıydı, teşekkürler. -> olumlu\nYorum: Ürün bozuk geldi, kimse aramadı. -> olumsuz\nYorum: Fiyat iyi ama paket kötüydü. -> karışık\n" + f"Yorum: {yorum} ->",
  "4 Adım adım": f"Yorumu analiz et: önce olumlu ifadeleri, sonra olumsuz ifadeleri listele, en sonunda genel duyguyu tek kelimeyle ver.\nYorum: {yorum}",
  "5 Kısıtlı": f"Yalnızca şu üç kelimeden birini yaz, başka hiçbir şey yazma: olumlu, olumsuz, karışık.\nYorum: {yorum}",
}
for ad, istem in kaliplar.items():
    y, m = uret(a.model, istem, sicaklik=0.1)
    print(f"\n=== {ad} === ({m['token']} token)\n{y.strip()}")
