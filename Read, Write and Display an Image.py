#Program to Read, Write and Display an Imgae File using OpenCV
import cv2

# Define the image path (Use direct string)
image_path = "C:\\Users\\HP\\Desktop\\test.jpg"  # Path  to be customised

# Read the image in different modes
image_color = cv2.imread(image_path, cv2.IMREAD_COLOR)       # Color image
image_unchanged = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)  # Unchanged
image_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)    # Grayscale image

#Display the images 
cv2.imshow("Color Image", image_color)
cv2.imshow("Unchanged Image", image_unchanged)
cv2.imshow("Grayscale Image", image_gray)

# Save the images with different names
cv2.imwrite("C:\\Users\\HP\\Desktop\\output_color.jpg", image_color)
cv2.imwrite("C:\\Users\\HP\\Desktop\\output_unchanged.jpg", image_unchanged)
cv2.imwrite("C:\\Users\\HP\\Desktop\\output_gray.jpg", image_gray)


print("Images saved successfully on the Desktop.")

# Wait for user to press a key
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()
