# Use the official Python image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose a port (if necessary; not needed for your script but can be useful for extensions)
# EXPOSE 8000

# Define environment variables (optional; good for defaults)
ENV SOURCE_FOLDER=/data/source
ENV TARGET_FOLDER=/data/target

# Create folders for source and target files
RUN mkdir -p /data/source /data/target

# Define the default command to run the script
CMD ["python", "merge_pdfs.py"]
