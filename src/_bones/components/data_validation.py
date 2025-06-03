import os, sys
from src._bones.logger import *
from src._bones.exception import *
from src._bones.constants import *
from src._bones.utils import read_yaml_file
from src._bones.entity.artifact_entity import DataIngestionArtifacts,DataValidationArtifact
from src._bones.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, data_ingestion_artifact:DataIngestionArtifacts):

        try:
            self.data_ingestion_artifact=data_ingestion_artifact
            self._schema_config = read_yaml_file(file_path=SCHEMA_YAML_PATH)  
        except Exception as e:
            raise CustomException(e, sys)
        
    def count_classes(self, path):

        try:
            outcomes = os.listdir(path)
            status = len(outcomes) == len(self._schema_config['classes'])
            return status
        except Exception as e:
            raise CustomException(e, sys)  

    def initiate_data_validation(self):

        try:
            logging.info("data validation status.....")

            validation_error_msg = ''
            status=self.count_classes(
                path= self.data_ingestion_artifact.train_file_path
            )
            if not status:
                validation_error_msg += "class are missing in train data.."
            status=self.count_classes(
                path=self.data_ingestion_artifact.test_file_path
            )    
            if not status:
                validation_error_msg += "class are missing in test data ..."
            validation_status=len(validation_error_msg) == 0

            validation_artifact=DataValidationArtifact(
                validation_status=validation_status
            )
            logging.info(f"Validation status : {validation_status}")
            print(validation_status)
            return validation_artifact
        except Exception as e:
            raise CustomException(e, sys) 