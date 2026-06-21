from flask import Flask, jsonify, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import random
import time
import os

app = Flask(__name__)

REQUEST_COUNT = Counter(
    "sample_app_requests_total",
    "Total number of requests",
    ["endpoint", "method", "http_status"]
)

REQUEST_LATENCY = Histogram(
    "sample_app_request_duration_seconds",
    "Request latency in seconds",
    ["endpoint"]
)


@app.route("/")
def home():
    start_time = time.time()
    status = "200"

    REQUEST_COUNT.labels(endpoint="/", method="GET", http_status=status).inc()
    REQUEST_LATENCY.labels(endpoint="/").observe(time.time() - start_time)

    return jsonify({
        "message": "Prometheus Grafana Monitoring Demo App",
        "pod_name": os.getenv("HOSTNAME", "local"),
        "status": "running"
    })


@app.route("/work")
def work():
    start_time = time.time()
    status = "200"

    time.sleep(random.uniform(0.05, 0.3))

    REQUEST_COUNT.labels(endpoint="/work", method="GET", http_status=status).inc()
    REQUEST_LATENCY.labels(endpoint="/work").observe(time.time() - start_time)

    return jsonify({
        "message": "Work request completed",
        "pod_name": os.getenv("HOSTNAME", "local")
    })


@app.route("/error")
def error():
    start_time = time.time()
    status = "500"

    REQUEST_COUNT.labels(endpoint="/error", method="GET", http_status=status).inc()
    REQUEST_LATENCY.labels(endpoint="/error").observe(time.time() - start_time)

    return jsonify({
        "message": "Simulated error response",
        "status": "error"
    }), 500


@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)