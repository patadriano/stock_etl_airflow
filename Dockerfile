FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/load_stocks.py .
COPY app/compute_indicators.py .
COPY app/generate_signals.py .

# Add to Dockerfile:
COPY app/append_stocks.py .
COPY app/append_indicators.py .
COPY app/append_signals.py .

CMD ["python", "load_stocks.py"]