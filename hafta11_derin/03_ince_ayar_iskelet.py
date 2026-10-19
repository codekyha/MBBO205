#!/usr/bin/env python3
"""İnce ayar iskeleti: küçük Türkçe metin kümesi, Trainer API. GPU önerilir; CPU'da epok=1 ile deneyin."""
import argparse, sys
ap = argparse.ArgumentParser(); ap.add_argument("--epok", type=int, default=1); ap.add_argument("--model", default="dbmdz/bert-base-turkish-cased"); a = ap.parse_args()
try:
    from datasets import Dataset
    from transformers import AutoTokenizer, AutoModelForSequenceClassification, TrainingArguments, Trainer
    import numpy as np
except ImportError:
    sys.exit("pip install -r requirements.txt")
metin = ["Harika bir deneyimdi", "Berbat, bir daha almam", "Beklentimi karşıladı", "Çok yavaş ve pahalı", "Kesinlikle tavsiye ederim", "Destek hattı cevap vermiyor",
         "Kurulum çok kolaydı", "Para iadesi alamadım", "Kalitesi iyi", "Ürün bozuk geldi"] * 4
etiket = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0] * 4
ds = Dataset.from_dict({"text": metin, "label": etiket}).train_test_split(test_size=.25, seed=42)
tok = AutoTokenizer.from_pretrained(a.model)
ds = ds.map(lambda b: tok(b["text"], truncation=True, padding="max_length", max_length=32), batched=True)
model = AutoModelForSequenceClassification.from_pretrained(a.model, num_labels=2)
def metrik(p): return {"dogruluk": float((np.argmax(p.predictions, -1) == p.label_ids).mean())}
tr = Trainer(model=model, args=TrainingArguments("cikti/ince_ayar", num_train_epochs=a.epok, per_device_train_batch_size=8, logging_steps=5, report_to=[]),
             train_dataset=ds["train"], eval_dataset=ds["test"], compute_metrics=metrik)
tr.train(); print(tr.evaluate())
