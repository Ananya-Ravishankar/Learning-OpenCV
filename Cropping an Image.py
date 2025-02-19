import cv2

#Load the image
img = cv2.imread("C:\\Users\\HP\\Desktop\\test.jpg")


cv2.imshow("Original Image", img)

#Define the coordinates for cropping: [y_start:y_end, x_start:x_end]
cropped_image = img[80:280, 150:330] #customisable

#Display the cropped image
cv2.imshow("Cropped Image", cropped_image)
cv2.waitKey(0) #0 ms as there is only one image
cv2.destroyAllWindows()
