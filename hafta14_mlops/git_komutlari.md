# Takım için Git rehberi

```bash
git clone <depo-url> && cd <depo>
git switch -c ozellik/etl-iyilestirme        # her iş için ayrı dal
git add -p && git commit -m "ETL: Türkçe sayı biçimi dönüşümü eklendi"
git push -u origin ozellik/etl-iyilestirme   # ardından GitHub'da Pull Request açın
git fetch origin && git rebase origin/main   # dalı güncel tutun
# çatışma: dosyayı düzenle -> git add <dosya> -> git rebase --continue
git log --oneline --graph --all | head -20
git tag -a v1.0.0 -m "final teslim" && git push --tags
```

Kurallar: `main` dalına doğrudan commit yok; her PR en az bir takım arkadaşı tarafından incelenir; commit mesajı
"ne" değil "neden" anlatır; büyük veri dosyaları (`> 5 MB`) depoya girmez (`.gitignore` + nesne depolama).
