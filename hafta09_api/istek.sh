#!/usr/bin/env bash
PORT=${1:-8000}
echo "== sağlık =="; curl -s localhost:$PORT/saglik; echo
echo "== tek tahmin =="
curl -s -X POST localhost:$PORT/tahmin -H "Content-Type: application/json" \
  -d '{"yas":34,"gelir":28000,"kidem_ay":6,"aylik_islem":3,"sehir":"Istanbul","segment":"Bireysel"}'; echo
echo "== geçersiz girdi (422 beklenir) =="
curl -s -o /dev/null -w "HTTP %{http_code}\n" -X POST localhost:$PORT/tahmin -H "Content-Type: application/json" \
  -d '{"yas":-5,"gelir":28000,"kidem_ay":6,"aylik_islem":3,"sehir":"Istanbul","segment":"Bireysel"}'
echo "== toplu =="
curl -s -X POST localhost:$PORT/tahmin/toplu -H "Content-Type: application/json" \
  -d '[{"yas":34,"gelir":28000,"kidem_ay":6,"aylik_islem":3,"sehir":"Istanbul","segment":"Bireysel"},
       {"yas":58,"gelir":90000,"kidem_ay":110,"aylik_islem":25,"sehir":"Ankara","segment":"Kurumsal"}]'; echo
echo "== belge: http://localhost:$PORT/docs =="
