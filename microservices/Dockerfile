FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Expose the port for gRPC
EXPOSE 50051

# Run the CRUD service
CMD ["python", "main.py"]
