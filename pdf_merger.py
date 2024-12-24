from PyPDF2 import PdfMerger
from pathlib import Path
import uuid

class PDFMergerService:
    def __init__(self, logger):
        self.logger = logger

    def merge_pdfs(self, pdf_contents, output_folder: Path):
        """Merge PDFs from provided content and save to output folder."""
        merger = PdfMerger()
        for pdf_name, pdf_content in pdf_contents:
            temp_file_path = output_folder / pdf_name
            with temp_file_path.open('wb') as temp_file:
                temp_file.write(pdf_content)
            merger.append(str(temp_file_path))
            self.logger.info(f"Added {pdf_name} to merger.")

        # Generate final PDF
        final_pdf_name = f"{uuid.uuid4()}.pdf"
        final_pdf_path = output_folder / final_pdf_name
        with final_pdf_path.open('wb') as output_file:
            merger.write(output_file)
        merger.close()

        self.logger.info(f"Merged PDF saved to {final_pdf_path}")
        return final_pdf_path
