# Mini Project 03: Dockerized To-Do API

## Project Overview

This mini project is a simple REST API for managing To-Do tasks.
The API is built using Node.js and Express and is containerized using Docker.

The project demonstrates how to build, run, tag, and push a Docker image to Docker Hub using semantic versioning.

## Features

* Create a new To-Do task
* Read all To-Do tasks
* Read a single To-Do task by ID
* Update a To-Do task
* Delete a To-Do task
* Health check endpoint
* Multi-stage Dockerfile
* Docker Hub image push with semantic version tag

## Tech Stack

* Node.js
* Express.js
* Docker
* Docker Hub
* Git
* GitHub

## API Endpoints

| Method | Endpoint     | Description        |
| ------ | ------------ | ------------------ |
| GET    | `/`          | API welcome route  |
| GET    | `/health`    | Health check route |
| GET    | `/todos`     | Get all todos      |
| GET    | `/todos/:id` | Get todo by ID     |
| POST   | `/todos`     | Create a new todo  |
| PUT    | `/todos/:id` | Update todo by ID  |
| DELETE | `/todos/:id` | Delete todo by ID  |

## Project Structure

```text
mini-project-03-dockerized-todo-api/
│
├── src/
│   └── server.js
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── package.json
├── package-lock.json
└── README.md
```

## How to Run Locally

Install dependencies:

```bash
npm install
```

Start the application:

```bash
npm start
```

The API will run on:

```text
http://localhost:3000
```

## How to Run with Docker

Build Docker image:

```bash
docker build -t dockerized-todo-api:v1.0.0 .
```

Run Docker container:

```bash
docker run -d -p 3000:3000 --name todo-api dockerized-todo-api:v1.0.0
```

Test API in browser:

```text
http://localhost:3000/health
http://localhost:3000/todos
```

Stop and remove container:

```bash
docker stop todo-api
docker rm todo-api
```

## Docker Hub Image

Docker Hub repository:

```text
yashredkar/dockerized-todo-api
```

Pull image:

```bash
docker pull yashredkar/dockerized-todo-api:v1.0.0
```

Run image from Docker Hub:

```bash
docker run -d -p 3000:3000 --name todo-api yashredkar/dockerized-todo-api:v1.0.0
```

## Docker Image Tags

| Tag      | Description              |
| -------- | ------------------------ |
| `v1.0.0` | Semantic version release |
| `latest` | Latest stable image      |

## Multi-Stage Dockerfile

This project uses a multi-stage Dockerfile.

Stage 1 installs production dependencies.
Stage 2 creates a lightweight final image for running the API.

This helps reduce the final Docker image size and keeps the container clean.

## Success Outcome

A working To-Do REST API containerized using Docker and publicly available on Docker Hub.

## Author

Yash Redkar
