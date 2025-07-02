# docker/Dockerfile
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy env and code
COPY env/ ./env/
COPY lib/ ./lib/
COPY core/ ./core/
COPY requirements.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment (change this in docker-compose)
ENV APP_ENV=local

CMD ["uvicorn", "lib.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
