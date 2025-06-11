# Distributed Load Balancer Project

## Overview
This project implements a simple distributed web server system with a basic load balancer to distribute requests among multiple server replicas. The server and load balancer are containerized using Docker.

## Project Structure
- `server.py`: The backend Flask web server application.
- `load_balancer.py`: The Flask application acting as a load balancer.
- `Dockerfile`: Used to containerize the `server.py` application.
- `requirements.txt`: Lists the Python dependencies for the server.
- `Makefile`: Automates building Docker images and running the services.
- `README.md`: This file.

## Setup and Running the Application

### Prerequisites
- Docker Desktop (or Docker Engine on Linux) installed and running.
- Python 3.9+ (for running the load balancer locally and installing dependencies).
- `pip` for Python package management.

### Building the Server Image
To build the Docker image for the server:
```bash
make build-server-image