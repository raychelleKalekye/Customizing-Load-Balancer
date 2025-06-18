FROM python:3.9-slim

# Install curl + Docker CLI
RUN apt-get update && \
    apt-get install -y docker.io curl && \
    pip install flask

WORKDIR /app
COPY load_balancer.py .

EXPOSE 5000

CMD ["python", "load_balancer.py"]
