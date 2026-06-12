# Mini Project 05: Docker Compose Full-Stack App

## Project Overview

This mini project demonstrates a three-container full-stack application using Docker Compose.

The application consists of:

* Nginx frontend container
* Flask backend API container
* PostgreSQL database container

All services are defined in a single `docker-compose.yml` file and can be started using one command.

The project also demonstrates Docker networking, service dependency management, health checks, environment-based configuration, and persistent database storage using Docker volumes.

## Architecture

```text
Browser
   |
   v
Nginx Frontend Container
   |
   v
Flask Backend API Container
   |
   v
PostgreSQL Database Container
   |
   v
Docker Volume for Persistent Data
```

## Tech Stack

* Docker
* Docker Compose
* Nginx
* Python Flask
* PostgreSQL
* Docker Volumes
* Docker Bridge Network

## Project Structure

```text
mini-project-05-docker-compose-full-stack-app/
│
├── docker-compose.yml
├── .env.example
├── .gitignore
├── README.md
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── frontend/
    ├── index.html
    └── nginx.conf
```

## Services

| Service  | Container Name           | Technology | Port            |
| -------- | ------------------------ | ---------- | --------------- |
| Frontend | `student-notes-frontend` | Nginx      | `8080:80`       |
| Backend  | `student-notes-backend`  | Flask      | `5000:5000`     |
| Database | `student-notes-db`       | PostgreSQL | `5432` internal |

## Features

* Full-stack app using 3 containers
* Nginx serves frontend UI
* Nginx reverse proxies API requests to Flask backend
* Flask backend connects to PostgreSQL
* PostgreSQL stores notes permanently
* Docker volume persists database data
* Custom Docker bridge network connects services
* Health checks for backend and database
* Restart policy using `restart: unless-stopped`
* Environment variables managed through `.env`

## Environment Configuration

Create a `.env` file using `.env.example`:

```bash
cp .env.example .env
```

Example variables:

```env
POSTGRES_DB=notesdb
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

DB_HOST=db
DB_PORT=5432
DB_NAME=notesdb
DB_USER=postgres
DB_PASSWORD=postgres

BACKEND_PORT=5000
FRONTEND_PORT=8080
```

## Run the Application

Start the full-stack application:

```bash
docker compose up --build -d
```

Open the frontend:

```text
http://localhost:8080
```

Open backend health check:

```text
http://localhost:5000/api/health
```

Expected backend health response:

```json
{
  "database": "connected",
  "service": "student-notes-api",
  "status": "healthy"
}
```

## Useful Docker Compose Commands

Check running containers:

```bash
docker compose ps
```

View backend logs:

```bash
docker compose logs backend
```

View frontend logs:

```bash
docker compose logs frontend
```

View database logs:

```bash
docker compose logs db
```

Stop containers:

```bash
docker compose down
```

Restart containers:

```bash
docker compose up --build -d
```

## Data Persistence

PostgreSQL data is stored in a named Docker volume:

```text
student_notes_postgres_data
```

Check Docker volumes:

```bash
docker volume ls
```

Persistence test:

1. Start the app.
2. Add a note from the frontend.
3. Stop containers using:

```bash
docker compose down
```

4. Start again using:

```bash
docker compose up --build -d
```

5. Open the frontend again.

The previously added note should still be visible. This proves PostgreSQL data persistence through Docker volumes.

## Docker Network

All services communicate through a custom Docker bridge network:

```text
student_notes_network
```

The frontend communicates with the backend using the Docker service name:

```text
backend:5000
```

The backend communicates with PostgreSQL using the Docker service name:

```text
db:5432
```

## Success Outcome

A multi-tier application running with one command:

```bash
docker compose up --build -d
```

This project demonstrates:

* Docker Compose orchestration
* Multi-container application deployment
* Nginx reverse proxy
* Flask API backend
* PostgreSQL database integration
* Persistent database volume
* Container networking
* Health checks and restart policies

## Author

Yash Redkar
