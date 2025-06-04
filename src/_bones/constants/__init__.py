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

MODEL_TRAINER_ARTIFACT_DIR : str = "model_trainer"
MODEL_NAME : str = "torch_model.pt"
BATCH_SIZE : int = 64
EPOCHS : int = 13
LEARNING_RATE : float = 0.001
GRAD_CLIP : float = 0.1
WEIGHT_DECAY : float = 1e-4
IN_CHANNELS: int = 3
OPTIMIZER = torch.optim.RMSprop
NUM_CLASSES :int = 6
TRANSFORM_OBJECT_NAME: str = "transform.pkl"