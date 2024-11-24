# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory (where your code is) to the working directory in the container
COPY . .

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Install the Python dependencies from the requirements.txt file and unrar-free
RUN apt-get update && apt-get install -y unrar-free \
    && pip install --upgrade pip \
    && pip install -r requirements.txt

# Specify the command to run your application
CMD ["python3", "src/main.py"]