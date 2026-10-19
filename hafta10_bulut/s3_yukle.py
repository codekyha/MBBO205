#!/usr/bin/env python3
"""S3 uyumlu depolama (MinIO) ile kova/nesne işlemleri."""
import os
import boto3
from botocore.client import Config

s3 = boto3.client("s3", endpoint_url=os.environ.get("S3_ENDPOINT", "http://localhost:9000"),
                  aws_access_key_id=os.environ.get("S3_KEY", "minioadmin"),
                  aws_secret_access_key=os.environ.get("S3_SECRET", "minioadmin"),
                  config=Config(signature_version="s3v4"), region_name="us-east-1")
KOVA = "mbbo205"
if KOVA not in [b["Name"] for b in s3.list_buckets()["Buckets"]]:
    s3.create_bucket(Bucket=KOVA); print("kova oluşturuldu:", KOVA)
dosyalar = {"veri/musteri.csv": "../veri/musteri.csv", "model/model_churn.pkl": "../hafta09_api/model/model_churn.pkl"}
for anahtar, yol in dosyalar.items():
    if os.path.exists(yol):
        s3.upload_file(yol, KOVA, anahtar); print(f"yüklendi: {yol} -> s3://{KOVA}/{anahtar}")
    else:
        print(f"atlandı (yok): {yol}")
print("nesneler:")
for o in s3.list_objects_v2(Bucket=KOVA).get("Contents", []):
    print(f"  {o['Key']:30s} {o['Size']/1024:8.1f} KB  {o['LastModified']:%Y-%m-%d %H:%M}")
os.makedirs("cikti", exist_ok=True)
s3.download_file(KOVA, "veri/musteri.csv", "cikti/musteri_indirilen.csv"); print("indirildi -> cikti/musteri_indirilen.csv")
url = s3.generate_presigned_url("get_object", Params={"Bucket": KOVA, "Key": "veri/musteri.csv"}, ExpiresIn=3600)
print("imzalı URL (1 saat):", url[:90] + "...")
