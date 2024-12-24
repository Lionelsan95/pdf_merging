# PDF Merger Tool

A Python-based PDF merger application designed with modularity, scalability, and performance in mind. Refactored using SOLID principles, this application is Dockerized for portability and ease of use.

---

## Features
- Merges multiple PDF files from a source folder into a single PDF file.
- Saves the merged PDF with a unique UUID filename in the target directory.
- Modular design adhering to SOLID principles for maintainability and scalability.
- Supports parallel processing for efficient handling of large datasets.
- Includes Docker and `docker-compose` for easy deployment.
- Automated unit and integration testing.

---

## Requirements
- Python 3.8 or later (for local execution)
- Docker and Docker Compose (for containerized execution)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/merge-pdfs.git
   cd merge-pdfs
   ```

2. (Optional) Install Python dependencies if running locally:
   ```bash
   pip install -r requirements.txt
   ```

3. Create environment variables in a `.env` file:
   ```plaintext
   SOURCE_FOLDER=path/to/source
   TARGET_FOLDER=path/to/target
   ```

4. Place your PDF files to merge in the `SOURCE_FOLDER` and ensure the `TARGET_FOLDER` exists.

---

## Usage

### Using Docker

#### Build the Docker Image:
```bash
make build
```

#### Run the Application:
```bash
make run
```

#### Start with Docker Compose:
```bash
make compose-up
```

#### Stop the Application:
```bash
make compose-down
```

#### Clean Generated Files:
```bash
make clean
```

---

### Running Locally

1. Ensure you have Python 3.8+ installed.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```

---

## Testing

### Run Tests Inside Docker:
```bash
make test
```

### Run Tests Locally:
```bash
pytest tests/
```

Tests include:
- **Unit Tests**: Verify individual components (e.g., file processing, merging logic).
- **Integration Tests**: Validate the entire pipeline from input to output.

---

## Project Structure
```
pdf-merger/
├── app.py               # Main application orchestrator
├── config.py            # Handles environment variable loading
├── logger.py            # Logger setup and configuration
├── pdf_processor.py     # Handles individual PDF processing
├── pdf_merger.py        # Handles merging PDFs
├── file_manager.py      # Manages file and directory operations
├── tests/               # Unit and integration tests
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker build configuration
├── docker-compose.yml   # Docker Compose configuration
├── Makefile             # Simplifies common tasks
├── data/                # Data directory
│   ├── source/          # Input PDFs
│   └── target/          # Output PDFs
└── README.md            # Project documentation
```

---

## Example Workflow

1. Place PDF files to merge in the `./data/source` folder.
2. Run the application using:
   ```bash
   make run
   ```
3. Check the `./data/target` folder for the merged PDF file.

---

## Environment Variables

The application uses the following environment variables:

| Variable       | Description                     | Default (Docker)        |
|----------------|---------------------------------|-------------------------|
| `SOURCE_FOLDER`| Path to input PDF folder        | `/app/data/source`      |
| `TARGET_FOLDER`| Path to output PDF folder       | `/app/data/target`      |

---

## Scaling the Application

For high-throughput use cases:
1. Use a message queue (e.g., RabbitMQ, Kafka) for asynchronous task handling.
2. Deploy multiple replicas of the application using a container orchestrator like Kubernetes.

---

## Troubleshooting

### Missing PDFs in the Source Folder
- Ensure the `SOURCE_FOLDER` path exists and contains valid PDF files.

### Docker Build Fails
- Verify that Docker is installed and running.
- Ensure `Dockerfile` and `requirements.txt` exist in the root directory.

### Tests Fail
- Verify the source folder has valid PDF files for integration tests.
- Ensure all dependencies are installed correctly.

---

## Contributions

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
