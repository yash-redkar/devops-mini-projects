# DevOps Mini Projects

This repository contains all mini projects completed during the DevOps training program.

Each mini project is maintained in a separate folder inside this single repository.
The projects demonstrate hands-on DevOps skills including Linux automation, Git workflow, Docker, Docker Hub, GitHub Actions, Docker Compose, networking, and persistent storage.

## Mini Projects List

| No. | Mini Project Name                      | Status    |
| --- | -------------------------------------- | --------- |
| 01  | Linux Sysadmin Automation Kit          | Completed |
| 02  | Git Workflow Simulator                 | Completed |
| 03  | Dockerized To-Do API                   | Completed |
| 04  | CI Pipeline for a Python App           | Completed |
| 05  | Docker Compose Full-Stack App          | Completed |
| 06  | Automated Artifact Versioning Pipeline | Pending   |
| 07  | Kubernetes Self-Healing App Demo       | Pending   |
| 08  | Kubernetes Horizontal Pod Autoscaler   | Pending   |
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

# DevOps Mini Projects

This repository contains all mini projects completed during the DevOps training program.

Each mini project is maintained in a separate folder inside this single repository.
The projects demonstrate hands-on DevOps skills including Linux automation, Git workflow, Docker, Docker Hub, GitHub Actions, Docker Compose, networking, and persistent storage.

## Mini Projects List

| No. | Mini Project Name                      | Status    |
| --- | -------------------------------------- | --------- |
| 01  | Linux Sysadmin Automation Kit          | Completed |
| 02  | Git Workflow Simulator                 | Completed |
| 03  | Dockerized To-Do API                   | Completed |
| 04  | CI Pipeline for a Python App           | Completed |
| 05  | Docker Compose Full-Stack App          | Completed |
| 06  | Automated Artifact Versioning Pipeline | Pending   |
| 07  | Kubernetes Self-Healing App Demo       | Pending   |
| 08  | Kubernetes Horizontal Pod Autoscaler   | Pending   |
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

## Repository Structure

```text
vit-devops-projects/
│
├── README.md
│
├── .github/
│   └── workflows/
│       └── python-ci.yml
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
└── mini-project-05-docker-compose-full-stack-app/
    ├── docker-compose.yml
    ├── .env.example
    ├── README.md
    ├── backend/
    └── frontend/
```

## Current Status

Mini Projects 01 to 05 are completed, tested, and pushed to GitHub.

The repository currently demonstrates:

* Linux automation
* Git and GitHub collaboration workflow
* Dockerized REST API
* Docker Compose full-stack deployment
Upcoming projects will focus on artifact automation, Kubernetes, monitoring, Terraform, secrets management, and rollback strategies.
## Author

Yash Redkar



