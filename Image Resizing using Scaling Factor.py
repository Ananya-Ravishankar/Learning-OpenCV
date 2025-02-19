import cv2
import numpy as np

#Reading the image
image_path = 'C:\\Users\\HP\\Desktop\\test.jpg'  #Insert your image path here
image = cv2.imread(image_path)

cv2.imshow('Original Image', image)

#Scaling Up the image 
scale_up_x = 1.5
scale_up_y = 1.5

#Scaling Down the image 
scale_down = 0.6

#Resize images
scaled_f_down = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(image, None, fx=scale_up_x, fy=scale_up_y, interpolation=cv2.INTER_LINEAR)

#Display resized images
cv2.imshow('Resized Down Image', scaled_f_down)
cv2.waitKey(20)
cv2.imshow('Resized Up image ', scaled_f_up)
cv2.waitKey(0)
cv2.destroyAllWindows()
