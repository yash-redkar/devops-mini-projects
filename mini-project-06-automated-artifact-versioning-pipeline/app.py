import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "development")
COMMIT_SHA = os.getenv("COMMIT_SHA", "local")


@app.route("/")
def home():
    return jsonify({
        "message": "Automated Artifact Versioning API",
        "version": APP_VERSION,
        "commit": COMMIT_SHA,
        "status": "running"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "artifact-versioning-api"
    })


@app.route("/version")
def version():
    return jsonify({
        "version": APP_VERSION,
        "commit": COMMIT_SHA
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
