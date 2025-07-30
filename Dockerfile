# Use official Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install Python dependencies from requirements.txt
RUN pip install --upgrade pip \
 && pip install -r requirements.txt

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "run.py"]

