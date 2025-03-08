import cv2

pikachu = cv2.imread('pika.png', cv2.IMREAD_COLOR)
cv2.imshow('pika', pikachu)
grey_image = cv2.cvtColor(pikachu, cv2.COLOR_BGR2GRAY)
cv2.imshow('pika', grey_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#color_bgr2rgb (allcaps) bgr - blue green red; #colorbgr2hsv (all caps) hsv - hue saturation value
#you can do between all formats

#erosion of image

import cv2
import numpy as np

pikachu1 = cv2.imread('pika.png', cv2.IMREAD_COLOR)

kernel = np.ones((5, 5), np.uint8)

eroded = cv2.erode(pikachu1, kernel)

cv2.imshow('pika', pikachu1)
cv2.imshow('pikaeroded', eroded)

cv2.waitKey(0)
cv2.destroyAllWindows()

#blurring of image
#gaussian blur, median blur, bilateral blur

pikachu2 = cv2.imread('pika.png', cv2.IMREAD_COLOR)
gaussianblurred = cv2.GaussianBlur(pikachu2, (5,5), 0)
medianblurred = cv2.medianBlur(pikachu2, 5)
bilateralblurred = cv2.bilateralFilter(pikachu2, 21, 9, 200, 200)

cv2.imshow('pika', pikachu2)
cv2.imshow('gaussianblurred', gaussianblurred)
cv2.imshow('medianblurred', medianblurred)
cv2.imshow('bilateralblurred', bilateralblurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

pika = cv2.imread('pika.png', cv2.IMREAD_COLOR)

cv2.imshow('pika3', pika)

startpoint = (50,30)
endpoint = (60,10)
linethickness = 5
linecolour = (150, 150, 150)
line = cv2.line(pika, startpoint, endpoint, linecolour, linethickness)
cv2.imshow('line', line)
#rectangle
startpoint2 = (50,50)
endpoint2 = (100,100)
rect = cv2.rectangle(pika, startpoint2, endpoint2, linecolour, linethickness)
cv2.imshow('rect', rect)
#if you want the rectangle to be filled with a colour, make rect thickness as -1 (applies for all cases)
centre = (100,200)
radius = 40
thickness2 = -1
circle = cv2.circle(pika, centre, radius, linecolour, thickness2)
cv2.imshow('circle', circle)

font = cv2.FONT_HERSHEY_SIMPLEX
colour = (150, 150, 150)
pos = (200, 200)
thickness3 = 3
fontscale = 1
text = cv2.putText(pika, 'Hello!', pos, font, fontscale, colour, thickness3, cv2.LINE_AA)
cv2.imshow('text', text)

cv2.waitKey(0)
cv2.destroyAllWindows()



