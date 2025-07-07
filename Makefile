# Docker Compose command
DC = docker-compose

# Default target
.PHONY: all
all: build up

# Build all images
.PHONY: build
build:
	@echo "Building Docker images..."
	$(DC) build

# Start the full stack (detached mode)
.PHONY: up
up:
	@echo "Starting all services..."
	$(DC) up -d

# Stop all containers (without removing them)
.PHONY: stop
stop:
	@echo "Stopping all services..."
	$(DC) stop

# Bring down the stack (remove containers, networks, etc.)
.PHONY: down
down:
	@echo "Removing all containers and networks..."
	$(DC) down

# View container logs
.PHONY: logs
logs:
	$(DC) logs -f

# Restart the entire stack
.PHONY: restart
restart: down up

# Clean up all volumes and networks (DANGEROUS!)
.PHONY: clean
clean:
	@echo "Removing all volumes and networks (clean)..."
	$(DC) down -v --remove-orphans

# Show running containers
.PHONY: ps
ps:
	$(DC) ps
