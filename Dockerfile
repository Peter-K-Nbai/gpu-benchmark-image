# Start from the NVIDIA CUDA base image
FROM python:3.10-bullseye

# Set up the working directory in the container
WORKDIR /app

# Install necessary tools including gcc
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python3 -m venv venv

# Upgrade pip in the virtual environment
RUN ./venv/bin/pip install --no-cache-dir --upgrade pip

# Install Python dependencies in the virtual environment
COPY requirements.txt .
RUN ./venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the PATH to use the virtual environment's Python and pip
ENV PATH="/app/venv/bin:$PATH"

# Expose the application port
EXPOSE 5000

# Start the application with Uvicorn
CMD ["uvicorn", "app:asgi_app", "--host", "0.0.0.0", "--port", "5000"]
