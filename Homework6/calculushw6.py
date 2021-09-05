import numpy as np
import matplotlib.pyplot as plt


# Задаем рандомное распределение точек
xi = np.random.uniform(-8, 8, 200)
# a = np.random.uniform(0.5, 1.5, 200)
# b = np.random.uniform(-1, 1, 200)

# f = 1/(1+np.exp(-a*xi-b))
yi = 1/(1+np.exp(-np.random.uniform(0.5, 1.5, 200)*xi-np.random.uniform(-1, 1, 200)))
plt.plot(xi,yi, marker="o", ls="")


from scipy.optimize import fsolve, broyden1
import math

def equations(p):
    a, b = p
    # Это заранее найденные производные от (y-f(x))**2 по переменным a и b
    # return ((-2*xi*np.exp(-A*xi-B)*(yi-1/(1+np.exp(-A*xi-B)))/(1+np.exp(-A*xi-B))**2).sum(), (-2*np.exp(-A*xi-B)*(yi-1/(1+np.exp(-A*xi-B)))/(1+np.exp(-A*xi-B))**2).sum())
    return (((-2) * xi * (yi - (1 / (1 + np.exp(-((a * xi) + b))))) * (np.exp(-(a * xi + b))) / ((np.exp(-(a * xi + b)) + 1) ** 2)).sum(), ((-2) * (yi - (1 / (1 + np.exp(-((a * xi) + b))))) * (np.exp(-(a * xi + b))) / ((np.exp(-(a * xi + b)) + 1) ** 2)).sum())
# Численное решение нелинечной системы уравнений
a, b =  fsolve(equations, (1, 1))
print(a, b)
#A, B =  broyden1(equations, (1, 1))
#print (A, B)

x = np.linspace(-8, 8, 200)
plt.plot(x, 1/(1+np.exp(-a*x-b)))


plt.show()