import  sys
import torch
import yaml
import torch.nn as nn
from src._bones.exception import CustomException
from torch.optim.lr_scheduler import StepLR
from src._bones.constants import *

def read_yaml_file(file_path: str) -> dict:
    try:
        with open(file_path, "rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e, sys) from e