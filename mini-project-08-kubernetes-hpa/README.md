# Mini Project 08: Kubernetes Horizontal Pod Autoscaler

## Project Overview

This mini project demonstrates Kubernetes Horizontal Pod Autoscaler using Minikube.

A CPU-intensive Flask application is deployed on Kubernetes with an initial replica count of 2 pods. The application is exposed using a NodePort Service. A Horizontal Pod Autoscaler is configured to scale the application from 2 pods to 8 pods based on CPU usage.

Load is generated on the CPU-intensive endpoint to increase CPU utilization. Kubernetes HPA detects the high CPU usage and automatically scales the number of pods. After the load is stopped, HPA slowly scales the application back down.

## Core Concept

Kubernetes Horizontal Pod Autoscaler automatically changes the number of running pods based on resource usage.

In this project:

```text
Minimum pods: 2
Maximum pods: 8
CPU target: 50%
```

When CPU usage goes above 50%, Kubernetes scales the application up.

When CPU usage goes below the target, Kubernetes gradually scales the application down.

## Architecture

```text
User / Load Generator
        |
        v
NodePort Service
        |
        v
Flask CPU-Intensive Application Pods
        |
        v
Horizontal Pod Autoscaler
        |
        v
Metrics Server
```

## Tech Stack

* Kubernetes
* Minikube
* kubectl
* Metrics Server
* Horizontal Pod Autoscaler
* Docker
* Python Flask
* YAML
* Load Testing

## Project Structure

```text
mini-project-08-kubernetes-hpa/
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
│   └── hpa.yaml
│
├── scripts/
│   └── load-test.sh
│
└── README.md
```

## Application Details

The application is a Flask API with three endpoints.

| Endpoint  | Description                        |
| --------- | ---------------------------------- |
| `/`       | Returns app status and pod name    |
| `/health` | Health check endpoint              |
| `/cpu`    | Generates CPU load for HPA testing |

The `/cpu` endpoint performs CPU-heavy calculations for a short time. When many requests are sent to this endpoint, CPU usage increases and HPA starts scaling pods.

## Kubernetes Resources

| Resource   | Name               | Purpose                             |
| ---------- | ------------------ | ----------------------------------- |
| Namespace  | `hpa-demo`         | Isolates project resources          |
| Deployment | `hpa-demo-app`     | Runs the Flask app                  |
| Service    | `hpa-demo-service` | Exposes the app using NodePort      |
| HPA        | `hpa-demo-app`     | Auto-scales pods based on CPU usage |

## HPA Configuration

The HPA is configured with:

```yaml
minReplicas: 2
maxReplicas: 8
averageUtilization: 50
```

This means:

```text
Start with minimum 2 pods.
Scale up if average CPU usage crosses 50%.
Do not scale above 8 pods.
Scale down when CPU usage becomes low.
```

## Why CPU Requests Are Important

HPA calculates CPU utilization based on the CPU request value defined in the Deployment.

In the Deployment, CPU request is configured as:

```yaml
resources:
  requests:
    cpu: "100m"
```

This allows HPA to calculate CPU percentage correctly.

Without CPU requests, HPA may show:

```text
<unknown>/50%
```

and autoscaling may not work properly.

## Build Docker Image in Minikube

Since this project uses a local Docker image, the image is built inside Minikube's Docker environment.

For PowerShell:

```powershell
minikube docker-env | Invoke-Expression
docker build -t hpa-demo-app:v1 ./app
```

For Git Bash:

```bash
eval $(minikube docker-env)
docker build -t hpa-demo-app:v1 ./app
```

The Deployment uses:

```yaml
image: hpa-demo-app:v1
imagePullPolicy: Never
```

This tells Kubernetes to use the locally available Minikube image instead of pulling from Docker Hub.

## Deploy the Application

Apply all Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Check all resources:

```bash
kubectl get all -n hpa-demo
```

Check pods:

```bash
kubectl get pods -n hpa-demo -o wide
```

Check HPA:

```bash
kubectl get hpa -n hpa-demo
```

## Access the Application

Get the Minikube service URL:

```bash
minikube service hpa-demo-service -n hpa-demo --url
```

Example output:

```text
http://127.0.0.1:51045
```

Open the app:

```text
http://127.0.0.1:51045
```

Test CPU endpoint:

```text
http://127.0.0.1:51045/cpu
```

## Load Testing

A load script is included:

```bash
./scripts/load-test.sh <minikube-service-url>
```

Example:

```bash
./scripts/load-test.sh http://127.0.0.1:51045
```

The script continuously sends requests to:

```text
/cpu
```

This increases CPU usage and triggers HPA scaling.

A Kubernetes-based load generator can also be used:

```bash
kubectl run load-generator -n hpa-demo --image=busybox --restart=Never -- /bin/sh -c "while true; do wget -q -O- http://hpa-demo-service/cpu > /dev/null; done"
```

Multiple load generator pods can be created to increase CPU pressure.

## Watch Autoscaling

Watch HPA:

```bash
kubectl get hpa -n hpa-demo -w
```

Watch pods:

```bash
kubectl get pods -n hpa-demo -w
```

Check CPU usage:

```bash
kubectl top pods -n hpa-demo
```

Describe HPA:

```bash
kubectl describe hpa hpa-demo-app -n hpa-demo
```

## Autoscaling Proof

Initial state:

```text
Minimum replicas: 2
Current replicas: 2
CPU target: 50%
```

Under load:

```text
CPU reached: 413% / 50%
```

HPA scaled the application:

```text
2 pods → 4 pods → 8 pods
```

Pod creation was observed as:

```text
Pending → ContainerCreating → Running
```

After load stopped:

```text
CPU reduced to: 1% / 50%
```

HPA scaled the application back down:

```text
8 pods → 2 pods
```

HPA event proof:

```text
SuccessfulRescale New size: 4; reason: cpu resource utilization above target
SuccessfulRescale New size: 8; reason: cpu resource utilization above target
SuccessfulRescale New size: 2; reason: All metrics below target
```

Final HPA state:

```text
cpu: 1%/50%
minPods: 2
maxPods: 8
replicas: 2
```

Final pod state:

```text
2 pods Running
```

## Useful Commands

Check HPA:

```bash
kubectl get hpa -n hpa-demo
```

Check pods:

```bash
kubectl get pods -n hpa-demo
```

Check deployment:

```bash
kubectl get deployment -n hpa-demo
```

Check pod CPU and memory:

```bash
kubectl top pods -n hpa-demo
```

Describe HPA:

```bash
kubectl describe hpa hpa-demo-app -n hpa-demo
```

Delete load generator:

```bash
kubectl delete pod load-generator -n hpa-demo
```

Delete all project resources:

```bash
kubectl delete namespace hpa-demo
```

## What I Learned

Through this project, I learned:

* How Kubernetes Horizontal Pod Autoscaler works
* How CPU-based autoscaling is configured
* Why Metrics Server is required for HPA
* Why CPU requests are required for CPU utilization calculation
* How to deploy a CPU-intensive app to Kubernetes
* How to expose the app using NodePort
* How to generate load for autoscaling tests
* How to monitor HPA using kubectl
* How pods scale up and scale down automatically based on CPU usage

## Real-World Use Case

In production environments, application traffic is not constant. During high traffic, more pods are needed to handle load. During low traffic, extra pods waste resources.

HPA helps DevOps teams automatically scale applications based on demand. This improves availability, performance, and resource efficiency.

## Author

Yash Redkar
