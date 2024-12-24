import os
from pathlib import Path

class Config:
    @staticmethod
    def load_env():
        source_folder = os.getenv("SOURCE_FOLDER")
        target_folder = os.getenv("TARGET_FOLDER")
        if not source_folder or not target_folder:
            raise ValueError("SOURCE_FOLDER and TARGET_FOLDER must be set in the .env file.")
        return Path(source_folder), Path(target_folder)
