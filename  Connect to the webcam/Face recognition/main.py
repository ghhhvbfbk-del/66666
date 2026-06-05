import  cv2

img  = cv2.imread('3.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

faces  =  cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


recults  =  faces.detectMultiScale(gray, scaleFactor=2, minNeighbors= 4)

for (x, y, w, h) in recults:
     cv2.rectangle( img,(x, y), (x  + w, y + h), (0, 0, 0), thickness=3 )

cv2.imshow('img',img)
cv2.waitKey(0)

