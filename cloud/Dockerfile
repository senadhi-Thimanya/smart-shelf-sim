# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy all cloud files
COPY . .

# Install Flask
RUN pip install flask

# Expose the port Flask will use
EXPOSE 5000

# Run the cloud API
CMD ["python", "cloud_api.py"]
