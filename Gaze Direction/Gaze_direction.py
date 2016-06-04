#Fabian implementation

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Video capture via webcam
cam = cv2.VideoCapture(-1)
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
	        # print(type(shape.part(1).x))
	        cv2.circle(frame,(shape.part(36).x,shape.part(36).y),2,(0,0,255))
	        cv2.circle(frame,(shape.part(39).x,shape.part(39).y),2,(0,0,255))
	        cv2.circle(frame,(shape.part(42).x,shape.part(42).y),2,(0,0,255))
	        cv2.circle(frame,(shape.part(45).x,shape.part(45).y),2,(0,0,255))
	        cv2.imshow('Video', frame)
	        if cv2.waitKey(1) & 0xFF == ord('q'):
	        	break
    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	faces1 = faceCascade1.detectMultiScale(gray, 1.1, 5)
    	for (x, y, w, h) in faces1:
		    eyes1 = eyecascade1.detectMultiScale(gray, 1.5, 6)
		    for (x1, y1, w1, h1 ) in eyes1:
				split = frame[y1:y1+h1,x1:x1+w1]
				split1=cv2.cvtColor(split, cv2.COLOR_BGR2GRAY)
				sobelx = cv2.Sobel(split1,cv2.CV_64F,1,0,ksize=5)
				sobely = cv2.Sobel(split1,cv2.CV_64F,0,1,ksize=5)
				sob = np.multiply(sobelx,sobely)
				minin = 100000
				minj=0
				mini=0
				print(sob.shape)
				for i in range(len(sob)/2):
					for j in range(len(sob)/2):
						if(sob[int(i+len(sob)/4)][int(j+len(sob)/4)]<minin):
							minin=gray[i][j]
							mini=i
							minj=j
							print(mini,minj)
				cv2.circle(frame,(x1+mini,y1+minj),1,(0,0,255))						
				cv2.line(frame,(x1+mini,y1+minj), (x1+2*mini-w1/2,y1+2*minj-h1/2),(255,0,0))
		# Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
