# Base Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Create source and target directories inside the container
RUN mkdir -p /app/data/source /app/data/target

# Default environment variables (can be overridden)
ENV SOURCE_FOLDER=/app/data/source
ENV TARGET_FOLDER=/app/data/target

# Default command to run the app
CMD ["python", "app.py"]
