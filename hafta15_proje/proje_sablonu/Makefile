.PHONY: kur veri etl egit demo test
kur:
	python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
veri:
	.venv/bin/python etl/indir.py
etl:
	.venv/bin/python etl/temizle.py
egit:
	.venv/bin/python model/egit.py
demo:
	docker compose -f servis/docker-compose.yml up --build -d && sleep 3 && curl -s localhost:8080/saglik && echo
test:
	.venv/bin/pytest -q tests/
