# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier(r'path_to_haar_xml')
# create a function to detect face
def adjusted_detect_face(img):
	face_img = img.copy()
	face_rect = face_cascade.detectMultiScale(face_img, scaleFactor = 1.2, minNeighbors = 5)
	for (x, y, w, h) in face_rect:
		cv2.rectangle(face_img, (x, y), (x + w, y + h), (255, 255, 255), 10)
		return face_img
# create a function to detect eyes
def detect_eyes(img):
	eye_img = img.copy()
	eye_rect = eye_cascade.detectMultiScale(eye_img, scaleFactor = 1.2, minNeighbors = 5)
	for (x, y, w, h) in eye_rect:
		cv2.rectangle(eye_img, (x, y), (x + w, y + h), (255, 255, 255), 10)	
		return eye_img
# Reading in the image and creating copies
img = cv2.imread(r'path_to_image')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()
# Detecting the face
face = adjusted_detect_face(img_copy1)
plt.imshow(face)
# Saving the image
cv2.imwrite('test.jpg', face)
#######################################################################################
# YOLO object detection
import cv2 as cv
import numpy as np
import time

img = cv.imread('images/horse.jpg')
cv.imshow('window',  img)
cv.waitKey(1)

# Give the configuration and weight files for the model and load the network.
net = cv.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

ln = net.getLayerNames()
print(len(ln), ln)

# construct a blob from the image
blob = cv.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
r = blob[0, 0, :, :]

cv.imshow('blob', r)
text = f'Blob shape={blob.shape}'
cv.displayOverlay('blob', text)
cv.waitKey(1)

net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t = time.time()

cv.displayOverlay('window', f'forward propagation time={t-t0}')
cv.imshow('window',  img)
cv.waitKey(0)
cv.destroyAllWindows()
#####################################################################################

 

