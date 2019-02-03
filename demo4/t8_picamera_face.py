#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from picamera import PiCamera
import cv2
from time import sleep
import matplotlib.pyplot as plt

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture('/home/pi/dev/demo4/t8_image.jpg')
camera.stop_preview()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 

img = cv2.imread('t8_image.jpg') 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

plt.imsave('t8_face.png', img) 