FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y \
    nmap \
    iproute2 \
    procps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && \
    pipenv install --system --deploy

COPY . .

RUN chmod +x monitor.py

CMD ["./monitor.py"]