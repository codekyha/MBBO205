#!/usr/bin/env python3
"""Betimsel istatistik ve korelasyon raporu."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from ortak.yardimci import veri_yukle, SAYISAL, cikti_dizini

df = veri_yukle()
C = cikti_dizini(__file__)
s = ["# EDA özeti", "", "## Betimsel istatistik", df[SAYISAL + ["harcama"]].describe().round(2).to_markdown(), "",
     "## Korelasyon", df[SAYISAL + ["harcama", "ayrildi"]].corr().round(3).to_markdown(), "",
     "## Hedef oranları", f"churn oranı: {df.ayrildi.mean():.3f}", "",
     "### Segmente göre", df.groupby("segment")[["harcama", "ayrildi"]].mean().round(3).to_markdown(), "",
     "### Şehre göre", df.groupby("sehir")[["harcama", "ayrildi"]].mean().round(3).to_markdown()]
metin = "\n".join(s)
with open(os.path.join(C, "eda_ozet.md"), "w", encoding="utf-8") as f:
    f.write(metin)
print(metin)
