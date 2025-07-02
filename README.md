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

## Testing & Observations

Performance tests were conducted to evaluate the behavior of the load balancer under different conditions: balanced routing, scaling, fault tolerance, and sticky sessions.

### 🔹 A-1: Load Distribution (Round-Robin)

* **Test**: 10,000 requests sent to 3-server system.
* **Result**: Each server handled \~3333 requests.
* **Observation**: Round-robin effectively balanced the load, with slight variation due to response latency.

---

### 🔹 A-2: Scalability

* **Test**: Server count increased from 2 → 6.
* **Result**: Requests per server dropped proportionally.
* **Observation**: Demonstrated good horizontal scalability under stateless load distribution.

---

### 🔹 A-3: Fault Tolerance

* **Test**: One server instance was intentionally stopped mid-test.
* **Result**: Initial 5xx errors occurred.
* **Recovery**: Docker’s auto-restart restored the container, and service resumed.
* **Recommendation**: Implement retry-on-failure logic in the load balancer for smoother recovery.

---

### 🔹 A-4: Sticky Sessions (Hash-Based Routing)

* **Test**: Load balancer routed requests by hashing client IPs.
* **Result**: Same client consistently routed to the same server (sticky sessions).
* **Observation**: Imbalanced load under skewed traffic patterns.
* **Conclusion**: Use hashing only if session persistence is required. Round-robin is fairer under uniform traffic.

---

## Results and Raw Data

Explore the full results, charts, and architecture in the following files:

* 📊 [`docs/TEST_RESULTS.md`](./docs/TEST_RESULTS.md) — In-depth analysis and visuals
* 🕒 [`results/response_times.json`](./results/response_times.json) — Raw server response times
* 📈 [`results/requests_per_server.csv`](./results/requests_per_server.csv) — Server-wise request count

---

## Future Improvements

* Add automatic health checks to the load balancer
* Implement retry and backoff strategies for failed requests
* Introduce latency-aware or least-connection routing
* Visualize real-time metrics via Grafana or Prometheus
* Extend to a Kubernetes-based deployment for orchestration

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.












