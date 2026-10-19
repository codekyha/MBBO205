#!/usr/bin/env python3
"""Hugging Face boru hatları: Türkçe duygu analizi ve sıfır-atış sınıflandırma."""
import sys
try:
    from transformers import pipeline
except ImportError:
    sys.exit("transformers kurulu değil: pip install -r requirements.txt")
cumleler = ["Servis çok hızlı ve destek ekibi ilgiliydi.", "Uygulama sürekli çöküyor, iade istiyorum.", "Fiyatlar makul ama kurulum uzun sürdü."]
try:
    duygu = pipeline("sentiment-analysis", model="savasy/bert-base-turkish-sentiment-cased")
    print("== Duygu analizi ==")
    for c, s in zip(cumleler, duygu(cumleler)):
        print(f"  {s['label']:9s} {s['score']:.3f}  {c}")
    sifir = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
    print("== Sıfır-atış sınıflandırma ==")
    for c in cumleler:
        r = sifir(c, candidate_labels=["teknik sorun", "fiyat", "müşteri hizmetleri"])
        print(f"  {r['labels'][0]:18s} {r['scores'][0]:.3f}  {c}")
except Exception as e:
    print(f"Model indirilemedi ({type(e).__name__}: {e}).\nİnternet bağlantısı veya önbellek gerekir: huggingface-cli download savasy/bert-base-turkish-sentiment-cased")
