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
    
def accuracy(outputs, label):
    try:
        _, pred=torch.max(outputs, dim=1)
        return torch.tensor(torch.sum(pred == label).item() / len(pred))
    except Exception as e:
        raise CustomException(e, sys)    
    

def get_default_gpu():
    try:
        if torch.cuda.is_available():
            return torch.device("cuda")
        else:
            return torch.device("cpu")
    except Exception as e:
        raise CustomException(e, sys)    
    
def to_device(data, device):
    try:
        if isinstance(data, (list, tuple)):
            return [to_device(x, device) for x in data]
        return data.to(device, non_blocking=True)
    except Exception as e:
        raise CustomException(e, sys) 

class DeviceDataLoader:
    def __init__(self, dl, device):

        self.dl = dl
        self.device = device

    def __iter__(self):

        for d in self.dl:
            yield to_device(d, self.device)

    def __len__(self):
        return len(self.dl)    
    
                   