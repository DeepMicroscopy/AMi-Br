from torch.utils.data import Dataset
import os
from PIL import Image
import numpy as np
import cv2

# Define dataset class
class AMFDataset(Dataset):
    def __init__(self, root_dir, ids:list, transform=None):
        """
        Args:
            root_dir (string): Directory with all the images.
            transform (callable, optional): Optional transform to be applied on a sample.
        """
        self.root_dir = root_dir
        self.transform = transform
        self.classes = [x for x in os.listdir(root_dir) if '.' not in x]
        self.images = []
        disregard=[]
        for cls in self.classes:
            class_dir = os.path.join(root_dir, cls)
            if '.' in class_dir:
                continue
            for img in os.listdir(class_dir):
                if '.DS' in img:
                    continue
                uid = int(img.split('_')[-1][:-4])
                if ids is not None and img.split(os.sep)[-1] not in ids: # select for train/test
                    continue
                
                self.images.append((os.path.join(class_dir, img), cls))
        print(self.classes)
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path, label = self.images[idx]
#        pillow_image = Image.open(img_path).convert("RGB")
#        image = np.array(pillow_image)

        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        if self.transform:
            image = self.transform(image=image)['image']
        
#        print(image)
        # Get label as index of the class name
        label_idx = self.classes.index(label)
        return image, label_idx