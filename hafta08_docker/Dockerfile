FROM python:3.12-slim
WORKDIR /app
# Önce bağımlılıklar: kod değişince bu katman önbellekten gelir
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app.py .
ENV N_ESTIMATORS=200
CMD ["python", "app.py"]
