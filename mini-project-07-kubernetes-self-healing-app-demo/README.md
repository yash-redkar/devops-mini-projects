# Mini Project 07: Kubernetes Self-Healing App Demo

## Project Overview

This mini project demonstrates Kubernetes self-healing using Minikube.

A simple Nginx web application is deployed using a Kubernetes Deployment with 3 replicas. The application is exposed internally using a ClusterIP Service and externally using a NodePort Service.

A shell script randomly deletes one running pod to simulate failure. Kubernetes automatically detects the missing pod and creates a new pod to restore the desired state.

## Core Concept

Kubernetes works on the principle of desired state.

In this project, the desired state is:

```text
3 running pods
```

When one pod is deleted manually, the actual state becomes:

```text
2 running pods
```

Kubernetes automatically creates a replacement pod and brings the system back to:

```text
3 running pods
```

This is Kubernetes self-healing.

## Architecture

```text
Browser
   |
   v
NodePort Service
   |
   v
ClusterIP Service
   |
   v
Deployment
   |
   v
3 Nginx Pods
```

## Tech Stack

* Kubernetes
* Minikube
* kubectl
* YAML
* Nginx
* Shell Script

## Project Structure

```text
mini-project-07-kubernetes-self-healing-app-demo/
│
├── k8s/
│   ├── namespace.yaml
│   ├── deployment.yaml
│   ├── clusterip-service.yaml
│   └── nodeport-service.yaml
│
├── scripts/
│   └── pod-chaos.sh
│
└── README.md
```

## Kubernetes Resources

| Resource          | Name                     | Purpose                      |
| ----------------- | ------------------------ | ---------------------------- |
| Namespace         | `self-healing-demo`      | Isolates project resources   |
| Deployment        | `self-healing-web`       | Maintains 3 running replicas |
| ClusterIP Service | `self-healing-clusterip` | Internal service access      |
| NodePort Service  | `self-healing-nodeport`  | External browser access      |

## Deployment Details

The application is deployed with 3 replicas:

```yaml
replicas: 3
```

This means Kubernetes will always try to keep 3 pods running.

## Run the Project

Start Minikube:

```bash
minikube start
```

Apply Kubernetes manifests:

```bash
kubectl apply -f k8s/
```

Check all resources:

```bash
kubectl get all -n self-healing-demo
```

Check pods:

```bash
kubectl get pods -n self-healing-demo -o wide
```

## Access the Application

Open the NodePort service:

```bash
minikube service self-healing-nodeport -n self-healing-demo
```

Or get the service URL:

```bash
minikube service self-healing-nodeport -n self-healing-demo --url
```

The browser should show the default Nginx welcome page.

## Self-Healing Demo

Run the chaos script:

```bash
./scripts/pod-chaos.sh
```

The script performs the following steps:

1. Lists the current running pods
2. Selects one random pod
3. Deletes the selected pod
4. Shows the newly created replacement pod
5. Watches Kubernetes restore the desired state

## Proof of Self-Healing

Before deletion:

```text
3 pods Running
```

Deleted pod:

```text
self-healing-web-75dcbc9c66-kblgs
```

New replacement pod created:

```text
self-healing-web-75dcbc9c66-wk6wv
```

Final deployment status:

```text
self-healing-web   3/3   3   3
```

This proves that Kubernetes restored the desired state automatically.

## Useful Commands

Check pods:

```bash
kubectl get pods -n self-healing-demo
```

Watch pods:

```bash
kubectl get pods -n self-healing-demo -w
```

Check deployment:

```bash
kubectl get deployment -n self-healing-demo
```

Check services:

```bash
kubectl get svc -n self-healing-demo
```

Delete one pod manually:

```bash
kubectl delete pod <pod-name> -n self-healing-demo
```

Delete all project resources:

```bash
kubectl delete namespace self-healing-demo
```

## What I Learned

Through this project, I learned:

* How Kubernetes Deployments maintain desired state
* How ReplicaSets recreate deleted pods
* How to expose applications using ClusterIP and NodePort Services
* How to use kubectl to inspect Kubernetes resources
* How Kubernetes performs self-healing automatically
* How to write a shell script to simulate pod failure

## Real-World Use Case

In production systems, application containers can crash due to bugs, memory issues, or node failures. Kubernetes self-healing helps maintain application availability by automatically replacing failed pods without manual intervention.

## Author

Yash Redkar
