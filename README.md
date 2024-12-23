# PDF Merger Tool

A simple Python tool to merge multiple PDF files from a source folder into a single PDF file with a UUIDv4 filename in the target directory. Now Dockerized for portability and ease of use.

---

## Features
- Merges all PDF files in a specified source folder.
- Saves the merged PDF with a unique UUID filename in the target directory.
- Easy-to-configure via Docker or environment variables.
- Automated testing included.

---

## Requirements
- Python 3.8 or later
- Docker (if using the Dockerized setup)
- `PyPDF2` and `python-dotenv` Python libraries (if running locally)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/merge-pdfs.git
   cd merge-pdfs
