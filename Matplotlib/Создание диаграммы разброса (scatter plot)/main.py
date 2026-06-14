import matplotlib.pyplot as plt
import numpy as np

# Создаём массив значений X от 0 до 10 (50 точек для плавности кривой)
X = np.linspace(0, 10, 50)

# Вычисляем соответствующие значения Y = X²
Y = X ** 2

# Создаём фигуру и оси
plt.figure(figsize=(10, 6))

# Строим линейный график (точки соединяются линиями)
plt.plot(X, Y, label='$Y = X^2$', color='blue', linewidth=2)

# Добавляем подписи осей
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)

# Добавляем заголовок
plt.title('График функции $Y = X^2$ (X от 0 до 10)', fontsize=14)

# Включаем сетку для удобства чтения графика
plt.grid(True, alpha=0.3)

# Добавляем легенду
plt.legend()

# Устанавливаем ограничения по осям (чтобы график не прилипал к краям)
plt.xlim(0, 10)
plt.ylim(0, max(Y) + 10)

# Отображаем график
plt.show()
