from src._bones.components.data_ingestion import DataIngestion
from src._bones.entity.artifact_entity import DataIngestionArtifacts
from src._bones.entity.config_entity import DataIngestionConfig
from src._bones.configuration.mongodb_connection import MongoGridFSOperations
from src._bones.pipeline.training_pipeline import TrainingPipline

from src._bones.constants import *


if __name__ == '__main__':

    training=TrainingPipline()
    training.run_pipeline()
