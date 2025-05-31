import os
import sys
from zipfile import ZipFile
from src._bones.logger import logging
from src._bones.exception import CustomException
from src._bones.entity.config_entity import DataIngestionConfig
from src._bones.entity.artifact_entity import DataIngestionArtifacts
from src._bones.configuration.mongodb_connection import MongoGridFSOperations
from src._bones.constants import MONGO_ZIP_FILE_NAME
class DataIngestion:
    def __init__(self, config: DataIngestionConfig, mongo_fs: MongoGridFSOperations):
        self.config = config
        self.mongo_fs = mongo_fs

    def download_zip_from_mongo(self):
        """
        Download the zip file from MongoDB GridFS if it does not exist locally.
        """
        try:
            if not os.path.exists(self.config.zip_data_path):
                logging.info(f"Downloading {self.config.zip_data_path} from MongoDB GridFS...")
                self.mongo_fs.download_file(filename=self.config.zip_filename, output_path=self.config.zip_data_path)
                logging.info("Download complete.")
            else:
                logging.info(f"Zip file already exists at {self.config.zip_data_path}, skipping download.")
        except Exception as e:
            raise CustomException(e, sys) from e

    def unzip_data(self):
        """
        Unzip the downloaded file to the data_path, creating directories as needed.
        """
        try:

            os.makedirs(self.config.data_path, exist_ok=True)
            
            # Extract the zip file with safer approach
            with ZipFile(self.config.zip_data_path, 'r') as zip_ref:
                # List all files in the zip
                all_files = zip_ref.namelist()
                logging.info(f"Files in zip: {all_files[:5]}...")  # Log first 5 files
                
                # Extract files one by one with error handling
                for file_name in all_files:
                    try:
                        # Skip directories
                        if file_name.endswith('/'):
                            continue
                        
                        # Create directory structure if needed
                        target_path = os.path.join(self.config.data_path, file_name)
                        dir_name = os.path.dirname(target_path)
                        os.makedirs(dir_name, exist_ok=True)
                        
                        # Extract file
                        with zip_ref.open(file_name) as source, open(target_path, 'wb') as target:
                            target.write(source.read())
                    except Exception as file_error:
                        logging.warning(f"Skipping file {file_name}: {str(file_error)}")
                        continue
            
            logging.info(f"Unzipping completed at {self.config.data_path}")
            
            # Check what folders were actually created
            if os.path.exists(self.config.data_path):
                created_folders = os.listdir(self.config.data_path)
                logging.info(f"Created folders: {created_folders}")
                
            # Verify the extracted paths exist
            if not os.path.exists(self.config.train_path):
                logging.warning(f"Expected train path does not exist: {self.config.train_path}")
            if not os.path.exists(self.config.test_path):
                logging.warning(f"Expected test path does not exist: {self.config.test_path}")
                
        except Exception as e:
            logging.error(f"Error during unzipping: {str(e)}")
            raise CustomException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifacts:
        """
        Main method to perform data ingestion: download + unzip.
        Returns data ingestion artifacts with paths to train/test folders.
        """
        try:
            logging.info("Starting data ingestion process...")
            os.makedirs(self.config.data_ingestion_artifact_dir, exist_ok=True)

            self.download_zip_from_mongo()
            self.unzip_data()

            data_ingestion_artifacts = DataIngestionArtifacts(
                train_file_path=self.config.train_path,
                test_file_path=self.config.test_path,
                data_path=self.config.data_path
            )

            logging.info(f"Data ingestion artifacts: {data_ingestion_artifacts}")
            logging.info("Data ingestion completed successfully.")

            return data_ingestion_artifacts
        except Exception as e:
            raise CustomException(e, sys) from e


