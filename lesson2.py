import cv2

bg1 = cv2.imread(r'OpenCV\Lesson 2\bg.jpg', cv2.IMREAD_COLOR)
cv2.imshow('bg1', bg1)

bg2 = cv2.imread(r'OpenCV\Lesson 2\bg2.jpg', cv2.IMREAD_COLOR)
cv2.imshow('bg2', bg2)

cv2.waitKey(0)

bg3 = cv2.addWeighted(bg1, 0.5, bg2, 0.5, 0)
cv2.imshow('bg3', bg3)

cv2.waitKey(0)
cv2.destroyAllWindows()

#addition

import cv2

star = cv2.imread(r'OpenCV\Lesson 2\star.jpg', cv2.IMREAD_COLOR)
cv2.imshow('star', star)

dot = cv2.imread(r'OpenCV\Lesson 2\dot.jpg', cv2.IMREAD_COLOR)
cv2.imshow('dot', dot)

cv2.waitKey(0)

new = cv2.subtract(star, dot)
cv2.imshow('new', new)

cv2.waitKey(0)
cv2.destroyAllWindows()

#subtraction

import cv2

pikachu = cv2.imread('pika.png', cv2.IMREAD_COLOR)
cv2.imshow('pika', pikachu)
pikachunew = cv2.resize(pikachu, (200, 200))
cv2.imshow('pika', pikachunew)

cv2.waitKey(0)
cv2.destroyAllWindows()

#resize