# -*- coding: utf-8 -*-
"""CalculusHW9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13fRuZfIQTV74JOGIsZs7EhfdgWASe4c1

__1.__ Исследовать сходимость ряда. 


### $$\frac{1}{2\sqrt2}+\frac{1}{3\sqrt3}+\,...\,+\frac{1}{(n+1)\sqrt{n+1}}+\,...\,=\sum\limits_{n=1}^{+\infty}\frac{1}{(n+1)\sqrt{n+1}}$$

(*) Двумя различными признаками.

1) Второй признак сравнения.
$$\sum\limits_{n=1}^{+\infty}\frac{1}{(n+1)\sqrt{n+1}}=\sum\limits_{n=1}^{+\infty}\frac{1}{(n+1)^{\frac{3}{2}}}$$
Небходимое условие:
$$\lim_{n\to +\infty}\frac{1}{(n+1)^{\frac{3}{2}}}=0$$
Достаточное условие:
$$\sum\limits_{n=1}^{+\infty}\frac{1}{(n+1)^{\frac{3}{2}}}\sim O\Big(\frac{1}{n^{\frac{3}{2}}}\Big)$$
2) Интегральный признак Коши.
$$\int\limits_{1}^{+\infty}a_{x}\,dx=\int\limits_{1}^{+\infty}\frac{1}{(n+1)\sqrt{n+1}} = \int\limits_{1}^{+\infty}(n+1)^{-\frac{3}{2}} = -2(n+1)^{-\frac{1}{2}}\bigg|_1^{+ \infty} = 0 + \frac{2}{\sqrt 2} =\sqrt 2$$
Интеграл существует, следовательно ряд сходится.

2. Исследовать сходимость ряда
$$\frac{1000}{1!}+\frac{1000^2}{2!}+\,...\,+\frac{1000^n}{n!}+\,...\,=\sum\limits_{n=1}^{+\infty}\frac{1000^n}{n!}$$

Признак д’Аламбера.


$$\lim_{n\to +\infty}\frac{a_{n+1}}{a_{n}}=
\lim_{n\to +\infty}\frac{\frac{1000^{n+1}}{n+1!}}{\frac{1000^n}{n!}}=\lim_{n\to +\infty}\frac{1000}{n+1} = 0 $$ 
$$0<1\ значит\ ряд\ сходится$$

__3*.__ Исследовать сходимость ряда

### $$\frac{2\cdot1!}{1}+\frac{2^2\cdot2!}{2^2}+\,...\,+\frac{2^n\cdot n!}{n^n}+\,...\,=\sum\limits_{n=1}^{+\infty}\frac{2^n\cdot n!}{n^n}$$


$$\lim_{n\to +\infty}\frac{a_{n + 1}}{a_{n}} = \lim_{n\to +\infty}\frac{\frac{2^{n+1}\cdot (n + 1)!}{(n + 1)^{n + 1}}}{\frac{2^n\cdot n!}{n^n}} = \lim_{n\to +\infty}\frac{2\cdot n^n}{(n + 1)^n} = 2\cdot\lim_{n\to +\infty}\frac{n^n}{(n+1)^n} = 2\cdot\lim_{n\to +\infty}\Big(\frac{n + 1 - 1}{n + 1}\Big)^n = 2\cdot\lim_{n\to +\infty} \Big(1 - \frac{1}{n + 1} \Big)^n = 2\cdot\lim_{n\to +\infty} \Big(1 + \frac{1}{-(n + 1)} \Big)^n = 2\cdot\lim_{n\to +\infty} \Big(1 + \frac{1}{-(n + 1)} \Big)^{\frac{n(-(n + 1))}{-(n + 1)}} = 2 \cdot e^{\lim_{n\to +\infty}\frac{n}{-(n + 1)}} = 2e^{-1} = \frac{2}{e} < 1$$

Ряд сходится

__4*.__ Исследовать сходимость ряда

### $$\frac{3\cdot1!}{1}+\frac{3^2\cdot2!}{2^2}+\,...\,+\frac{3^n\cdot n!}{n^n}+\,...\,=\sum\limits_{n=1}^{+\infty}\frac{3^n\cdot n!}{n^n}$$


Найдем предел:

$$\lim_{n\to +\infty}\frac{a_{n + 1}}{a_{n}} = \lim_{n\to +\infty}\frac{\frac{3^{n+1}\cdot (n + 1)!}{(n + 1)^{n + 1}}}{\frac{3^n\cdot n!}{n^n}} = \lim_{n\to +\infty}\frac{3\cdot n^n}{(n + 1)^n} = 3\cdot\lim_{n\to +\infty}\frac{n^n}{(n+1)^n} = 2\cdot\lim_{n\to +\infty}\Big(\frac{n + 1 - 1}{n + 1}\Big)^n = 3\cdot\lim_{n\to +\infty} \Big(1 - \frac{1}{n + 1} \Big)^n = 3\cdot\lim_{n\to +\infty} \Big(1 + \frac{1}{-(n + 1)} \Big)^n = 3\cdot\lim_{n\to +\infty} \Big(1 + \frac{1}{-(n + 1)} \Big)^{\frac{n(-(n + 1))}{-(n + 1)}} = 3 \cdot e^{\lim_{n\to +\infty}\frac{n}{-(n + 1)}} = 3e^{-1} = \frac{3}{e} > 1$$

Ряд расходится

__5*.__ Исследовать сходимость ряда

### $$-\frac{\sqrt1}{2}+\frac{\sqrt2}{3}-\,...\,+\frac{(-1)^n\sqrt n}{n+1}+\,...\,=\sum\limits_{n=1}^{+\infty}\frac{(-1)^n\sqrt n}{n+1}$$
$$$$
Знакочередующийся ряд. Признак Лейбница.

1)
$$\lim_{n\to +\infty}a_n = \lim_{n\to +\infty} \frac{(-1)^n\sqrt n}{n + 1}  = \Big(\frac{\infty}{\infty}\Big) = 0 $$

Старшая степень числителя меньше старшей степени знаменателя, следовательно предел будет равен нулю. 

2) $$\Big|\frac{(-1)^{n + 1}\sqrt {n + 1}}{(n + 1) + 1}\Big| < \Big|\frac{(-1)^n\sqrt n}{n+1}\Big|$$

Возьмём производную от функции.

$$\Big(\frac{\sqrt n}{n + 1}\Big)' = \frac{\frac{1}{2}\cdot\frac{1}{\sqrt n}(n+1) - \sqrt n}{(n + 1)^2} = \frac{-n + 1}{2\sqrt n \cdot(n + 1)^2}$$

Корнем является n = 1. Подставим 4. Получаем, что производная меньше нуля. Функция убывает. Итого: условие монотонности выполняется.


3) $$\int\limits_{1}^{+\infty}a_{x}\,dx = \int\limits_{1}^{+\infty} \frac {\sqrt n}{n+1}= *$$
$$$$
$$t = \sqrt n$$

$$dt=\frac{1}{2}\frac{1}{\sqrt n}dn$$
$$dn = 2\sqrt n\cdot dt$$ 

$$* = \int\limits_{1}^{+\infty} \frac{t^2}{t^2 + 1}\cdot dt = \int\limits_{1}^{+\infty} \frac{t^2 + 1 - 1}{t^2 + 1}\cdot dt = \int\limits_{1}^{+\infty} \Big( 1 - \frac{1}{t^2 + 1}\Big) dt =  (t + \arctan t )\Bigg|_1^{\infty} = \infty$$

Без обратной замены видно, что получаем бесконечность. Итого, ряд не сходится.

Ответ для всего решения: ряд сходится условно.

Разное. Проверим через д'Аламбера: Если предел по модулю меньше единицы, то следующий член меньше предыдущего.

$$\lim_{n\to +\infty}\frac{a_{n+1}}{a_{n}}=
\lim_{n\to +\infty} \frac{\sqrt {n+1}}{n + 2}\cdot\frac{n + 1}{\sqrt n} = 1$$ 

Если я понимаю, то предел будет равен 1. А потому д'Аламбера не работает. Но тогда неверно решение, что монотонность выполняется.
"""

from sympy import *
init_printing()
n = Symbol('n')
f = (sqrt(n + 1)/(n + 2))/((sqrt(n)/(n + 1)))
f

limit (f, n, +oo)

from sympy import *
init_printing()
n = Symbol('n')
f = sqrt(n)/(n + 1)
f

integrate(f,(n, 1, +oo))

integrate(f, n)

diff(f, n)

from scipy.optimize import fsolve
import sys

def equations(p):
  n = p
  - (n**(1/2)) / ((n + 1)**2) + 1 / (2 * n**(1/2)*(n + 1))
  # - n**(1/2)
  return n

n = fsolve(equations, 4)
print(n)

"""Так и не получилось у меня заставить fsolve найти корни производной. Поэтому в sympy"""

from sympy.solvers import solve
from sympy import Symbol
n = Symbol('n')
solve(- (n**(1/2)) / ((n + 1)**2) + 1 / (2 * n**(1/2)*(n + 1)), n)

"""__6*.__ Разложить функцию $y=e^x$ в ряд Маклорена, а так же в ряд Фурье на отрезке $[-\pi, \pi]$. Построить график функции и разложений.

1) ряд Маклорена

$$f(x)=\sum\limits_{n=0}^{+\infty}\frac{f^{(n)}(0)}{n!}x^n$$
$$$$
$$f^{(n)}=e^x,\ f^{(n)}(0) = 1$$
$$$$
$$e^x=1+\frac{1\cdot x}{1!}+\frac{1\cdot x^2}{2!}+\frac{1\cdot x^3}{3!}+ ... + \frac{1\cdot x^n}{n!}=\sum\limits_{n=0}^{+\infty}\frac{x^n}{n!}$$


2) ряд Фурье

$$f(x)=a_{0}+\sum\limits_{n=1}^{+\infty}(a_n\cos nx+b_n\sin nx)$$

где

### $$a_0=\frac{1}{2\pi}\int\limits_{-\pi}^\pi f(x)\,dx$$


$$\int\limits_{-\pi}^\pi$$

$$a_0 = \frac{1}{2\pi}\int\limits_{-\pi}^\pi f(x)\,dx = \frac{1}{2\pi}\int\limits_{-\pi}^\pi e^x\,dx = \frac{1}{2\pi} e^x \Bigr|_{-\pi}^\pi = \frac{e^{\pi} - e^{-\pi}}{2\pi}$$

### $$a_n = \frac{1}{\pi}\int\limits_{-\pi}^\pi f(x)\cos nx\,dx = \frac{1}{\pi}\int\limits_{-\pi}^\pi e^x \cos nx\,dx$$

$$\int\limits_{-\pi}^\pi e^x \cos nx\,dx = (*)$$

$$U = e^x \Rightarrow dU=e^x\,dx$$ 
$$dV = \cos nx\,dx \Rightarrow V=\frac{1}{n}\sin nx$$ 

$$ (*) = \frac{1}{n} \sin nx \cdot e^x \Bigr|_{-\pi}^\pi - \int\limits_{-\pi}^\pi \frac{1}{n} \sin nx \cdot e^x \,dx = \frac{1}{n} \sin nx \cdot e^x \Bigr|_{-\pi}^\pi - \frac{1}{n} \int\limits_{-\pi}^\pi \sin nx \cdot e^x \,dx = (*)$$

$$ U = e^x \Rightarrow dU=e^x\,dx$$
$$ dV = \sin nx \,dx \Rightarrow V = - \frac{1}{n} \cos nx$$

$$ (*) = \frac{1}{n} \sin nx \cdot e^x \Bigr|_{-\pi}^\pi - \frac{1}{n} \Big(-\frac{1}{n} \cos nx \cdot e^x \Bigr|_{-\pi}^\pi - \int\limits_{-\pi}^\pi - \frac{1}{n} \cos nx \cdot e^x \,dx \Big) = \frac{1}{n} \sin nx \cdot e^x \Bigr|_{-\pi}^\pi + \frac{1}{n^2} \cos nx \cdot e^x \Bigr|_{-\pi}^\pi - \frac{1}{n^2}\int\limits_{-\pi}^\pi \cos nx \cdot e^x \,dx$$

переносим интеграл в левую часть

$$\int\limits_{-\pi}^\pi \cos nx \cdot e^x \,dx + \frac{1}{n^2}\int\limits_{-\pi}^\pi \cos nx \cdot e^x \,dx = \frac{1}{n} \sin nx \cdot e^x \Bigr|_{-\pi}^\pi + \frac{1}{n^2} \cos nx \cdot e^x \Bigr|_{-\pi}^\pi$$

$$\Big(1 + \frac{1}{n^2}\Big)\int\limits_{-\pi}^\pi \cos nx \cdot e^x \,dx = \frac{e^{\pi}}{n} \sin {\pi}n - \frac{e^{-\pi}}{n} \sin ({-\pi}n) + \frac{e^{\pi}}{n^2} \cos {\pi}n - \frac{e^{-\pi}}{n^2} \cos ({-\pi}n)$$

$$\Big(1 + \frac{1}{n^2}\Big)\int\limits_{-\pi}^\pi \cos nx \cdot e^x \,dx = \frac{e^{\pi}}{n^2} \cos {\pi}n - \frac{e^{-\pi}}{n^2} \cos ({\pi}n)$$

$$\int\limits_{-\pi}^\pi \cos nx \cdot e^x \,dx =  \cos {\pi}n \Big(\frac{e^{\pi}}{n^2}- \frac{e^{-\pi}}{n^2} \Big) \cdot \Big(\frac{n^2}{n^2 + 1} \Big)$$

$$\int\limits_{-\pi}^\pi \cos nx \cdot e^x \,dx =  (-1)^n\Big(\frac{e^{\pi} - e^{-\pi}}{n^2 + 1} \Big)$$

$$a_n = \frac{1}{\pi}\int\limits_{-\pi}^\pi f(x)\cos nx\,dx = \frac{1}{\pi}\int\limits_{-\pi}^\pi e^x \cos nx\,dx = \frac{1}{\pi} (-1)^n\Big(\frac{e^{\pi} - e^{-\pi}}{n^2 + 1} \Big)$$

### $$b_n = \frac{1}{\pi}\int\limits_{-\pi}^\pi f(x)\sin nx\,dx = \frac{1}{\pi}\int\limits_{-\pi}^\pi e^x \sin nx\,dx$$

$$\int\limits_{-\pi}^\pi e^x \sin nx\,dx = (*)$$

$$U = e^x \Rightarrow dU=e^x\,dx$$ 
$$dV = \sin nx\,dx \Rightarrow V = -\frac{1}{n}\cos nx$$

$$(*) = -\frac{e^x}{n}\cos nx \Bigr|_{-\pi}^\pi - \int\limits_{-\pi}^\pi -\frac{1}{n}\cos nx \cdot e^x \,dx = -\frac{e^x}{n}\cos nx \Bigr|_{-\pi}^\pi + \int\limits_{-\pi}^\pi -\frac{1}{n}\cos nx \cdot e^x \,dx = (*)$$

$$U = e^x \Rightarrow dU=e^x\,dx$$
$$dV = \cos nx\,dx \Rightarrow V = \frac{1}{n}\sin nx$$

$$(*) = -\frac{e^x}{n}\cos nx \Bigr|_{-\pi}^\pi + \frac{1}{n}\Big( e^x \cdot \frac{1}{n}\sin nx \Bigr|_{-\pi}^\pi - \int\limits_{-\pi}^\pi \frac{1}{n} \sin nx \cdot e^x \,dx \Big) = -\frac{e^x}{n}\cos nx \Bigr|_{-\pi}^\pi + \frac{1}{n^2} e^x \sin nx \Bigr|_{-\pi}^\pi - \frac{1}{n^2} \int\limits_{-\pi}^\pi \sin nx \cdot e^x \,dx$$

переносим интегралы в левую часть

$$\int\limits_{-\pi}^\pi e^x \sin nx\,dx  + \frac{1}{n^2} \int\limits_{-\pi}^\pi \sin nx \cdot e^x \,dx = \frac{1}{n^2} e^x \sin nx \Bigr|_{-\pi}^\pi - -\frac{e^x}{n}\cos nx \Bigr|_{-\pi}^\pi$$

$$\int\limits_{-\pi}^\pi e^x \sin nx\,dx \Big( \frac{n^2 + 1}{n^2}\Big) = \frac{1}{n^2} e^{\pi} \sin \pi n - \frac{1}{n^2} e^{-\pi} \sin (-\pi n) - \Big(\frac{e^{\pi}}{n}\cos \pi n - \frac{e^{-\pi}}{n}\cos (-\pi n)\Big) $$

$$\int\limits_{-\pi}^\pi e^x \sin nx\,dx \Big( \frac{n^2 + 1}{n^2}\Big) = \frac{e^{-\pi}}{n}\cos (-\pi n) - \frac{e^{\pi}}{n}\cos \pi n$$

$$\int\limits_{-\pi}^\pi e^x \sin nx\,dx = \Big( \frac{n^2}{n(n^2 + 1)}\Big)(-1)^n(e^{-\pi} - e^{\pi})$$

$$\int\limits_{-\pi}^\pi e^x \sin nx\,dx = \frac{(-1)^n(e^{-\pi} - e^{\pi})n}{n^2 + 1}$$

$$b_n = \frac{1}{\pi} \frac{(-1)^n(e^{-\pi} - e^{\pi})n}{n^2 + 1}$$

$$f(x)=a_{0}+\sum\limits_{n=1}^{+\infty}(a_n\cos nx+b_n\sin nx) = \frac{e^{\pi} - e^{-\pi}}{2\pi} + \sum\limits_{n=1}^{+\infty}\Big( \frac{(-1)^n}{\pi} \frac{e^{\pi} - e^{-\pi}}{n^2 + 1}  \cos nx + \frac{(-1)^n}{\pi} \frac{(e^{-\pi} - e^{\pi})n}{n^2 + 1} \sin nx \Big)$$
"""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (6, 6))
plt.axis([-2, 5, -6, 20])


x = np.arange(-5, 20, 0.5)

y = np.exp(x)

k = 6
# tay = []
def taylor():
    n = 0
    res_t = 0
    while n <= k:
        
        res_t = res_t + (x**n)/(np.math.factorial(n))
        # tay.append(res_t)
        n += 1
    return res_t

# print(taylor())

def fourier():
    n = 0
    res_f = 0
    # a_0 = ((np.exp(np.pi) - np.exp(-np.pi))/2*np.pi
    while n <= k:
        res_f = res_f + ((1 / np.pi) * ((-1) ** (n+1)) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1)) * np.cos(x * n) + (n * (1 / np.pi) * ((-1) ** n) * (np.exp(-np.pi) - np.exp(np.pi)) / ((n ** 2) + 1)) * np.sin(x * n)
        
        n += 1
    # return res_f + ((np.exp(np.pi) - np.exp(-np.pi))/2*np.pi

plt.plot(x, y, marker = "o", label = "f", ls="", c = 'b')
plt.plot(x, taylor(), c = 'r', label = "taylor")
# plt.plot(x, fourier(), marker = "o", label="fourier", ls="", c = 'b')
plt.grid(True)
plt.legend()
plt.show()

"""Честно говоря, не уверен насчёт построения Фурье(хотя и Тейлора тоже). Поэтому демонстрирую 2 варианта. Первый тот, что получился изначально. Но что-то он совсем не то рисует при малом количестве итераций."""

import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize = (6, 6))
plt.axis([-5, 5, -5, 20])


# x = np.arange(0, 4, 0.5)
x = np.arange(-np.pi, np.pi, 0.25)
# x = np.linspace(-np.pi, np.pi, 20)

y = np.exp(x)

k = 40

# print((np.exp(np.pi) - np.exp(-np.pi))/(2*np.pi))
# print(x)

def fourier():
    n = 1
    res_f = 0
    # a_0 = ((np.exp(np.pi) - np.exp(-np.pi))/2*np.pi
    while n <= k:
        res_f = res_f + ((1 / np.pi) * ((-1) ** (n)) * np.cos(x * n) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1))  + (n * (1 / np.pi) * ((-1) ** n) * np.sin(x * n) * (np.exp(-np.pi) - np.exp(np.pi)) / ((n ** 2) + 1))
        # res_f = res_f + (((-1) ** (n)) / np.pi) * ((np.exp(np.pi) - np.exp(-np.pi)) * np.cos(x * n) / ((n ** 2) + 1)  + (np.exp(-np.pi) - np.exp(np.pi)) * np.sin(x * n) / ((n ** 2) + 1)) 
        # res_f = res_f + (((-1) ** (n)) / ((np.pi) * ((n ** 2) + 1))) * ((np.exp(np.pi) - np.exp(-np.pi)) * np.cos(x * n) + n * (np.exp(-np.pi) - np.exp(np.pi)) * np.sin(x * n)) 
        # print('cos', np.cos(x * n))
        # print('sin', np.sin(x * n))
        n += 1
    # res_f = res_f + ((np.exp(np.pi) - np.exp(-np.pi))/(2*np.pi)

    return res_f + (np.exp(np.pi) - np.exp(-np.pi))/(2 * np.pi)

# print('res_f', fourier())

plt.plot(x, y, marker = "d", label = "f", ls="", c = 'g')
plt.plot(x, fourier())
plt.grid(True)
plt.legend()
plt.show()

"""И второй код. Из примера на хабре."""

import matplotlib.pyplot as plt # модуль для графиков
import numpy as np # модуль для операций со списками и массивами

def func(n):# анализируемая функция
         return np.exp(n)
def func_1(n):# функция для расчёта коэффициента a[k]
         return ((-1) ** n) * (1 / np.pi) * (np.exp(np.pi) - np.exp(-np.pi)) / ((n ** 2) + 1)
def func_2(n):#функция для расчёта коэффициента b[k]
         return ((-1) ** n) * (n * (1 / np.pi)) * (np.exp(-np.pi) - np.exp(np.pi)) / ((n ** 2) + 1)

a_0 = (np.exp(np.pi) - np.exp(-np.pi)) / (2*np.pi)

c = 40 #количество членов

a = []; b = []; k = np.arange(0, c, 1); q = np.arange(-np.pi, np.pi, 0.05)

a = [func_1(n) for n in k]
# print(a)
b = [func_2(n) for n in k]
# print(b)
# print(k)
# print('a_0', a_0)
# print('a[0]', a[0])

F1 = a_0 + [a[1] * np.math.cos(k[1] * x) + b[1] * np.math.sin(k[1] * x) for x in q]
# print(F1)
F2 = a_0 + [a[2] * np.math.cos(k[2] * x) + b[2] * np.math.sin(k[2] * x) for x in q]
F3 = a_0 + [a[3] * np.math.cos(k[3] * x) + b[3] * np.math.sin(k[3] * x) for x in q]

plt.figure()

plt.plot(q, F1, label = '1 гармоника', c = 'r')
plt.plot(q, F2 , label = '2 гармоника')
plt.plot(q, F3, label = '3 гармоника')
plt.legend()


plt.grid(True)
# F = np.empty(shape=[0, n])
# F = F1 + F2 + F3 -2*a_0

# plt.plot(q, F, label='F(t)')
F = np.array([0*x for x in q])
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
plt.plot(q, y, label = 'exp')
plt.grid(True)
plt.legend()
plt.show()