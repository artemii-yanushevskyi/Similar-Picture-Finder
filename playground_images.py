from PIL import Image   
import numpy as np

def create_image():
    array = np.zeros([4,8,3], dtype=np.uint8)
    array[:,4:] = [255, 255, 0]
    img = Image.fromarray(array)
    img.save('image.png')

def read_image():
    img = Image.open('image.png')
    array = np.array(img)
    print(array)

read_image()