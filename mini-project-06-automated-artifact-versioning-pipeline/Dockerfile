FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --user --no-cache-dir -r requirements.txt


FROM python:3.11-slim AS runner

WORKDIR /app

ARG APP_VERSION=development
ARG COMMIT_SHA=local

ENV PATH=/root/.local/bin:$PATH
ENV APP_VERSION=${APP_VERSION}
ENV COMMIT_SHA=${COMMIT_SHA}

COPY --from=builder /root/.local /root/.local
COPY app.py .

EXPOSE 8080

CMD ["python", "app.py"]