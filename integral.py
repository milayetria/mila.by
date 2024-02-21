import numpy as np
import matplotlib.pyplot as plt

def fungsi(x):
    return 13 * x**2 + 9 * x - 12

def integral_trapesium(x1, x2, n):
    h = (x2 - x1) / n
    integral = 0.5 * (fungsi(x1) + fungsi(x2))

    for i in range(1, n):
        x = x1 + i * h
        integral += fungsi(x)

    return h * integral

x2 = 2
n = 1000  # Jumlah trapesium, semakin besar semakin akurat

hasil_integral = integral_trapesium(x1, x2, n)

x = np.linspace(x1, x2, 100)
y = fungsi(x)

plt.plot(x, y, label='13x^2 + 9x - 12')
plt.fill_between(x, y, alpha=0.3, hatch='/')
plt.text((x1 + x2) / 2, fungsi((x1 + x2) / 2), f'Integral = {hasil_integral:.2f}', ha='center', va='bottom')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafik Fungsi dan Area di Bawah Kurva')
plt.legend()
plt.show()
