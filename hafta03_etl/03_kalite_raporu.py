#!/usr/bin/env python3
"""Şemaya göre veri kalitesi raporu üretir."""
import os, sys
import pandas as pd, yaml

YOL = sys.argv[1] if len(sys.argv) > 1 else "cikti/temiz_musteri.csv"
TIP = {"int": "integer", "float": "floating", "str": "string"}

def rapor(df: pd.DataFrame, sema: dict) -> list[str]:
    s = ["# Veri kalitesi raporu", f"Dosya: `{YOL}`  Satır: {len(df)}  Sütun: {df.shape[1]}", "",
         "| Sütun | Eksik % | Benzersiz | İhlal | Not |", "|---|---|---|---|---|"]
    toplam_ihlal = 0
    for ad, k in sema.items():
        if ad not in df.columns:
            s.append(f"| {ad} | - | - | 1 | sütun yok |"); toplam_ihlal += 1; continue
        col = df[ad]; ihlal = 0; notlar = []
        tur = pd.api.types.infer_dtype(col.dropna())
        if TIP[k["tip"]] not in tur: ihlal += 1; notlar.append(f"tip {tur}")
        if "min" in k: n = int((col < k["min"]).sum()); ihlal += n; notlar += [f"<min {n}"] if n else []
        if "max" in k: n = int((col > k["max"]).sum()); ihlal += n; notlar += [f">max {n}"] if n else []
        if "degerler" in k: n = int((~col.isin(k["degerler"])).sum()); ihlal += n; notlar += [f"tanımsız {n}"] if n else []
        if k.get("benzersiz") and col.duplicated().any(): n = int(col.duplicated().sum()); ihlal += n; notlar.append(f"yinelenen {n}")
        toplam_ihlal += ihlal
        s.append(f"| {ad} | {100*col.isna().mean():.1f} | {col.nunique()} | {ihlal} | {', '.join(notlar) or '—'} |")
    s += ["", f"**Toplam ihlal: {toplam_ihlal}**"]
    return s

if __name__ == "__main__":
    with open("sema.yaml", encoding="utf-8") as f:
        sema = yaml.safe_load(f)
    df = pd.read_csv(YOL)
    satirlar = rapor(df, sema)
    os.makedirs("cikti", exist_ok=True)
    with open("cikti/kalite_raporu.md", "w", encoding="utf-8") as f:
        f.write("\n".join(satirlar))
    print("\n".join(satirlar))
    print("\ncikti/kalite_raporu.md yazıldı")
