# Use a lightweight CUDA image with Python
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04


# Install Python, pip, and necessary libraries
RUN apt-get update && apt-get install -y python3 python3-pip

# Set up the working directory and copy dependencies
WORKDIR /app
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose the port for the application
EXPOSE 5000

# Start the app with Uvicorn
CMD ["uvicorn", "app:asgi_app", "--host", "0.0.0.0", "--port", "5000"]
