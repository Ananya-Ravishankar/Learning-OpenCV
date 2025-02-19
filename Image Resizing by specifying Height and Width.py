import cv2
import numpy as np

#Readind the image
image = cv2.imread('C:\\Users\\HP\\Desktop\\test.jpg')  # Insert your image path here
cv2.imshow('Original Image', image)

#downscaling the image
down_width = 200
down_height = 100
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)

#upscaling the image 
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation=cv2.INTER_LINEAR)


cv2.imshow('Resized Down image', resized_down)
cv2.waitKey(20)
cv2.imshow('Resized Up image', resized_up)
cv2.waitKey(0)
cv2.destroyAllWindows()
