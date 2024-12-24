# Variables
DOCKER_IMAGE = pdf-merger-app
DOCKER_CONTAINER = pdf-merger-container
SOURCE_FOLDER = ./data/source
TARGET_FOLDER = ./data/target

# Docker Commands
build:
	@echo "Building the Docker image..."
	docker build -t $(DOCKER_IMAGE) .

run:
	@echo "Running the Docker container..."
	docker run --rm -v $(SOURCE_FOLDER):/app/data/source -v $(TARGET_FOLDER):/app/data/target $(DOCKER_IMAGE)

test:
	@echo "Running unit tests inside Docker..."
	docker run --rm -v $(SOURCE_FOLDER):/app/data/source -v $(TARGET_FOLDER):/app/data/target $(DOCKER_IMAGE) pytest tests/

compose-up:
	@echo "Starting the application with docker-compose..."
	docker-compose up

compose-down:
	@echo "Stopping the application with docker-compose..."
	docker-compose down

clean:
	@echo "Cleaning up temporary files..."
	rm -rf $(TARGET_FOLDER)/*.pdf

docker-clean:
	@echo "Cleaning up Docker resources..."
	docker system prune -af

help:
	@echo "Available commands:"
	@echo "  build          - Build the Docker image"
	@echo "  run            - Run the Docker container for merging PDFs"
	@echo "  test           - Run unit tests inside the Docker container"
	@echo "  compose-up     - Start the application using docker-compose"
	@echo "  compose-down   - Stop the application using docker-compose"
	@echo "  clean          - Remove generated files"
	@echo "  docker-clean   - Remove unused Docker resources"
