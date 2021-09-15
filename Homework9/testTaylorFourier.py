import numpy as np
import matplotlib.pyplot as plt
import math

plt.figure(figsize = (10, 6))
plt.axis([-5, 5, -6, 20])

# генерируем цифры в рамках диапазона с шагом. начало, конец, шаг
x = np.arange(1, 20, 0.5)
# print(x)
# функция будет зависеть от икс
y = np.exp(x)
# т.е. как я понимаю, для рисования мы бёрем икс, потом подставляем его в функцию, получаем значение и выводим.

k = 30
tay = []
def taylor():
    n = 0
    res_t = 0
    while n <= k:
        # p = p + (function.diff(x,i).subs(x, x0))/(factorial(i))*(x-x0)**i
        # print(x ** n)
        res_t = res_t + (x[n]**n) / (np.math.factorial(n))

        # print(res_t)
        tay.append(res_t)
        n += 1

        print('tay', tay)
    return res_t

print('икс', x)

taylor()

# four = []
# def fourier():
#     n = 1
#     res_f = 0
#
#     a_0 = (np.exp(np.pi) - np.exp(-np.pi))/(2 * np.pi)
#     # a_n = (1/np.pi) * ((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))/((n**2) + 1)
#     # b_n = n * (1/np.pi) * ((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))/((n**2) + 1)
#     while n <= len(x):
#         # res_f = res_f + (1/np.pi) * ((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))/((n**2) + 1) * np.math.cos(n * x) + n * (1/np.pi) * ((-1)**n) * (np.exp(np.pi) - np.exp(-np.pi))/((n**2) + 1) * np.math.sin(n * x)
#         r = math.cos(x[n] * n)
#         print(r)
#         four = four.append(r)
#         print(four)
#         # res_f = res_f + (1 / np.pi) * ((-1) ** n) * math.cos(x[n] * n)
#
#
#     # return res_f




# plt.plot(x, y, marker = "x", label="f", ls="", c = 'b')
# plt.plot(x, taylor(), c = 'r')
# plt.plot(x, fourier(), marker = "o", label="fourier", ls="", c = 'b')
# plt.show()

