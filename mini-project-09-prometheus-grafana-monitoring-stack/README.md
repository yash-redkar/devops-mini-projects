# Mini Project 09: Prometheus + Grafana Monitoring Stack

## Project Overview

This project demonstrates a Kubernetes monitoring stack using Prometheus, Grafana, Helm, and a sample Flask application.

Prometheus scrapes custom metrics exposed by the Flask app through the `/metrics` endpoint. Grafana visualizes those metrics in a custom dashboard showing request rate, error rate, request rate by endpoint, pod CPU usage, and pod memory usage.

## Tech Stack

* Kubernetes
* Minikube
* Helm
* Prometheus
* Grafana
* Prometheus Operator
* ServiceMonitor
* PromQL
* Python Flask
* Docker

## Project Structure

```text
mini-project-09-prometheus-grafana-monitoring-stack/
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── service.yaml
│   └── servicemonitor.yaml
│
├── dashboard/
│   └── grafana-dashboard.json
│
├── notes.md
└── README.md
```

## Application Endpoints

| Endpoint   | Description                  |
| ---------- | ---------------------------- |
| `/`        | Application status           |
| `/work`    | Simulates successful request |
| `/error`   | Simulates HTTP 500 error     |
| `/health`  | Health check                 |
| `/metrics` | Prometheus metrics endpoint  |

## Metrics Exposed

The Flask app exposes custom metrics using `prometheus-client`.

```text
sample_app_requests_total
sample_app_request_duration_seconds
```

These metrics help track request count, HTTP status, endpoint traffic, and request latency.

## Kubernetes Resources

| Resource       | Name                             |
| -------------- | -------------------------------- |
| Namespace      | `monitoring-demo`                |
| Deployment     | `monitoring-demo-app`            |
| Service        | `monitoring-demo-service`        |
| ServiceMonitor | `monitoring-demo-servicemonitor` |

## Build Docker Image

For Git Bash:

```bash
eval $(minikube docker-env)
docker build -t monitoring-demo-app:v1 ./app
```

For PowerShell:

```powershell
minikube docker-env | Invoke-Expression
docker build -t monitoring-demo-app:v1 ./app
```

## Deploy Application

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/servicemonitor.yaml
```

Check resources:

```bash
kubectl get all -n monitoring-demo
kubectl get servicemonitor -n monitoring-demo
```

## Access Application

```bash
minikube service monitoring-demo-service -n monitoring-demo --url
```

Example endpoints:

```text
http://127.0.0.1:<port>/
http://127.0.0.1:<port>/work
http://127.0.0.1:<port>/error
http://127.0.0.1:<port>/metrics
```

## Prometheus

Port-forward Prometheus:

```bash
kubectl port-forward -n monitoring svc/monitoring-kube-prometheus-prometheus 9090:9090
```

Open:

```text
http://localhost:9090
```

Prometheus target proof:

```text
serviceMonitor/monitoring-demo/monitoring-demo-servicemonitor/0
2 / 2 up
```

## Grafana

Port-forward Grafana:

```bash
kubectl port-forward -n monitoring svc/monitoring-grafana 3001:80
```

Open:

```text
http://localhost:3001
```

## Grafana Dashboard Panels

| Panel                    | PromQL Query                                                                                                           |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------- |
| Request Rate             | `sum(rate(sample_app_requests_total[1m]))`                                                                             |
| Error Rate               | `sum(rate(sample_app_requests_total{http_status=~"5.."}[1m]))`                                                         |
| Request Rate by Endpoint | `sum(rate(sample_app_requests_total[1m])) by (exported_endpoint)`                                                      |
| Pod CPU Usage            | `sum(rate(container_cpu_usage_seconds_total{namespace="monitoring-demo", pod=~"monitoring-demo-app.*"}[1m])) by (pod)` |
| Pod Memory Usage         | `sum(container_memory_working_set_bytes{namespace="monitoring-demo", pod=~"monitoring-demo-app.*"}) by (pod)`          |

## Dashboard Export

The Grafana dashboard is exported and saved as:

```text
dashboard/grafana-dashboard.json
```

## Success Outcome

This project demonstrates:

* Prometheus and Grafana running on Minikube
* Flask app exposing custom Prometheus metrics
* ServiceMonitor scraping app metrics
* Prometheus targets showing app as `UP`
* Grafana dashboard showing request rate, error rate, endpoint traffic, CPU usage, and memory usage
* Dashboard exported as JSON

## Author

Yash Redkar
