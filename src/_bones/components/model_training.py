import os, sys
import numpy as np
import joblib

from src._bones.logger import *
from src._bones.exception import *
from src._bones.utils import *
from src._bones.entity.artifact_entity import *
from src._bones.entity.config_entity import *

from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader
from torch.utils.data import random_split
import torchvision.transforms as tt

from typing import Any, Tuple
import mlflow
import mlflow.pytorch



class ModelTrainer:

    def __init__(self, data_ingestion_artifact:DataValidationArtifact,
                 model_trainer_config: ModelTrainerConfig):
        
        try:
            self.data_ingestion_arifact=data_ingestion_artifact
            self.model_trainer_config=model_trainer_config
        except Exception as e:
            raise CustomException(e ,sys)
        
    def pytorch_metric_tracking_mlflow(self) -> None:

        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)    
        
    def get_data_loader(self) -> Tuple[Any, Any]:

        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)    
        
    def get_model(self) -> Any:

        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)   
        
    def load_to_cpu_else_gpu(self) -> torch.device:

        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)   

    def train_model(self) -> Any:

        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)     
        
    def initiate_model_trainer(self) -> ModelTrainerArtifacts:
        try:
            pass
        except Exception as e:
            raise CustomException(e, sys)    