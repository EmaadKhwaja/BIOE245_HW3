import os
from torchvision import datasets, transforms

# Set the path where the data was downloaded
data_dir = os.path.join(os.getcwd(), 'lgg-mri-segmentation')

# Define the data transformations
data_transforms = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Create the dataset
dataset = datasets.ImageFolder(data_dir, transform=data_transforms)