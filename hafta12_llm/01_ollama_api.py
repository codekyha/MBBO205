#!/usr/bin/env python3
"""Ollama API temel kullanım ve hız ölçümü."""
import argparse, sys
from ollama_istemci import hazir, uret, sohbet, HOST
ap = argparse.ArgumentParser(); ap.add_argument("--model", default="llama3.2:3b"); ap.add_argument("--sicaklik", type=float, default=0.2); a = ap.parse_args()
if not hazir(): sys.exit(f"Ollama erişilemiyor ({HOST}). `ollama serve` çalışıyor mu?")
sistem = open("istemler/sistem.txt", encoding="utf-8").read()
print("== Tek seferlik üretim =="); yanit, m = uret(a.model, "Bulut bilişimde IaaS, PaaS ve SaaS farkını üç maddede açıkla.", sistem, a.sicaklik)
print(yanit); print(f"-- {m['token']} token, {m['token_s']:.1f} token/s, {m['sure']:.1f} s")
print("\n== Akışlı üretim =="); uret(a.model, "Docker imajı ile konteyner arasındaki fark nedir? İki cümle.", sistem, a.sicaklik, akis=True)
print("\n== Çok turlu sohbet ==")
mesajlar = [{"role": "system", "content": sistem}, {"role": "user", "content": "k-means algoritmasını tek cümlede anlat."}]
c1 = sohbet(a.model, mesajlar, a.sicaklik); print("asistan:", c1)
mesajlar += [{"role": "assistant", "content": c1}, {"role": "user", "content": "Peki k nasıl seçilir?"}]
print("asistan:", sohbet(a.model, mesajlar, a.sicaklik))
