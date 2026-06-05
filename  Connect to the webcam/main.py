import cv2

# Создаём объект захвата видео с камеры
cap = cv2.VideoCapture(0)

# Проверяем, успешно ли открыт источник
if not cap.isOpened():
    print("Не удалось открыть камеру")

# Определяем кодек и создаём объект записи видео
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Можно использовать другие кодеки (например, MJPG, X264)
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 20.0 — частота кадров в секунду

# Записываем видео
while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:
        out.write(frame)  # Записываем кадр в файл
        cv2.imshow('frame', frame)  # Отображаем кадр (опционально)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Выход по нажатию клавиши
            break
    else:
        break

# Освобождаем ресурсы
cap.release()
out.release()
cv2.destroyAllWindows()