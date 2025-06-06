import torch
import torch.nn as nn
import torch.nn.functional as F
from src._bones.utils import accuracy


class ImageClassificationBase(nn.modules):

    def training_step(self, batch):
        
        image, labels=batch
        outputs=self(image)
        losses=F.cross_entropy(outputs, labels)
        return losses
    
    def validation_step(self, batch):

        image, label=batch
        outputs=self(image)
        losses=F.cross_entropy(outputs, label)
        accu=accuracy(outputs=outputs,
                      label=label)
        return {'val_loss ': losses.detach(), 'val_acc': accu}
    
    def validation_epoch_end(self, outputs):

        batch_loss=[x['val_loss']for x in outputs]
        epoch_loss=torch.stack(batch_loss).mean()
        batch_acc=[x['val_acc'] for x in outputs]
        epoch_acc=torch.stack(batch_acc).mean()
        return {'val_loss': epoch_loss.item(), 'val_acc': epoch_acc.item()}
    
    def epoch_end(self, epoch, result):
       
        print("Epoch [{}], train_loss: {:.4f}, val_loss: {:.4f}, val_acc: {:.4f}".format(
            epoch, result['train_loss'], result['val_loss'], result['val_acc']))
        

class VGGClassificationBase(ImageClassificationBase):
    def __init__(self, vgg_model):
        super().__init__()
        self.vgg = vgg_model

    def forward(self, xb):
        return self.vgg(xb)        