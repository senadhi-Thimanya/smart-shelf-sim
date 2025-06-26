# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy edge service scripts into the container
COPY . .

# Install required libraries (requests for HTTP client)
RUN pip install requests

# Default command to run (you can change this)
CMD ["python", "shelf_status_service.py"]
