import cv2

# Инициализация веб‑камеры (0 — индекс камеры по умолчанию)
cap = cv2.VideoCapture(0)

# Загрузка классификатора для обнаружения лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    # Чтение кадра с веб‑камеры
    ret, frame = cap.read()

    if not ret:
        print("Не удалось получить кадр с камеры")
        break

    # Преобразование кадра в оттенки серого (классификатор работает с чёрно‑белыми изображениями)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Обнаружение лиц на кадре
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # Коэффициент уменьшения изображения на каждом масштабе
        minNeighbors=2,  # Минимальное количество соседей для сохранения прямоугольника
        minSize=(31, 31)  # Минимальный размер лица
    )

    # Отрисовка прямоугольников вокруг обнаруженных лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (139, 0, 0), 1)
        cv2.putText(frame,' maika',   (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (139, 0, 0), 2)

    # Отображение кадра с выделенными лицами
    cv2.imshow('Face Detection', frame)

    # Выход по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()
