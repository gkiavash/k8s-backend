# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends gcc libc-dev libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the application code to the working directory
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port that the app runs on
#EXPOSE 8000

# Run the application with Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "k8s_backend.wsgi:application"]
