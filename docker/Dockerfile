FROM python:3.11-slim

WORKDIR /app

COPY env/ ./env/
COPY lib/ ./lib/
COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV APP_ENV=local
ENV PYTHONPATH=/app/lib

CMD ["uvicorn", "lib.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
