#!/usr/bin/env python3
"""LLM'den yapılandırılmış JSON çıkarma ve doğrulama."""
import argparse, json, sys
from ollama_istemci import hazir, uret, HOST
ap = argparse.ArgumentParser(); ap.add_argument("--model", default="llama3.2:3b"); ap.add_argument("--deneme", type=int, default=2); a = ap.parse_args()
if not hazir(): sys.exit(f"Ollama erişilemiyor ({HOST}).")
sablon = open("istemler/gorev_json.txt", encoding="utf-8").read()
yorumlar = ["Uygulama her açılışta çöküyor, acil çözüm lazım!", "Fiyat biraz yüksek ama kalite tatmin edici.", "Kargo üç gün gecikti, paket sağlamdı."]
def gecerli(j: dict) -> list[str]:
    h = []
    if j.get("duygu") not in {"olumlu", "olumsuz", "notr"}: h.append("duygu")
    if j.get("konu") not in {"teknik", "fiyat", "destek", "teslimat", "diger"}: h.append("konu")
    if not (isinstance(j.get("aciliyet"), int) and 1 <= j["aciliyet"] <= 5): h.append("aciliyet")
    if not isinstance(j.get("ozet"), str) or len(j["ozet"].split()) > 12: h.append("ozet")
    return h
sonuc = []
for y in yorumlar:
    for deneme in range(1, a.deneme + 1):
        ham, _ = uret(a.model, sablon.format(metin=y), sicaklik=0.0, json_mod=True)
        try:
            j = json.loads(ham); hatalar = gecerli(j)
        except json.JSONDecodeError:
            j, hatalar = None, ["json"]
        if not hatalar: break
        print(f"  deneme {deneme} geçersiz ({', '.join(hatalar)}): {ham[:80]!r}")
    sonuc.append({"yorum": y, "cikti": j, "hatalar": hatalar})
    print(f"{y}\n  -> {j}  {'OK' if not hatalar else 'HATALI: ' + ', '.join(hatalar)}")
print(f"\ngeçerli: {sum(not s['hatalar'] for s in sonuc)}/{len(sonuc)}")
json.dump(sonuc, open("cikti_json.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
