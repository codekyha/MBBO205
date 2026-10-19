PY=.venv/bin/python
PIP=.venv/bin/pip

.PHONY: kur veri test temizle hafta01 hafta02 hafta03 hafta04 hafta05 hafta06 hafta07 hafta08 hafta09 hafta10 hafta11 hafta12 hafta13 hafta14 hafta15

kur:
	python3 -m venv .venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

veri:
	$(PY) ortak/veri_uret.py

hafta01:
	cd hafta01_linux && bash 01_sistem_bilgisi.sh && bash 02_dosya_islemleri.sh && bash 03_metin_isleme.sh && bash 04_surec_izleme.sh

hafta02:
	cd hafta02_python && ../$(PY) 01_temeller.py && ../$(PY) 02_numpy_pandas.py

hafta03: veri
	cd hafta03_etl && ../$(PY) 01_veri_cek.py && ../$(PY) 02_temizle.py && ../$(PY) 03_kalite_raporu.py

hafta04: veri
	cd hafta04_eda && ../$(PY) 01_ozet.py && ../$(PY) 02_gorsel.py

hafta05: veri
	cd hafta05_ml && ../$(PY) 01_siniflandirma.py && ../$(PY) 02_regresyon.py

hafta06: veri
	cd hafta06_degerlendirme && ../$(PY) 01_capraz_dogrulama.py && ../$(PY) 02_hiperparametre.py && ../$(PY) 03_karisiklik_matrisi.py

hafta07: veri
	cd hafta07_denetimsiz && ../$(PY) 01_kmeans.py && ../$(PY) 02_pca.py

hafta08:
	cd hafta08_docker && docker build -t mbbo205/hafta08 . && docker run --rm mbbo205/hafta08

hafta09: veri
	cd hafta09_api && ../$(PY) egit.py && docker compose up --build -d && sleep 3 && bash istek.sh; cd hafta09_api && docker compose down

hafta10:
	cd hafta10_bulut && docker compose up -d && ../$(PY) s3_yukle.py; cd hafta10_bulut && docker compose down

hafta11:
	cd hafta11_derin && ../$(PY) 01_mlp_torch.py && ../$(PY) 02_hf_pipeline.py

hafta12:
	cd hafta12_llm && ../$(PY) 01_ollama_api.py && ../$(PY) 02_istem_muhendisligi.py

hafta13:
	cd hafta13_rag && ../$(PY) 01_rag.py && ../$(PY) 02_bellek.py

hafta14:
	cd hafta14_mlops && ../$(PY) egit_ve_kaydet.py && ../$(PY) izleme.py && ../.venv/bin/pytest -q

hafta15:
	cd hafta15_proje && cat README.md

test:
	cd hafta14_mlops && ../.venv/bin/pytest -q

temizle:
	find . -name cikti -type d -prune -exec rm -rf {} +
	find . -name "*.pkl" -delete
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
