import os
import torch
from from_root import from_root

ARTIFACTS_DIR : str = "artifact"
SOURCE_DIR_NAME : str = 'src'
TRAIN_FOLDER_NAME : str = 'train'
TEST_FOLDER_NAME : str = 'test'

#Dataingestion constants

DATA_INGESTION_ARTIFACTS_DIR = "data_ingestion"

MONGO_ZIP_FILE_NAME = "Bones-data.zip"  # ZIP file name in GridFS
UNZIP_FOLDER_NAME = "unzip_data"
TRAIN_FOLDER_NAME = "train"
TEST_FOLDER_NAME = "test"

MONGO_DB_NAME = "mydatabase"

SCHEMA_YAML_PATH= os.path.join("config", "schema.yaml")