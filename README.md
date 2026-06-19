# DevOps Mini Projects

This repository contains all mini projects completed during the DevOps training program.

Each mini project is maintained in a separate folder inside this single repository.
The projects demonstrate hands-on DevOps skills including Linux automation, Git workflow, Docker, Docker Hub, GitHub Actions, Docker Compose, Kubernetes, networking, persistent storage, artifact versioning, self-healing, autoscaling, metrics, and release automation.

## Mini Projects List

| No. | Mini Project Name                      | Status    |
| --- | -------------------------------------- | --------- |
| 01  | Linux Sysadmin Automation Kit          | Completed |
| 02  | Git Workflow Simulator                 | Completed |
| 03  | Dockerized To-Do API                   | Completed |
| 04  | CI Pipeline for a Python App           | Completed |
| 05  | Docker Compose Full-Stack App          | Completed |
| 06  | Automated Artifact Versioning Pipeline | Completed |
| 07  | Kubernetes Self-Healing App Demo       | Completed |
| 08  | Kubernetes Horizontal Pod Autoscaler   | Completed |
| 09  | Prometheus + Grafana Monitoring Stack  | Pending   |
| 10  | Terraform AWS EC2 Deployment           | Pending   |
| 11  | Static Website CI/CD to S3             | Pending   |
| 12  | Multi-Environment Deployment Pipeline  | Pending   |
| 13  | Log Aggregation with ELK Lite          | Pending   |
| 14  | Secrets Management with Vault/AWS SSM  | Pending   |
| 15  | Rollback Strategy Implementation       | Pending   |

## Completed Projects Summary

### Mini Project 01: Linux Sysadmin Automation Kit

A shell script-based automation project that performs basic system health checks such as disk usage, memory information, process status, service checks, and log generation.

**Skills used:** Linux, Shell Scripting, Git Bash, System Monitoring

---

### Mini Project 02: Git Workflow Simulator

A Git and GitHub workflow simulation project demonstrating feature branches, pull requests, code review comments, merge conflicts, conflict resolution, release tagging, and GitHub Releases.

**Skills used:** Git, GitHub, Branching, Pull Requests, Merge Conflict Resolution, Release Tagging

---

### Mini Project 03: Dockerized To-Do API

A REST API built with Node.js and Express, containerized using a multi-stage Dockerfile, tagged with semantic versioning, and pushed publicly to Docker Hub.

**Skills used:** Docker, Dockerfile, REST API, Docker Hub, Semantic Versioning

**Docker Hub Image:**

```text
yashredkar/dockerized-todo-api:v1.0.0
```

---

### Mini Project 04: CI Pipeline for a Python App

A Python Student Grade Calculator with automated CI using GitHub Actions. The pipeline performs linting using flake8, unit testing using pytest, and coverage reporting using pytest-cov.

**Skills used:** Python, pytest, flake8, pytest-cov, GitHub Actions, CI/CD

**CI Result:** Green build with 100% test coverage for core logic.

---

### Mini Project 05: Docker Compose Full-Stack App

A three-container full-stack application deployed using Docker Compose.

The application includes:

* Nginx frontend
* Flask backend API
* PostgreSQL database
* Docker volume for persistent database storage
* Custom Docker bridge network
* Health checks and restart policies

**Skills used:** Docker Compose, Nginx, Flask, PostgreSQL, Docker Networking, Docker Volumes

**Run command:**

```bash
docker compose up --build -d
```

---

### Mini Project 06: Automated Artifact Versioning Pipeline

An automated release pipeline using GitHub Actions that builds a Docker image when a semantic version tag is pushed.

The pipeline automatically:

* Builds a Docker image
* Tags the image with semantic version
* Tags the image with git commit SHA
* Pushes the image to Docker Hub
* Generates release notes
* Uploads changelog artifact
* Creates a GitHub Release

**Skills used:** GitHub Actions, Docker, Docker Hub, Semantic Versioning, Release Automation

**Docker Hub Image:**

```text
yashredkar/artifact-versioning-api:v1.0.0
```

**Release Tag Example:**

```text
mp06-v1.0.0
```

---

### Mini Project 07: Kubernetes Self-Healing App Demo

A Kubernetes self-healing demo using Minikube. The project deploys an Nginx web application using a Kubernetes Deployment with 3 replicas.

The application is exposed using:

* ClusterIP Service for internal access
* NodePort Service for external browser access

A shell script randomly deletes one running pod to simulate failure. Kubernetes automatically creates a replacement pod and restores the deployment back to 3 running replicas.

**Skills used:** Kubernetes, Minikube, kubectl, YAML, Deployments, ReplicaSets, Services, Shell Scripting

**Self-healing proof:**

```text
Before deletion: 3 pods Running
Deleted pod: self-healing-web-75dcbc9c66-kblgs
New replacement pod: self-healing-web-75dcbc9c66-wk6wv
Final deployment status: 3/3 READY
```

**Run command:**

```bash
kubectl apply -f k8s/
```

**Chaos script:**

```bash
./scripts/pod-chaos.sh
```

---

### Mini Project 08: Kubernetes Horizontal Pod Autoscaler

A Kubernetes autoscaling demo using Minikube, Metrics Server, and Horizontal Pod Autoscaler.

The project deploys a CPU-intensive Flask application with an initial replica count of 2 pods. HPA monitors CPU usage and automatically scales the application between 2 and 8 pods.

The application is exposed using a NodePort Service and load is generated against the CPU-intensive endpoint.

**Skills used:** Kubernetes, Minikube, kubectl, YAML, Metrics Server, Horizontal Pod Autoscaler, Load Testing, Docker, Flask

**Autoscaling proof:**

```text
Initial replicas: 2
CPU target: 50%
CPU reached: 413% / 50%
Scale up: 2 → 4 → 8 pods
Scale down: 8 → 2 pods
Final CPU: 1% / 50%
```

**HPA event proof:**

```text
SuccessfulRescale New size: 4; reason: cpu resource utilization above target
SuccessfulRescale New size: 8; reason: cpu resource utilization above target
SuccessfulRescale New size: 2; reason: All metrics below target
```

**Run command:**

```bash
kubectl apply -f k8s/
```

**Watch HPA:**

```bash
kubectl get hpa -n hpa-demo -w
```

## Repository Structure

```text
vit-devops-projects/
│
├── README.md
│
├── .github/
│   └── workflows/
│       ├── python-ci.yml
│       └── artifact-versioning.yml
│
├── mini-project-01-linux-sysadmin-automation-kit/
│   ├── health_check.sh
│   ├── README.md
│   └── logs/
│
├── mini-project-02-git-workflow-simulator/
│   ├── README.md
│   ├── CONTRIBUTING.md
│   ├── CHANGELOG.md
│   ├── TEAM.md
│   ├── release-notes.md
│   └── app/
│
├── mini-project-03-dockerized-todo-api/
│   ├── Dockerfile
│   ├── README.md
│   ├── package.json
│   ├── package-lock.json
│   └── src/
│
├── mini-project-04-ci-pipeline-python-app/
│   ├── app.py
│   ├── test_app.py
│   ├── requirements.txt
│   ├── README.md
│   └── .gitignore
│
├── mini-project-05-docker-compose-full-stack-app/
│   ├── docker-compose.yml
│   ├── .env.example
│   ├── README.md
│   ├── backend/
│   └── frontend/
│
├── mini-project-06-automated-artifact-versioning-pipeline/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── README.md
│   └── .dockerignore
│
├── mini-project-07-kubernetes-self-healing-app-demo/
│   ├── k8s/
│   ├── scripts/
│   └── README.md
│
└── mini-project-08-kubernetes-hpa/
    ├── app/
    │   ├── app.py
    │   ├── Dockerfile
    │   └── requirements.txt
    ├── k8s/
    │   ├── namespace.yaml
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   └── hpa.yaml
    ├── scripts/
    │   └── load-test.sh
    └── README.md
```

## Current Status

Mini Projects 01 to 08 are completed, tested, and pushed to GitHub.

The repository currently demonstrates:

* Linux automation
* Git and GitHub collaboration workflow
* Dockerized REST API
* GitHub Actions CI pipeline
* Docker Compose full-stack deployment
* Automated Docker image versioning
* Docker Hub release artifact publishing
* GitHub Release automation
* Kubernetes Deployments and Services
* Kubernetes self-healing using ReplicaSets
* Kubernetes autoscaling using HPA and Metrics Server

Upcoming projects will focus on monitoring, Terraform, cloud deployment, secrets management, and rollback strategies.

## Author

Yash Redkar
