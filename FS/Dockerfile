# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask
RUN pip install Flask

# Expose port 9090 for the Fibonacci Server
EXPOSE 9090

# Command to run the Fibonacci Server
CMD ["python", "fibonacci_server.py"]