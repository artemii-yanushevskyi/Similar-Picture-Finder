from .process_input import get_folder_path
import os
from PIL import Image
import numpy as np

folder_path = get_folder_path()

def are_same_images(img1, img2, root=folder_path):
    image1 = Image.open(os.path.join(folder_path, img1))
    image2 = Image.open(os.path.join(folder_path, img2))
    array1 = np.array(image1)
    array2 = np.array(image2)
    if array1.size != array2.size:
        return False
    return (array1 == array2).all()


images = os.listdir(folder_path)
same_all = []
while any(images):
    image = images.pop(0)
    same = [image]
    different = []
    for i in range(len(images)):
        if are_same_images(image, images[i]):
            same.append(images[i])
        else:
            different.append(images[i])

    same_all.insert(-1, same)
    images = different

for sa in same_all:
    print(*sa)