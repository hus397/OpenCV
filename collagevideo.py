import cv2
import os
from PIL import Image


path = 'C:\\Users\\kruzi\\Desktop\\pythonone\\images'
os.chdir('C:\\Users\\kruzi\\Desktop\\pythonone\\images')
meanwidth = 0
meanheight = 0
numberofimages = len(os.listdir('.'))
for image in os.listdir('.'):
    img = Image.open(os.path.join(path, image))
    width,height = img.size
    meanwidth = meanwidth + width 
    meanheight = meanheight + height

meanwidth = meanwidth//numberofimages
meanheight = meanheight//numberofimages

print(meanwidth)
print(meanheight)

