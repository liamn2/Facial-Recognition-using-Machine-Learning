# Name: Liam Nutley
# Email: liam.nutley@yahoo.ie
# Problem 1

# Importing all required packages
import cv2
import numpy as np
import matplotlib.pyplot as plt
import PIL as pil


# Read in the cascade classifiers for face and eyes
face_cascade = cv2.CascadeClassifier(r'C:\Users\liamn\Desktop\data-engineer-takehome\haarcascade_frontalface_default.xml')

# create a function to detect face
def adjusted_detect_face(img):
	
	face_img = img.copy()
	
	face_rect = face_cascade.detectMultiScale(face_img,
											scaleFactor = 1.2,
											minNeighbors = 5)
	
	for (x, y, w, h) in face_rect:
		cv2.rectangle(face_img, (x, y),
					(x + w, y + h), (255, 255, 255), 10)\
		
	return face_img


# create a function to detect eyes
def detect_eyes(img):
	
	eye_img = img.copy()
	eye_rect = eye_cascade.detectMultiScale(eye_img,
											scaleFactor = 1.2,
											minNeighbors = 5)
	for (x, y, w, h) in eye_rect:
		cv2.rectangle(eye_img, (x, y),
					(x + w, y + h), (255, 255, 255), 10)	
	return eye_img

# Reading in the image and creating copies
img = cv2.imread(r'C:\Users\liamn\Desktop\data-engineer-takehome\picture.jpg')
img_copy1 = img.copy()
img_copy2 = img.copy()
img_copy3 = img.copy()

# Detecting the face
face = adjusted_detect_face(img_copy1)
plt.imshow(face)
# Saving the image
cv2.imwrite('face.jpg', face)