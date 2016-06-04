import cv2
import sys

# Defining cascade variables
faceCascade1 = cv2.CascadeClassifier('../haarcascades/haarcascade_frontalface_alt2.xml')

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

frame_number = 0
flag = 0
last_x = 0
last_y = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    frame_number=frame_number+1
    if ret:
        if flag == 0:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces1:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                last_x = x
                last_y = y
                flag = 1

        else :
            flag = 0
            faces1 = faceCascade1.detectMultiScale(roi_gray, 1.1, 5)
            
            # Draw a rectangle around the faces
            for (x, y, w, h) in faces1:
                cv2.rectangle(frame, (last_x+x, last_y+y), (last_x+x+w, last_y+y+h), (0, 0, 255), 2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                last_x = last_x + x-10
                last_y = last_y + y-10
                flag = 1
            
        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
