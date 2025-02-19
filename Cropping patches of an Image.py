import cv2

#Custimisable
image_path = "C:\\Users\\HP\\Desktop\\test.jpg"
M = 76   # Customisable Patch height
N = 104  # Customisable Patch width

#Loading the image
img = cv2.imread(image_path)

#Create a copy for cropping
image_copy = img.copy()

#Image dimensions
img_height, img_width = img.shape[:2] #extracts only height and width

#NOTE: Make sure the 'saved_patches' folder already exists, or saving will fail.

#Loop through the image and extract patches
for y in range(0, img_height, M):
    for x in range(0, img_width, N):
        y1 = min(y + M, img_height)
        x1 = min(x + N, img_width)

        #cropping the patch
        tile = image_copy[y:y1, x:x1] #NumPy Array Slicing Method

        
        #draw rectangle around the patch on the original image
        cv2.rectangle(img, (x, y), (x1 - 1, y1 - 1), (0, 20, 0), 1) 

#Displaying the image with patches
cv2.imshow("Patched Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
