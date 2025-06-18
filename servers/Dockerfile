# Use Python runtime
FROM python:3.9-slim

# Install Flask
RUN pip install flask

# Copy our server code
WORKDIR /app
COPY app.py .

# Tell Docker what env var to expect
ENV SERVER_ID=unknown

# Expose port
EXPOSE 5000

# Run the server
CMD ["python", "app.py"]
