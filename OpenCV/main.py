import cv2
cap = cv2.VideoCapture('video/1.mp4')

while True:
    success, img  = cap.read()
    cv2.imshow('img', img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break







