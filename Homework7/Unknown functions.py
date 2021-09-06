import numpy as np
from scipy.interpolate import splev, splrep
from matplotlib import pylab as plt

n = 20
l = 20
h = l/n

x = np.arange (0, l, h)
# print(x)
# print(x[2])

x = np.append(x, l)
# print(x)
# print(len(x))

f = np.array([0])
# print(f)
g = np.array([1])
# print(g)

while(n != 0):
    # считаем синус по формуле. Дословно. Равен синусу на предыдущем шаге + косинус на шаг.

    f = np.append(f, f[-1] + 0.5 * g[-1] * h)
    # print(sin_d)
    # cos_d = np.sqrt(1 - (sin_d[-1])**2)
    g = np.append(g, g[-1] + (2-2 * f[-1]))
    n -= 1

# print(f)
# print(g)
# создадим пространство размером 6 на 6
# само пространство не будем выведено, если на нём ничего не создано.
plt.figure(figsize = (10, 6))
# создаём оси в этом пространстве. Оси по икс от нуля до 20. По игрек от -6 до 6
plt.axis([0, 20, -6, 6])
# plt.show()

# требует на вход массив икс и функцию от икс
# возвращает вектор-узлов и кортеж коэффициентов в нашей кубической функции интерполяции + степень интерполяции
splf = splrep(x, f)
# print(splf)
splg = splrep(x, g)


# Теперь должны нарисовать ещё и эти сплайны.

x2 = np.linspace(0, l, 200)

# На вход массив точек, куда должны вернуть значения сплайна. + кортеж требуемых коэффициентов.
# Возвращает массив значений сплайна, высчитанных в точках, которые подавали на вход. Если на
y2 = splev(x2, splf)
plt.plot(x2, y2, label="Кубический сплайн f")

x3 = np.linspace(0, l, 200)
y3 = splev(x3, splg)
plt.plot(x3, y3, label="Кубический сплайн g")

plt.legend()
plt.show()