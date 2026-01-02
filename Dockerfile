FROM python:3.9-slim as builder
COPY requirements.txt .
RUN apt-get update && apt-get install -y gcc
RUN pip install --no-cache-dir --target=/install -r requirements.txt 
FROM python:3.9-slim as producer
COPY --from=builder /install /usr/local/lib/python3.9/site-packages
ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages
WORKDIR /app
RUN groupadd -r amir && useradd -r -g amir amir
COPY . .
RUN chown amir:amir /app
USER amir
EXPOSE 5000
CMD ["python", "main.py"]