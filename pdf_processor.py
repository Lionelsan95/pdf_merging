from pathlib import Path

class PDFProcessor:
    def __init__(self, logger):
        self.logger = logger

    def read_pdf(self, pdf_path: Path):
        """Read a PDF file and return its content."""
        try:
            with pdf_path.open('rb') as pdf_file:
                self.logger.info(f"Processing {pdf_path.name}")
                return pdf_path.name, pdf_file.read()
        except Exception as e:
            self.logger.error(f"Error reading {pdf_path}: {e}")
            return None
