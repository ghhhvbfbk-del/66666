import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 60)

y1 =  x**2
y2 = x**3

plt.figure(figsize=(10, 6))

plt.plot(x, y1, label='$y = x^{2}$', color='blue', linewidth=2)
plt.plot(x, y2, label='$y = x^{3}$', color='red', linewidth=2)

plt.title('Графики функций $y = x^{2}$ и $y = x^{3}$', fontsize=14)


plt.xlabel('x', fontsize=12)

plt.ylabel('y', fontsize=12)

plt.grid(True, alpha=0.3)
plt.axhline(y=0, color='k', linewidth=0.8)
plt.axvline(x=0, color='k', linewidth=0.8)

plt.legend(fontsize=12)
plt.axis('equal')



plt.tight_layout()
plt.show()



