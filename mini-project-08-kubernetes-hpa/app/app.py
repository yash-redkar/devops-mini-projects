from flask import Flask, jsonify
import time
import math
import os

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Kubernetes HPA Demo App",
        "status": "running",
        "pod_name": os.getenv("HOSTNAME", "local")
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/cpu")
def cpu_load():
    start_time = time.time()
    result = 0

    while time.time() - start_time < 0.5:
        for number in range(1, 10000):
            result += math.sqrt(number) * math.sin(number)

    return jsonify({
        "message": "CPU load generated",
        "pod_name": os.getenv("HOSTNAME", "local"),
        "result": result
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
