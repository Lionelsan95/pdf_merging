# tests/test_merge_pdfs.py
import unittest
from pathlib import Path
from merge_pdfs import merge_pdfs

class TestMergePDFs(unittest.TestCase):
    def test_merge_pdfs(self):
        source = Path("tests/sample_source")
        target = Path("tests/sample_target")
        source.mkdir(parents=True, exist_ok=True)
        target.mkdir(parents=True, exist_ok=True)

        # Add test PDFs to source folder
        (source / "test1.pdf").touch()
        (source / "test2.pdf").touch()

        merge_pdfs(source, target)

        # Check if a PDF file is created in the target folder
        self.assertTrue(any(target.glob("*.pdf")))

if __name__ == "__main__":
    unittest.main()
