.PHONY: all build-server-image run-servers run-load-balancer stop-all clean

SERVER_IMAGE_NAME = server-image
SERVER_PORTS = 5001 5002 5003 
NUM_SERVERS = 


all: build-server-image run-servers run-load-balancer


build-server-image:
	@echo "Building Docker image for the server..."
	docker build -t $(SERVER_IMAGE_NAME) .
	@echo "Server image '$(SERVER_IMAGE_NAME)' built successfully."


run-servers: stop-servers clean-servers
	@echo "Running $(NUM_SERVERS) server replicas..."
	@for i in $(seq 1 $(NUM_SERVERS)); do \
		HOST_PORT=$$(echo $(SERVER_PORTS) | cut -d' ' -f$$i); \
		SERVER_ID=$$i; \
		echo "Starting server-$$SERVER_ID on host port $$HOST_PORT..."; \
		docker run -d --name server-$$SERVER_ID -e SERVER_ID=$$SERVER_ID -p $$HOST_PORT:5000 $(SERVER_IMAGE_NAME); \
	done
	@echo "All server replicas started."
	docker ps -f ancestor=$(SERVER_IMAGE_NAME)


run-load-balancer:
	@echo "Starting the Load Balancer..."
	@echo "Ensure Python dependencies (Flask, requests) are installed in your virtual environment."
	python3 loadBalancer.py


stop-servers:
	@echo "Stopping server containers..."
	docker stop $$(docker ps -aq -f ancestor=$(SERVER_IMAGE_NAME)) 2>/dev/null || true
	@echo "Server containers stopped."


clean-servers:
	@echo "Removing stopped server containers..."
	docker rm $$(docker ps -aq -f ancestor=$(SERVER_IMAGE_NAME)) 2>/dev/null || true
	@echo "Stopped server containers removed."


clean: stop-servers clean-servers
	@echo "Project cleanup complete."
