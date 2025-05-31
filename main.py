from src._bones.components.data_ingestion import DataIngestion
from src._bones.entity.artifact_entity import DataIngestionArtifacts
from src._bones.entity.config_entity import DataIngestionConfig
from src._bones.configuration.mongodb_connection import MongoGridFSOperations

from src._bones.constants import *



config = DataIngestionConfig()
mongo_ops = MongoGridFSOperations(uri=MONGO_URI, db_name=MONGO_DB_NAME)
ingestor = DataIngestion(config, mongo_ops)
artifact = ingestor.initiate_data_ingestion()