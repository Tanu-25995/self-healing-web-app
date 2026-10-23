
# Self-Healing Web Application

## Project Overview
This project demonstrates a simple web application that uses Docker health checks and a Python monitoring script to detect and recover from application health issues.

## Technologies Used
- Python
- Flask
- Docker
- Docker Health Check
- Python Docker SDK
- Linux (Ubuntu on WSL2 and AWS EC2)

## Project Structure
```text
self-healing-web-app/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
├── self_heal.py
├── .gitignore
└── README.md
```

## How It Works
1. The Flask web application runs inside a Docker container.
2. The `/health` endpoint reports the application's health.
3. Docker periodically checks the health endpoint.
4. The Python monitoring script checks the container's health status.
5. If the container becomes unhealthy, the script restarts it.

## Build the Docker Image
```bash
docker build -t self-healing-web-app .
```

## Run the Container
```bash
docker run -d --name self-healing-web-container --restart unless-stopped -p 5000:5000 self-healing-web-app
```

## Test the Application
Check the home page:
```bash
curl http://localhost:5000/
```

Check the health endpoint:
```bash
curl http://localhost:5000/health
```

## Run the Monitoring Script
Activate the Python virtual environment:
```bash
source venv/bin/activate
```

Run the self-healing script:
```bash
python self_heal.py
```

Press `Ctrl+C` to stop the monitoring script.

## Learning Outcomes
- Building a Python Flask application
- Creating Docker images and containers
- Configuring Docker health checks
- Monitoring container health
- Automating container recovery using Python

## AWS Deployment

- **Cloud Platform:** AWS EC2
- **Operating System:** Ubuntu Server 24.04
- **Containerization:** Docker
- **Web Server / Reverse Proxy:** Nginx
- **Application Port:** 5000
- **Public Access:** HTTP on port 80
- **Health Check:** `/health`
- **Self-Healing Monitor:** Python with Docker SDK

The Flask application runs inside a Docker container on an AWS EC2 instance. Nginx forwards incoming HTTP requests to the application. Docker health checks monitor application health, and a Python monitoring script checks the container status and attempts to restart it if it becomes unhealthy.

## CI/CD

A Jenkins pipeline builds the Docker image and tests the application health endpoint.


