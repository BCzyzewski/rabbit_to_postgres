FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (for better caching if your requirements don't change often)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .