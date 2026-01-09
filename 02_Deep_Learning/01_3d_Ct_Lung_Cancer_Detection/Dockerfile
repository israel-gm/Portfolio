FROM pytorch/pytorch:2.9.1-cuda13.0-cudnn9-runtime

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies commonly required by scientific Python
RUN apt-get update && apt-get install -y \
    git \
    curl \
    build-essential \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /usr/workspace

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install Python deps
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Default command (overridden by docker-compose, but safe)
CMD ["sleep", "infinity"]