# Use the official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Expose port 53533 for the Authoritative Server
EXPOSE 53533

# Command to run the Authoritative Server
CMD ["python", "authoritative_server.py"]