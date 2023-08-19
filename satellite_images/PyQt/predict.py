import torch
from torchvision import transforms
# from torchvision.models.detection import

# import cv2

from PIL import Image

import warnings
warnings.filterwarnings('ignore')

# from ResNet import
from PyQt.ResNet import ResNet9, Sim_ResNet9

classes = ['agricultural', 'airplane', 'baseballdiamond', 'beach', 'buildings', 'chaparral', 'cloudy', 'denseresidential'
           'desert', 'forest', 'freeway', 'golfcourse', 'green_area', 'harbor', 'intersection', 'mediumresidential', 'mobilehomepark',
           'overpass', 'parkinglot', 'river', 'runway', 'sparseresidential', 'storagetanks', 'tenniscourt', 'water'
           ]

def get_device():
    device = torch.device('cpu') if torch.cuda.is_available() else torch.device('cpu')
    return device

def to_device(data, device):
    """ Move tensor into chosen device"""
    if isinstance(data, (list, tuple)):
        return [to_device(x, device) for x in data]
    return data.to(device, non_blocking=True)


def image_trans():
    stats = ([0.485, 0.456, 0.406], [0.229, 0.224, 0.2])

    img_trans = transforms.Compose([
        transforms.RandomCrop(64, padding=4, padding_mode='reflect'),
        transforms.RandomRotation(30),
        transforms.RandomHorizontalFlip(),
        transforms.Resize(64),
        transforms.ToTensor(),
        transforms.Normalize(*stats, inplace=True)

    ])

    return img_trans


def predict_images(img_path):
    model_cpu = to_device(Sim_ResNet9(3,25), get_device())
    model_cpu.load_state_dict(torch.load('./ResModel_FC.pth',
                                         map_location=torch.device('cpu')
                                         ))

    model_cpu.eval()
    torch.no_grad()
    image = Image.open(img_path).convert('RGB')
    img = image_trans()(image)
    # convert to a batch of 1
    uns_image_batch = to_device(img.unsqueeze(0), get_device())
    # get prediction from model
    training_batch_res = model_cpu(uns_image_batch)
    # pick index with highest probablity
    _, preds = torch.max(training_batch_res, dim=1)

    # retrieve the class label
    return classes[preds[0].item()], img_path


if __name__ == '__main__':

    print('loading params into model under CPU successfully')