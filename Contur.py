import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img = cv2.imread(r'C:\Users\Liviu\Desktop\Donald_Trump.jpg')
#Convertim imaginea in alb-negru
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#Detectam fetele
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
for (x,y,w,h) in faces:
	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
#Afisam imaginea
cv2.imshow('Imagine: ', img)
cv2.waitKey()

#https://controlc.com/7eb2e38c