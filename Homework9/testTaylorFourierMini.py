import numpy as np
import matplotlib.pyplot as plt
import math
#
# plt.figure(figsize = (10, 6))
# plt.axis([-5, 5, -6, 20])
#
# # генерируем цифры в рамках диапазона с шагом. начало, конец, шаг
# x = np.arange(1, 2.5, 0.5)
# # print(x)
# # функция будет зависеть от икс
# y = np.exp(x)
# # т.е. как я понимаю, для рисования мы бёрем икс, потом подставляем его в функцию, получаем значение и выводим.
#
# k = 1
# tay = []
# def taylor():
#     n = 0
#     res_t = 0
#     while n <= k:
#         res_t = res_t + (x**n) / (np.math.factorial(n))
#
#         tay.append(res_t)
#         n += 1
#
#     print('tay', tay)
#     return res_t
# print('икс', x)
# print(taylor())
#
# def fourier():
#     n = 0
#     res_f = 0
#     a_0 = (np.exp(np.pi) - np.exp(-np.pi)) / (2 * np.pi)
#     # a_n = (1 / np.pi) * ((-1) ** n) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1)
#     while n <= k:
#         res_f = res_f + ((1 / np.pi) * ((-1) ** n) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1)) * np.cos(x * n) + \
#                 (n * (1 / np.pi) * ((-1) ** n) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1)) * np.sin(x * n)
#         n += 1
#     return res_f + a_0
#
# print(fourier())
######################################################################################
# import numpy as np
# import matplotlib.pyplot as plt
#
# plt.figure(figsize = (6, 6))
# plt.axis([-5, 5, -5, 30])
#
#
# # x = np.arange(-np.pi, np.pi, 0.5)
# x = np.arange(-5, 20, 0.5)
#
# k = 1
#
# print((np.exp(np.pi) - np.exp(-np.pi))/(2*np.pi))
#
# print(x)
#
# def fourier():
#     n = 1
#     res_f = 0
#     # a_0 = ((np.exp(np.pi) - np.exp(-np.pi))/2*np.pi
#     while n <= k:
#         # res_f = res_f + ((1 / np.pi) * ((-1) ** (n)) * np.cos(x * n) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1))  + (n * (1 / np.pi) * ((-1) ** n) * np.sin(x * n) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1))
#         res_f = res_f + (((-1) ** (n)) / np.pi) * ((np.exp(np.pi) - np.exp(-np.pi)) * np.cos(x * n) / ((n ** 2) + 1)  + (np.exp(-np.pi) - np.exp(np.pi)) * np.sin(x * n) / ((n ** 2) + 1))
#
#
#         print('cos', np.cos(x * n))
#         print('sin', np.sin(x * n))
#         print(res_f)
#         n += 1
#     # res_f = res_f + ((np.exp(np.pi) - np.exp(-np.pi))/(2*np.pi)
#
#     return res_f + (np.exp(np.pi) - np.exp(-np.pi))/(2 * np.pi)
#
# fourier()

###############################################################
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(6, 6))
plt.axis([-5, 5, -5, 30])

# x = np.arange(-1, 2, 0.5)
x = np.arange(-np.pi, np.pi, 0.05)
# x = np.linspace(-np.pi, np.pi, 20)

y = np.exp(x)

k = 5

print((np.exp(np.pi) - np.exp(-np.pi)) / (2 * np.pi))

print(x)


def fourier():
    n = 1
    res_f = 0
    # a_0 = ((np.exp(np.pi) - np.exp(-np.pi))/2*np.pi
    while n <= k:
        # res_f = res_f + ((1 / np.pi) * ((-1) ** (n)) * np.cos(x * n) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1))  + (n * (1 / np.pi) * ((-1) ** n) * np.sin(x * n) * (np.exp(-np.pi) - np.exp(np.pi)) / ((n ** 2) + 1))
        # res_f = res_f + (((-1) ** (n)) / np.pi) * ((np.exp(np.pi) - np.exp(-np.pi)) * np.cos(x * n) / ((n ** 2) + 1)  + (np.exp(-np.pi) - np.exp(np.pi)) * np.sin(x * n) / ((n ** 2) + 1))
        res_f = res_f + (1 / ((np.pi) * ((n ** 2) + 1))) * (((-1) ** (n)) * (np.exp(np.pi) - np.exp(-np.pi)) * np.cos(x * n) + ((-1) ** (n)) * (np.exp(-np.pi) - np.exp(np.pi)) * np.sin(x * n))
        a_n = (np.exp(np.pi) - np.exp(-np.pi)) * (((-1) ** (n)) / ((np.pi) * ((n ** 2) + 1)))
        b_n = (np.exp(-np.pi) - np.exp(np.pi)) * (((-1) ** (n)) / ((np.pi) * ((n ** 2) + 1)))
        print('a_n', a_n)
        print('b_n', b_n)
        print('a_0', (np.exp(np.pi) - np.exp(-np.pi))/ (2 * np.pi))
        # print('cos', np.cos(x * n))
        # print('sin', np.sin(x * n))
        n += 1
    # res_f = res_f + ((np.exp(np.pi) - np.exp(-np.pi))/(2*np.pi)

    return res_f + (np.exp(np.pi) - np.exp(-np.pi)) / (2 * np.pi)


print('res_f', fourier())

plt.plot(x, y, marker="4", label="f", ls="", c='b')
# plt.plot(x, taylor(), c = 'r', label = "taylor")
plt.plot(x, fourier())
plt.legend()
plt.show()