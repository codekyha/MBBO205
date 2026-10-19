# Derleme bağlamı proje kökü olmalı: docker build -f servis/Dockerfile .
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY servis/ .
COPY model/ model/
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
