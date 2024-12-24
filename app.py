from pathlib import Path
from config import Config
from logger import Logger
from pdf_processor import PDFProcessor
from pdf_merger import PDFMergerService
from file_manager import FileManager
import multiprocessing
import tempfile

class App:
    def __init__(self):
        # Initialize logger
        self.logger = Logger.get_logger("PDFMergerApp")

        # Load configuration
        self.source_folder, self.target_folder = Config.load_env()

        # Initialize services
        self.file_manager = FileManager(self.logger)
        self.pdf_processor = PDFProcessor(self.logger)
        self.pdf_merger = PDFMergerService(self.logger)

    def process_and_merge(self):
        # Ensure directories exist
        self.file_manager.ensure_directory(self.source_folder)
        self.file_manager.ensure_directory(self.target_folder)

        # Get list of PDF files
        pdf_files = self.file_manager.get_pdf_files(self.source_folder)

        # Use temporary directory for processing
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir_path = Path(temp_dir)

            # Process PDFs in parallel
            with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
                results = pool.map(self.pdf_processor.read_pdf, pdf_files)

            # Filter valid PDFs
            valid_pdfs = [result for result in results if result is not None]

            # Merge PDFs
            self.pdf_merger.merge_pdfs(valid_pdfs, self.target_folder)


if __name__ == "__main__":
    try:
        app = App()
        app.process_and_merge()
    except Exception as e:
        logger = Logger.get_logger("PDFMergerApp")
        logger.error(f"An error occurred: {e}")
