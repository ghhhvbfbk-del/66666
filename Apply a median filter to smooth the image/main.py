import cv2

# Загрузка изображения
image = cv2.imread('1.jpg.', 0)  # 0 для чёрно-белого изображения

# Применение медианного фильтра
median_blurred_image = cv2.medianBlur(image, 5)

# Отображение результата
cv2.imshow('Исходное изображение', image)
cv2.imshow('Медианно сглаженное изображение', median_blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()