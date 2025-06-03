import cv2
cap = cv2.VideoCapture(0)
while True:
    ket,img = cap.read()
    cv2.imshow('frame',img)
    cv2.waitKey(1)