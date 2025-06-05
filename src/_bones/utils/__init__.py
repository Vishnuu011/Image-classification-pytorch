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


@torch.no_grad()
def evaluate(model, val_loader):
    try:
        model.eval()
        outputs=[model.validation_step(batch) for batch in val_loader]
        return model.validation_epoch_end(outputs)
    except Exception as e:
        raise CustomException(e, sys)      
    

def fit_trainer(
        epochs, 
        lr, 
        model, 
        train_data_loader, 
        val_data_loader,
        opt_fun=torch.optim.SGD, 
        grad_clip=GRAD_CLIP
    ):
    try:
        history=[]
        optimizer = opt_fun(params=model.parameters(), 
                            lr=lr, weight_decay=WEIGHT_DECAY)
        sched=torch.optim.lr_scheduler.OneCycleLR(optimizer=optimizer, 
                                                  max_lr=lr, epochs=epochs,
                                                  steps_per_epoch=len(train_data_loader)
                                                  )
        for epochs in range(epochs):
            model.train()
            train_losses = []
            for batch in train_data_loader:

                loss=model.training_step(batch)
                train_losses.append(loss)
                loss.backward()

                if grad_clip:
                    nn.utils.clip_grad_value_(model.parameters(), 
                                              clip_value=grad_clip)
                optimizer.step()
                optimizer.zero_grad()

                sched.step()
            result = evaluate(model, val_data_loader)
            result['train_loss'] = torch.stack(train_losses).mean().item()
            model.epoch_end(epochs, result)
            history.append(result)
        return history, result    
    except Exception as e:
        raise CustomException(e, sys)
    

def predict_img(img, model, device):
    try:
        x_img = to_device(img.unsqueeze(0), device)
        y_img = model(x_img)
        proba = torch.softmax(y_img, dim=1)
        probs, pred = torch.max(proba, dim=1)
        class_labels=['Oblique fracture', 'Spiral Fracture']
        predicted_class=class_labels[pred.item()]
        confidence=probs.item()*100
        return predicted_class, confidence
    except Exception as e:
        raise CustomException(e, sys)
    

#utils     