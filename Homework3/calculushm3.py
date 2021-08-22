# -*- coding: utf-8 -*-
"""CalculusHM3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iXxjIlbFXF4bCuW2LWhO4fWEuGphpYW1

1. Найти предел функции:

### $$а)\,\,\,\,\lim_{x\to 6} \frac{x^2-36}{x^2-x-30}$$
$$$$
$$\lim_{x \to 6}\frac{x^2-36}{x^2-x-30} = \Big(\frac{0}{0}\Big) = \lim_{x \to 6}
\frac{(x-6)(x+6)}{(x-6)(x+5)}=\lim_{x \to 6}\frac{(x+6)}{(x+5)}=\lim_{x \to 6}\frac{(6+6)}{(6+5)} = \frac{12}{11}$$
$$$$
$$ D = b^2 - 4ac = 1-120=121$$
$$x_{1, 2}=\frac{-b\pm \sqrt{D}}{2a}=\frac{1\pm 11}{2}$$
"""

from sympy import *
init_printing()

x=Symbol('x')
a = (x**2 - 36) / (x**2-x-30)
a

print('Проверка через библиотеку sympy')
print('')
limit (a, x, 6)

"""### $$б)\,\,\,\,\lim_{x\to 7} \frac{x^2-49}{x^2-13x+42}$$

$$$$
$$\lim_{x \to 7}\frac{x^2-49}{x^2-13x+42} = \Big(\frac{0}{0}\Big) = \lim_{x \to 7}
\frac{(x-7)(x+7)}{(x-7)(x-6)}=\lim_{x \to 7}\frac{(x+7)}{(x-6)}=\lim_{x \to 7}\frac{(7+7)}{(7-6)} = 14$$
$$$$
$$ D = b^2 - 4ac = 169-168=121$$
$$x_{1, 2}=\frac{-b\pm \sqrt{D}}{2a}=\frac{13\pm 1}{2}$$
"""

x=Symbol('x')
a = (x**2 - 49) / ((x**2)-(13*x)+42)
a

print('Проверка через библиотеку sympy\n')
limit (a, x, 7)

"""
### $$в^*)\,\,\,\,\lim_{x\to 7} \frac{\sqrt{x+2}-\sqrt[3]{x+20}}{\sqrt[4]{x+9}-2}$$
$$$$
$$\lim_{x\to 7} \frac{\sqrt{x+2}-\sqrt[3]{x+20}}{\sqrt[4]{x+9}-2} = \Big(\frac{0}{0}\Big)$$ 

$$\sqsupset \sqrt{x+2}-\sqrt[3]{x+20} = A$$
избавимся от корней в знаменателе

$$ = \lim_{x\to 7} \frac{A*(\sqrt[4]{x+9}+2)*(\sqrt{x+9}+4)}{x+9-16} = $$

$$\sqsupset (\sqrt[4]{x+9}+2)*(\sqrt{x+9}+4)= B$$

$$ = \lim_{x\to 7} \frac{(\sqrt{x+2} - \sqrt[3]{x+20})*(x+2+\sqrt{x+2}*\sqrt[3]{x+20}+\sqrt[3]{(x+20)^2})*B}{(x-7)*(x+2+\sqrt{x+2}*\sqrt[3]{x+20}+\sqrt[3]{(x+20)^2})} =\lim_{x\to 7} \frac{(\sqrt{(x+2)^3} - (x+20))*B*(\sqrt{(x+2)^3} + (x + 20))}{(x-7)*(x + 2 + \sqrt{x+2}*\sqrt[3]{x + 20}+\sqrt[3]{(x + 20)^2})*(\sqrt{(x + 2)^3} + (x + 20))} =  \lim_{x\to 7} \frac{({(x+2)^3} - (x + 20)^2)*B}{(x-7)*(x+2+\sqrt{x+2}*\sqrt[3]{x+20}+\sqrt[3]{(x+20)^2})*(\sqrt{(x+2)^3} + (x + 20))} =
\lim_{x\to 7} \frac{(x^3 +6x^2+12x+8-x^2-40x-400)*B}{(x-7)*(x+2+\sqrt{x+2}*\sqrt[3]{x+20}+\sqrt[3]{(x+20)^2})*(\sqrt{(x+2)^3} + (x + 20))}=\lim_{x\to 7} \frac{(x^3 + 5x^2 - 28x - 392)*B}{(x-7)*(x+2+\sqrt{x+2}*\sqrt[3]{x + 20}+\sqrt[3]{(x+20)^2})*(\sqrt{(x+2)^3} + (x + 20))}=\lim_{x\to 7} \frac{(x - 7)*(x^2 + 12x + 56)*(\sqrt[4]{x+9}+2)*(\sqrt{x+9}+4)}{(x-7)*(x+2+\sqrt{x+2}*\sqrt[3]{x+20}+\sqrt[3]{(x+20)^2})*(\sqrt{(x+2)^3} + (x+20))}=\frac{(49+84+56)*(2+2)*(4+4)}{(7+2+9+9)*(27+27)}=\frac{189*4*8}{(7+2+9+9)(27+27)}=\frac{224}{54}=\frac{112}{27}$$
"""

x=Symbol('x')
a = (sqrt(x+2) - (x+20)**(1/3))/((x+9)**(1/4)-2)
a

print('Проверка через библиотеку sympy\n')
limit (a, x, 7)

print(112/27)

"""### $$г)\,\,\,\,\lim_{x\to 0} \frac{3x\,\mbox{tg}\,4x}{1-\cos4x}$$
$$$$

$$\lim_{x\to 0} \frac{3x\,\mbox{tg}\,4x}{1-\cos4x}=\frac{3}{2}\lim_{x \to 0}\frac{x\,\mbox{tg}\,4x}{\sin2x\sin2x}=\frac{3}{2}\lim_{x \to 0}\frac{x\,\mbox{tg}\,4x}{4x}=\frac{3}{2}$$
"""

x=Symbol('x')
a = (3*x*tan(4*x))/(1-cos(4*x))
a

print('Проверка через библиотеку sympy\n')
limit (a, x, 0)

"""### $$д^{**})\,\,\,\,\lim_{x\to 0} \frac{\sqrt2x^2\sin4x}{(1-\cos2x)^{\frac{3}{2}}}$$
$$$$
$$\lim_{x\to 0} \frac{\sqrt2x^2\sin4x}{(1-\cos2x)^{\frac{3}{2}}}=\Big(\frac{0}{0}\Big)=\lim_{x\to 0} \frac{\sqrt2x^2\sin4x}{\sqrt{8*\sin^6 x}}=\lim_{x\to 0} \frac{\sqrt2x^2\sin4x}{2\sqrt{2}|\sin^3 x|}=\lim_{x\to 0} \frac{(x^2)*2*\sin(2x)*\cos(2x)}{2*|\sin^3 x|} =\lim_{x\to 0} \frac{x^2*\sin(2x)}{|x^3|} = \lim_{x\to 0}\frac{2x^3}{|x^3|}$$

Насколько я понимаю, то предела в точке 0 не существует. Т.к. в определении предела, мы должны приближаться к одному числу. А здесь мы приближаемся справа к +2, а слева к -2.

### $$е)\,\,\,\,\lim_{x\to \infty} \Bigr(\frac{4x}{4x+3}\Bigl)^\frac{5x^2}{7x-1}$$
$$$$
$$\lim_{x\to \infty} \Bigr(\frac{4x}{4x+3}\Bigl)^\frac{5x^2}{7x-1}=(1)^{+\infty}=\lim_{x\to \infty} e^{\Bigl(\frac{-3}{4x+3}\Bigr)\frac{5x^2}{7x-1}}=\lim_{x\to \infty} e^{\Bigl(\frac{-15x^2}{(4x+3)(7x-1)}\Bigr)}=e^{\frac{-15}{28}}=\frac{1}{e^{\frac{15}{28}}}$$

### $$ж^*)\,\,\,\,\lim_{x\to +0} \frac{5^x-1}{x}$$

$$$$

$$\lim_{x\to +0} \frac{5^x-1}{x}=\Big(\frac{0}{0}\Big)$$
$$$$
$$5=e^{\ln5}$$
$$$$
$$5^x=e^{x\ln5}$$
$$$$
$$\sqsupset n = x\ln5$$
$$$$
$$=\lim_{n\to +0} \Big(\frac{e^{n}-1}{n}\Big)\ln5=\ln5$$

### $$з^*)\,\,\,\,\lim_{x\to +\infty} \frac{\ln(x^2-x+1)}{\ln(x^{10}+x+1)}$$

$$$$
$$\lim_{x\to +\infty} \frac{\ln(x^2-x+1)}{\ln(x^{10}+x+1)} =\Big(\frac{\infty}{\infty}\Big)= \lim_{x\to +\infty} \frac{2\ln(x) + \ln(1-\frac{1}{x}+\frac{1}{x^2})}{10\ln(x)+\ln(1+\frac{1}{x^9} + \frac{1}{x^{10}})} =  \lim_{x\to +\infty} \frac{2 + \frac{1}{\ln{x}} \ln(1-\frac{1}{x}+\frac{1}{x^2})}{10 + \frac{1}{\ln{x}}\ln(1+\frac{1}{x^9} + \frac{1}{x^{10}})} = \frac{1}{5} $$

__2*.__ На языке Python предложить алгоритм вычисляющий численно предел последовательности

### $$\lim_{n\to +\infty} \frac{n}{\sqrt[n]{n!}}$$

$$\forall\varepsilon>0\,\,\,\exists \delta(\varepsilon), \,\,\,\forall x\,\,\, |x-x_0|<\delta:|f(x)-A|<\varepsilon$$

Из определения, нам надо сразу явно задавать А. Не совсем понятно как это делать. Поэтому будем смотреть на последовательность. И тут практически скопирован код, который был показан на занятии.
Т.е. нам нужно вычислить такое значение f(x1)-f(x0), при котором эта разница будет неотличима от заданного эпсилон.
"""

import math
import sympy
import numpy as np
import scipy

eps = 0.000001

def limF(n):
    b = sympy.factorial(n)
    #print(type(b))
    c = 1/n
    return (n / pow(b, c))

n = 1
lim = 1
x0 = limF(n)

while lim > eps:
    n += 1
    x1 = limF(n)
    lim = abs(x1 - x0)
    x0 = x1

print (f'Численное значение предела: {x1}\n',f'Погрешность: {lim}\n', f'Число шагов: {n-1}')

"""Правда сработало только в случае использования sympy. Иначе ошибка переполнения для хоть чуть больших значений эпсилон. Дальше я попытался написать свою функцию факториала. И этот код даже работает, но выдаёт не ошибку, а просто 0 при больших значениях эпсилон. Не понимаю пока в каком типе считает sympy. Вроде он возвращает некое значение 'sympy.core.numbers.Integer'. В общем, решения этой задачи у меня нет."""

eps = 0.001

#n = int(input('n = '))
def factorial(n):
    temp = float(1)
    if (n == 0):
       return temp
    else:
        for i in range(1, n + 1):
            temp = float(temp) * i
        return temp

def limF(n):
    b = factorial(n)
    c = 1/n
    #print(type(b))
    return (n / pow(b, c))

n = 1
lim = 1
x0 = limF(n)
i = 0

while lim > eps:
    n += 1
    i += 1
    x1 = limF(n)
    lim = abs(x1 - x0)
    x0 = x1
    #print(i)

print (f'Численное значение предела: {x1}\n',f'Погрешность: {lim}\n', f'Число шагов: {n-1}')