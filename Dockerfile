# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the worker code
COPY worker/worker.py .
COPY shared/ ./shared/

# Set the command to run the worker
CMD ["celery", "-A", "worker", "worker", "--loglevel=info"]