#Importing OpenCv library
import cv2 

#Defining the video path
video_path = "C:\\Users\\HP\\Desktop\\test_vid.mp4"  #custamisable

#Creating an object
vid_capture = cv2.VideoCapture(video_path)

#To check if the video file was successfully opened
if not vid_capture.isOpened():
    print("Error: Unable to open the video file. Check the file path.")
else:
    # Getting Frame Rate info
    fps = vid_capture.get(cv2.CAP_PROP_FPS)
    print(f"Frames per second: {fps} ,FPS")

    # Get total frame count
    frame_count = vid_capture.get(cv2.CAP_PROP_FRAME_COUNT)
    print(f"Total frame count: {frame_count}")

# Read and display video frames
while vid_capture.isOpened():
    ret, frame = vid_capture.read()  # Reading frame
    
    if ret == True:
        cv2.imshow("Video Frame", frame)  # Display the frame

        # Wait for 20 ms, press 'q'key to exit video file
        key = cv2.waitKey(20) 
        
        if key == ord('q'):
            break
    else:
        break  

# Releasing the object 
vid_capture.release()
cv2.destroyAllWindows()
