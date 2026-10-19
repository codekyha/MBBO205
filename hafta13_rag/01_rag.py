#!/usr/bin/env python3
"""Basit RAG: parçalama → geri getirme (TF-IDF veya Ollama gömme) → bağlamlı üretim."""
import argparse, glob, os, sys
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "hafta12_llm"))

# Ders notundaki METIN sözlüğü: belge adı -> içerik (belgeler/ dizininden yüklenir, yoksa gömülü örnek)
METIN: dict[str, str] = {}
for yol in sorted(glob.glob(os.path.join(os.path.dirname(__file__), "belgeler", "*.md"))):
    METIN[os.path.basename(yol)] = open(yol, encoding="utf-8").read()
if not METIN:
    METIN = {"ornek.md": "Ders 14 hafta sürer. Ara sınav %40, final %60 ağırlıklıdır."}

def parcala(metin: str, boyut: int = 400, ortusme: int = 80) -> list[str]:
    parcalar, i = [], 0
    while i < len(metin):
        parcalar.append(metin[i:i + boyut].strip()); i += boyut - ortusme
    return [p for p in parcalar if p]

def geri_getir(soru: str, parcalar: list[str], k: int, gomme: bool, model_gomme: str):
    if gomme:
        import requests
        from ollama_istemci import HOST
        def g(t): return requests.post(f"{HOST}/api/embeddings", json={"model": model_gomme, "prompt": t}, timeout=120).json()["embedding"]
        E = np.array([g(p) for p in parcalar]); q = np.array(g(soru))[None, :]
        skor = cosine_similarity(q, E)[0]
    else:
        vec = TfidfVectorizer(ngram_range=(1, 2), sublinear_tf=True).fit(parcalar + [soru])
        skor = cosine_similarity(vec.transform([soru]), vec.transform(parcalar))[0]
    sira = np.argsort(skor)[::-1][:k]
    return [(parcalar[i], float(skor[i])) for i in sira]

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--soru", required=True); ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--boyut", type=int, default=400); ap.add_argument("--gomme", action="store_true"); ap.add_argument("--model_gomme", default="nomic-embed-text")
    ap.add_argument("--model", default="llama3.2:3b"); a = ap.parse_args()
    parcalar, kaynak = [], []
    for ad, m in METIN.items():
        for p in parcala(m, a.boyut): parcalar.append(p); kaynak.append(ad)
    print(f"{len(METIN)} belge, {len(parcalar)} parça")
    sonuc = geri_getir(a.soru, parcalar, a.k, a.gomme, a.model_gomme)
    print(f"\n== En yakın {a.k} parça ==")
    for p, s in sonuc: print(f"[{s:.3f}] ({kaynak[parcalar.index(p)]}) {p[:120].replace(chr(10), ' ')}...")
    baglam = "\n\n".join(p for p, _ in sonuc)
    istem = f"Yalnızca aşağıdaki bağlama dayanarak Türkçe yanıt ver; bağlamda yoksa 'Belgelerde bulunamadı' de.\n\nBAĞLAM:\n{baglam}\n\nSORU: {a.soru}\nYANIT:"
    try:
        from ollama_istemci import hazir, uret
        if hazir():
            y, m = uret(a.model, istem, sicaklik=0.0); print(f"\n== Yanıt ({a.model}) ==\n{y.strip()}")
        else:
            print("\n(Ollama erişilemedi; yalnızca geri getirme gösterildi. İstem uzunluğu:", len(istem), "karakter)")
    except Exception as e:
        print("\n(üretim atlandı:", e, ")")
