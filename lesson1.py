import cv2

pikachu = cv2.imread('pika.png', cv2.IMREAD_COLOR)
cv2.imshow('pika', pikachu)

cv2.waitKey(0)
cv2.destroyAllWindows()

#three modes: cv2.IMREAD_COLOR and 1 both work when opening colour image
#cv2.IMREAD_GRAYSCALE and 0 both work 
#cv2.IMREAD_UNCHANGED and -1 both work#

import cv2

pikachu = cv2.imread('pika.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('pika', pikachu)

cv2.waitKey(0)
cv2.destroyAllWindows()

#three modes: cv2.IMREAD_COLOR and 1 both work when opening colour image
#cv2.IMREAD_GRAYSCALE and 0 both work 
#cv2.IMREAD_UNCHANGED and -1 both work