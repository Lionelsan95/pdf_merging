from pathlib import Path

class FileManager:
    def __init__(self, logger):
        self.logger = logger

    def ensure_directory(self, directory: Path):
        """Ensures the directory exists."""
        if not directory.exists():
            directory.mkdir(parents=True, exist_ok=True)
            self.logger.info(f"Created directory: {directory}")

    def get_pdf_files(self, directory: Path):
        """Gets all PDF files in a directory."""
        pdf_files = sorted(directory.glob("*.pdf"))
        if not pdf_files:
            self.logger.error(f"No PDF files found in {directory}")
            raise ValueError(f"No PDF files found in {directory}")
        return pdf_files
