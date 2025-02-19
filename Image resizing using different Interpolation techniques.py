import cv2
import numpy as np

#Reading the image
image_path = 'C:\\Users\\HP\\Desktop\\test.jpg'  #Insert your image path here
image = cv2.imread(image_path)

#Scaling factor
scale_down = 0.6

#Scaling down the image using different interpolation techniques
res_inter_nearest = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_NEAREST)
res_inter_linear = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
res_inter_area = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_AREA)
res_inter_cubic = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_CUBIC)

#Concatenate images 
horizontal_concat = np.concatenate((res_inter_nearest, res_inter_linear, res_inter_area, res_inter_cubic), axis=1)

#Display the concatenated image
cv2.imshow('INTER_NEAREST :: INTER_LINEAR :: INTER_AREA :: INTER_CUBIC', horizontal_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()
