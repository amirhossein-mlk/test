import cv2

img = cv2.imread('img.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
