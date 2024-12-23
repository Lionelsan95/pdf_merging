import os
import uuid
import logging
from pathlib import Path
from PyPDF2 import PdfMerger
from dotenv import load_dotenv

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load environment variables
load_dotenv()

# Get source and target directories from environment variables
SOURCE_FOLDER = os.getenv("SOURCE_FOLDER")
TARGET_FOLDER = os.getenv("TARGET_FOLDER")

# Verify that the source and target directories are set
if not SOURCE_FOLDER or not TARGET_FOLDER:
    logging.error("SOURCE_FOLDER and TARGET_FOLDER must be set in the .env file.")
    raise ValueError("SOURCE_FOLDER and TARGET_FOLDER must be set in the .env file.")

def merge_pdfs(source_folder: Path, target_folder: Path):
    # Ensure the source folder exists
    if not source_folder.exists():
        logging.error(f"The source folder '{source_folder}' does not exist.")
        raise FileNotFoundError(f"The source folder '{source_folder}' does not exist.")
    
    # Create the target folder if it doesn't exist
    target_folder.mkdir(parents=True, exist_ok=True)
    
    # Get a list of all PDF files in the source folder
    pdf_files = sorted(source_folder.glob('*.pdf'))
    if not pdf_files:
        logging.error("No PDF files found in the source folder.")
        raise ValueError("No PDF files found in the source folder.")
    
    # Initialize the PDF merger
    merger = PdfMerger()
    
    # Merge all PDF files
    for pdf_path in pdf_files:
        with pdf_path.open('rb') as pdf_file:
            merger.append(pdf_file)
            logging.info(f"Added {pdf_path.name} to the merger.")
    
    # Generate a UUIDv4 name for the final PDF
    final_pdf_name = f"{uuid.uuid4()}.pdf"
    final_pdf_path = target_folder / final_pdf_name
    
    # Write the merged PDF to the target directory
    with final_pdf_path.open('wb') as output_file:
        merger.write(output_file)
    merger.close()
    
    logging.info(f"PDFs merged successfully! Final file saved at: {final_pdf_path}")

if __name__ == "__main__":
    try:
        merge_pdfs(Path(SOURCE_FOLDER), Path(TARGET_FOLDER))
    except Exception as e:
        logging.error(f"An error occurred: {e}")
