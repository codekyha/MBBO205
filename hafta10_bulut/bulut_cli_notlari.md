# Bulut CLI eşdeğerleri (isteğe bağlı; hesap gerektirir)

| İşlem | AWS | GCP | Azure |
|---|---|---|---|
| Kova oluştur | `aws s3 mb s3://mbbo205` | `gsutil mb gs://mbbo205` | `az storage container create -n mbbo205` |
| Dosya yükle | `aws s3 cp musteri.csv s3://mbbo205/` | `gsutil cp musteri.csv gs://mbbo205/` | `az storage blob upload -c mbbo205 -f musteri.csv` |
| Listele | `aws s3 ls s3://mbbo205/` | `gsutil ls gs://mbbo205/` | `az storage blob list -c mbbo205 -o table` |
| Sanal makine | `aws ec2 run-instances --instance-type t3.small ...` | `gcloud compute instances create ...` | `az vm create ...` |
| Konteyner çalıştır | ECS/App Runner | Cloud Run: `gcloud run deploy api --source .` | `az container create ...` |

Ücretsiz katman sınırları ve fiyatlar sık değişir; ödev raporlarında fiyat kaynağını ve tarihini belirtin.
MinIO'ya `aws` CLI ile erişim: `aws --endpoint-url http://localhost:9000 s3 ls` (kimlik: minioadmin/minioadmin).
