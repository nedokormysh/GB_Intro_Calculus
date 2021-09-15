from scipy.integrate import quad # модуль для интегрирования
import matplotlib.pyplot as plt # модуль для графиков
import numpy as np # модуль для операций со списками и массивами

def func(n):# анализируемая функция
         return np.exp(n)
def func_1(n):# функция для расчёта коэффициента a[k]
         return ((-1) ** n) * (1 / np.pi) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1)
def func_2(n):#функция для расчёта коэффициента b[k]
         return ((-1) ** n) * (n * (1 / np.pi)) * (np.exp(-np.pi) - np.exp(np.pi)) / ((n ** 2) + 1)

a_0 = (np.exp(np.pi) - np.exp(-np.pi)) / (2*np.pi)
c = 4
a = []; b = []; k = np.arange(0, c, 1); q = np.arange(-np.pi, np.pi, 0.05)

a = [func_1(n) for n in k]
print(a)
b = [func_2(n) for n in k]
print(b)
print(k)
print('a_0', a_0)
print('a[0]', a[0])

F1 = a_0 + [a[1] * np.math.cos(k[1] * x) + b[1] * np.math.sin(k[1] * x) for x in q]
# print(F1)
F2 = a_0 + [a[2] * np.math.cos(k[2] * x) + b[2] * np.math.sin(k[2] * x) for x in q]
F3 = a_0 + [a[3] * np.math.cos(k[3] * x) + b[3] * np.math.sin(k[3] * x) for x in q]

plt.figure()

plt.plot(q, F1, label='1 гармоника', c = 'r')
plt.plot(q, F2 , label='2 гармоника')
plt.plot(q, F3, label='3 гармоника')


plt.grid(True)
# F = np.empty(shape=[0, n])
# F = F1 + F2 + F3 -2*a_0

# plt.plot(q, F, label='F(t)')
F = np.array([0*x for x in q+1])# подготовка массива для анализа с a[0]/2
# print('F',F)
# print('Len F',len(F))
# print('F1', F1)
# print('F2', F2)
# print('F3', F3)
# print('LenF1', len(F1), len(F2))

for n in np.arange(1, c, 1):
         F = F + np.array([a[n] * np.math.cos(k[n] * x) + b[n] * np.math.sin(k[n] * x) for x in q])# вычисление членов ряда Фурье
F = F + a_0

y = np.exp(q)

plt.figure()
plt.plot(q, F, label='F(t)')
plt.plot(q, y)
plt.show()