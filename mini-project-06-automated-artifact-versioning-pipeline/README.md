# Mini Project 06: Automated Artifact Versioning Pipeline

## Project Overview

This mini project demonstrates an automated artifact versioning and release pipeline using GitHub Actions, Docker, Docker Hub, semantic versioning, and GitHub Releases.

The goal of this project is to automate the complete release process. Whenever a version tag is pushed to GitHub, the pipeline automatically builds a Docker image, tags it with both the semantic version and the git commit SHA, pushes the image to Docker Hub, generates release notes, uploads a changelog artifact, and creates a GitHub Release.

## Problem Statement

In real-world DevOps workflows, application releases must be versioned, traceable, and repeatable. Manual Docker image tagging and release creation can cause mistakes, missing changelogs, and confusion about which code version is deployed.

This project solves that problem by automating the release process using Git tags and GitHub Actions.

## Architecture

```text
Developer
   |
   | Push Git Tag: mp06-v1.0.0
   v
GitHub Repository
   |
   v
GitHub Actions Workflow
   |
   | Build Docker Image
   | Tag Image with:
   |   - v1.0.0
   |   - sha-<commit-sha>
   |   - latest
   |
   v
Docker Hub
   |
   v
GitHub Release with Changelog
```

## Tech Stack

* Git
* GitHub
* GitHub Actions
* Docker
* Docker Hub
* Python Flask
* Semantic Versioning
* Release Automation

## Project Structure

```text
mini-project-06-automated-artifact-versioning-pipeline/
│
├── app.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .dockerignore
```

Workflow file:

```text
.github/workflows/artifact-versioning.yml
```

## Application Details

The application is a simple Flask API that exposes the following endpoints:

| Endpoint   | Description                                       |
| ---------- | ------------------------------------------------- |
| `/`        | Shows application status, version, and commit SHA |
| `/health`  | Health check endpoint                             |
| `/version` | Displays the running app version and commit SHA   |

## Docker Image

Docker Hub repository:

```text
yashredkar/artifact-versioning-api
```

Generated image tags:

```text
yashredkar/artifact-versioning-api:v1.0.0
yashredkar/artifact-versioning-api:sha-<commit-sha>
yashredkar/artifact-versioning-api:latest
```

## GitHub Actions Workflow

The workflow runs when a tag matching the following pattern is pushed:

```text
mp06-v*.*.*
```

Example tag:

```text
mp06-v1.0.0
```

When this tag is pushed, GitHub Actions automatically performs the following steps:

1. Checks out the source code
2. Extracts the semantic version from the Git tag
3. Extracts the short Git commit SHA
4. Generates release notes using recent Git commits
5. Logs in to Docker Hub using GitHub repository secrets
6. Builds the Docker image
7. Pushes the Docker image to Docker Hub with multiple tags
8. Uploads release notes as a workflow artifact
9. Creates a GitHub Release automatically

## Required GitHub Secrets

The following repository secrets are required for Docker Hub authentication:

| Secret Name          | Description                      |
| -------------------- | -------------------------------- |
| `DOCKERHUB_USERNAME` | Docker Hub username              |
| `DOCKERHUB_TOKEN`    | Docker Hub personal access token |

These secrets are added in:

```text
GitHub Repository → Settings → Secrets and variables → Actions
```

## Local Build and Run

Build the Docker image locally:

```bash
docker build -t artifact-versioning-api:local .
```

Run the container:

```bash
docker run -d -p 8081:8080 --name artifact-api artifact-versioning-api:local
```

Open in browser:

```text
http://localhost:8081
```

Health check:

```text
http://localhost:8081/health
```

Version endpoint:

```text
http://localhost:8081/version
```

Stop and remove the container:

```bash
docker stop artifact-api
docker rm artifact-api
```

## Automated Release Process

Create a new semantic version tag:

```bash
git tag mp06-v1.0.0
```

Push the tag:

```bash
git push origin mp06-v1.0.0
```

This triggers the GitHub Actions pipeline.

## Successful Outcome

After the workflow completes successfully:

* Docker image is built automatically
* Docker image is pushed to Docker Hub
* Image is tagged with semantic version
* Image is tagged with short commit SHA
* Latest tag is updated
* Changelog artifact is generated
* GitHub Release is created automatically

## Verification

Docker Hub should show:

```text
yashredkar/artifact-versioning-api:v1.0.0
yashredkar/artifact-versioning-api:sha-<commit-sha>
yashredkar/artifact-versioning-api:latest
```

GitHub Releases should show:

```text
Mini Project 06 Release v1.0.0
```

## What I Learned

Through this project, I learned how to:

* Use Git tags to trigger release workflows
* Automate Docker image builds using GitHub Actions
* Push Docker images to Docker Hub from CI/CD
* Use semantic versioning for release management
* Track releases using commit SHA tags
* Create GitHub Releases automatically
* Generate changelogs during CI/CD execution
* Store sensitive credentials securely using GitHub Secrets

## Real-World Use Case

This pipeline is useful in production DevOps environments where every release must be traceable and repeatable. By tagging every release with both a semantic version and commit SHA, teams can identify exactly which code version is running in production and roll back safely if needed.

## Author

Yash Redkar
