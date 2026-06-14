import matplotlib.pyplot as plt
import numpy as np



x  = np.arange(0, 10, 0.1)

y = x ** 2

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', s=50)



plt.plot(x,y, '--', alpha=0.6,color='red')
plt.plot(x, y, '--', alpha=0.5, color='gray')

plt.title('Scatter Plot: Y = X²', fontsize=14)

plt.xlabel('X (от 0 до 10)', fontsize=12)
plt.ylabel('Y = X²', fontsize=12)
plt.grid(True, alpha=0.3)


for i in range(len(x)):
    plt.annotate(f'({x[i]}, {y[i]})', (x[i], y[i]), textcoords="offset points",
                xytext=(0,10), ha='center', fontsize=9)



plt.tight_layout()
plt.show()
