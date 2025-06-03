
from dataclasses import dataclass
from datetime import datetime
import os
from from_root import from_root
from src._bones.constants import *

@dataclass
class DataIngestionConfig:
    timestamp: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
    data_ingestion_artifact_dir: str = os.path.join(from_root(), ARTIFACTS_DIR, DATA_INGESTION_ARTIFACTS_DIR)
    zip_filename: str = MONGO_ZIP_FILE_NAME
    zip_data_path: str = os.path.join(data_ingestion_artifact_dir, MONGO_ZIP_FILE_NAME)
    data_path: str = os.path.join(data_ingestion_artifact_dir, UNZIP_FOLDER_NAME)
    extracted_folder_name: str = "Bones-data"  # Name of the folder inside the zip
    train_path: str = os.path.join(data_path, extracted_folder_name, TRAIN_FOLDER_NAME)
    test_path: str = os.path.join(data_path, extracted_folder_name, TEST_FOLDER_NAME)


@dataclass
class DataValidationConfig:
    schema_file_path = os.path.join("config", "schema.yaml")