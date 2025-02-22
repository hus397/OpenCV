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

