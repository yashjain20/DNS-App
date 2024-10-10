# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Flask and Requests
RUN pip install Flask requests

# Expose port 8080 for the User Server
EXPOSE 8080

# Command to run the User Server
CMD ["python", "user_server.py"]