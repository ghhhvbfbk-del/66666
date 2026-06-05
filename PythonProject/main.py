import cv2

img = cv2.imread('images/1.jpg')
img = cv2.putText(img, "Hello OpenCV", (506, 506), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), )


cv2.imshow("Output", img)
cv2.waitKey(0)

# Загружаем изображение
image = cv2.imread('original.jpg')







resized_image = cv2.resize(image, None, fx=50, fy=50, )







