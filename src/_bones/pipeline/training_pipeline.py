import os, sys
from src._bones.components.data_ingestion import DataIngestion
from src._bones.components.data_validation import DataValidation
from src._bones.entity.artifact_entity import(
    DataIngestionArtifacts,
    DataValidationArtifact
)
from src._bones.entity.config_entity import (
    DataIngestionConfig,
    DataValidationConfig
)

from src._bones.exception import *
from src._bones.configuration.mongodb_connection import MongoGridFSOperations
from src._bones.constants import *
from src._bones.logger import *

from dotenv import load_dotenv

load_dotenv()

MONGO_URI=os.getenv("MONGO_URI")
class TrainingPipline:
    def __init__(self):

        self.data_ingestion_config=DataIngestionConfig()
        
    def start_data_ingestion(self) -> DataIngestionArtifacts:

        try:
            mongo_ops = MongoGridFSOperations(uri=MONGO_URI, db_name=MONGO_DB_NAME)
            ingestor = DataIngestion(self.data_ingestion_config, mongo_ops)
            artifact = ingestor.initiate_data_ingestion()
            return artifact
        except Exception as e:
            raise CustomException(e,sys)   
        
    def start_data_validation(self, data_ingestion_artifact : DataIngestionArtifacts)-> DataValidationArtifact:
        try:
            logging.info("Entered the start_data_validation method of TrainPipeline class")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info("Exited the start_data_validation method of TrainPipeline class")
            return data_validation_artifact
        except Exception as e:
            raise CustomException(e,sys)
    

    def run_pipeline(self):

        try:
            ingestion_artifact=self.start_data_ingestion()
            validation_artifact=self.start_data_validation(
                data_ingestion_artifact=ingestion_artifact
            )
            return validation_artifact

        except Exception as e:
            raise CustomException(e, sys)     