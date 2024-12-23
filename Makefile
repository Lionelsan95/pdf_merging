# Variables
DOCKER_IMAGE = pdf-merger
SOURCE_FOLDER = ./data/source
TARGET_FOLDER = ./data/target
TEST_FOLDER = ./tests

# Docker Commands
build:
	@echo "Building the Docker image..."
	docker build -t $(DOCKER_IMAGE) .

run:
	@echo "Running the Docker container..."
	docker run --rm -v $(SOURCE_FOLDER):/data/source -v $(TARGET_FOLDER):/data/target $(DOCKER_IMAGE)

test:
	@echo "Running automated tests inside Docker..."
	docker run --rm -v $(TEST_FOLDER):/app/tests $(DOCKER_IMAGE)

compose-up:
	@echo "Starting with docker-compose..."
	docker-compose up

compose-down:
	@echo "Stopping with docker-compose..."
	docker-compose down

clean:
	@echo "Cleaning up Docker environment..."
	docker system prune -af

# Testing Locally
local-test:
	@echo "Running local tests..."
	python -m unittest discover tests

help:
	@echo "Available commands:"
	@echo "  build          - Build the Docker image"
	@echo "  run            - Run the Docker container for PDF merging"
	@echo "  test           - Run automated tests inside Docker"
	@echo "  compose-up     - Start the application using docker-compose"
	@echo "  compose-down   - Stop the application using docker-compose"
	@echo "  clean          - Clean up unused Docker resources"
	@echo "  local-test     - Run local unit tests without Docker"
