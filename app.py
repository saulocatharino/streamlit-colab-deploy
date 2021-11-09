import cvlib
import cv2
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

empty = st.empty()

cap = cv2.VideoCapture('face-demographics-walking-and-pause.mp4')
font = cv2.FONT_HERSHEY_SIMPLEX

ret = True
count = 0
while ret:
  count += 1
  ret, frame = cap.read()
  frame = cv2.resize(frame, None, fx=.5, fy=.5)
  faces, confidences = cvlib.detect_face(frame)

  for face in faces:
    face_img = frame[face[1]:face[3],face[0]:face[2]]
    label, confidence = cvlib.detect_gender(face_img, enable_gpu=False)
    classe = np.argmax(confidence)
    conf = confidence[classe]
    x1,y1,x2,y2 = face[0],face[1],face[2],face[3]
    cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),1,cv2.LINE_AA)
    cv2.putText(frame, label[classe], (x1,y1-20), font, .5, (0,255,0), 1, cv2.LINE_AA)
  empty.image(frame)
  
