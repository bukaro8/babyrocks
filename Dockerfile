# Use an official Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Workdir inside the container
WORKDIR /app

# Install system dependencies (for PostgreSQL etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Expose the port Gunicorn will run on
EXPOSE 8000

# At container start:
# 1) collect static files
# 2) start Gunicorn server
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn babyrocks.wsgi:application --bind 0.0.0.0:8000"]
