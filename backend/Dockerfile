FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PYTHONPATH=/app/api/v1/integrations/_allegro/sdk/output

# na przyszłość przy dodawaniu innych sdk w razie potrzeby użyć wiele ENV:
# ENV PYTHONPATH=\
# /app/api/v1/integrations/_allegro/sdk/output:\
# /app/api/v1/integrations/_amazon/sdk/output:\
# /app/api/v1/integrations/_ebay/sdk/output

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app
COPY .env .

# EXPOSE 8000
