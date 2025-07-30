# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip \
 && pip install flask flask_sqlalchemy flask_migrate flask-wtf

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "run.py"]

