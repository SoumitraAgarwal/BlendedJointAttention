# Facial landmark detection

import cv2
import numpy as np
import dlib 

# Video capture via webcam
cam = cv2.VideoCapture('../Test/test.mp4')
cam.set(3,640)
cam.set(4,480)
video_capture = cam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')

while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	if ret:
		dets = detector(frame, 1)
		for k, d in enumerate(dets):
		    # Get the landmarks/parts for the face in box d.
			shape = predictor(frame, d)
			for i in range(68):
				cv2.circle(frame,(shape.part(i).x,shape.part(i).y),2,(0,0,255))
	# Display the resulting frame
	cv2.imshow('Video', frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
	    break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()