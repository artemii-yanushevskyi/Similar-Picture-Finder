#! env/bin/python
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

img = Image.open('tests/test_same/image 1.png')
array1 = np.array(img)
print(array1[3,3])
img = Image.open('tests/test_same/image 1 duplicate.png')
array2 = np.array(img)
array2[3,3] = [255]*3 + [255] # last is opacity 0 - transparent 255 - opaque
img = Image.fromarray(array2)
img.save('tests/test_same/image 2 appears like 1 but different.png')
print((array1 == array2).all())

