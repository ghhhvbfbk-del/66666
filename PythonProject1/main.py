import cv2
import  cv2 as cv
import numpy as np
import  os
import tensorflow as tf
import  pickle

from cv2.data import haarcascade
from  keras_facenet import  FaceNet
import   tensorflow  as  tf
from sklearn.preprocessing import LabelEncoder




os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


facenet = FaceNet()
faces_embeddings = np.load("faces_embeddings_done_4classes (2).npz")
Y =faces_embeddings['arr_1']
encoder = LabelEncoder()
encoder.fit(Y)
haarcascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


model =  pickle.load(open("svm_model_160x160.pkl", 'rb'))

cap = cv2.VideoCapture(0)

while cap.isOpened():

    _, frame = cap.read()
    rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    gray_img = cv.cvtColor(rgb_img, cv.COLOR_BGR2GRAY)
    faces = haarcascade.detectMultiScale(gray_img, 1.3, 5)
    for x, y, w, h in faces:
        img = rgb_img[y:y + h, x:x + w]
        img = cv.resize(img, (160, 160))  # 1x160x160x3
        img = np.expand_dims(img, axis=0)
        ypred = facenet.embeddings(img)
        face_name = model.predict(ypred)
        final_name = encoder.inverse_transform(face_name)[0]
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 255), 10)
        cv.putText(frame, str(final_name), (x, y - 10), cv.FONT_HERSHEY_SIMPLEX,
                   1, (0, 0, 255), 3, cv.LINE_AA)

    cv.imshow("face Recognition", frame)
    if cv.waitKey(1) & ord('q') == 27:
     break

cap.release()
cv.destroyAllWindows()