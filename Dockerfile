FROM python:3.10-slim-buster

WORKDIR /app

COPY . /app

RUN ls -l /app/requirements.txt
RUN cat /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "server.py"]