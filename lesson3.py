import cv2

pikachu = cv2.imread('pika.png', cv2.IMREAD_COLOR)
cv2.imshow('pika', pikachu)
grey_image = cv2.cvtColor(pikachu, cv2.COLOR_BGR2GRAY)
cv2.imshow('pika', grey_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

#color_bgr2rgb (allcaps) bgr - blue green red; #colorbgr2hsv (all caps) hsv - hue saturation value
#you can do between all formats