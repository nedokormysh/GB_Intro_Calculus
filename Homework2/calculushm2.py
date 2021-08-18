# -*- coding: utf-8 -*-
"""CalculusHM2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bsbfGPgiiqALk3LnybiG2gR2LNc1v0-J

__1.__ Найти предел последовательности:

### $$а)\,\,\,\,\lim_{n\to \infty} \frac{(23-2n^2)(3n^2+17)^2}{4n^6+n-1}$$

### $$б)\,\,\,\,\lim_{n\to \infty} \frac{(97-2n)^3}{2n(3n^2+15)+8n}$$

### $$в)\,\,\,\,\lim_{n\to \infty} \frac{2n^3+13n(n+18)}{(27-n)(2n+19)^2}$$

### $$г)\,\,\,\,\lim_{n\to \infty} (\sqrt{n^2+1}-n)$$

### $$д)\,\,\,\,\lim_{n\to \infty} \frac{(-4)^n+5\cdot7^n}{(-4)^{n-1}+7^{n+2}}$$

### $$e)^*\,\,\,\,\lim_{n\to \infty} \Bigl(\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\frac{1}{3\cdot4}+...+\frac{1}{(n-1)\cdot n}\Bigr)$$
"""

from sympy import *
init_printing()

"""### $а)$
$$\lim_{n\to \infty} \frac{(23-2n^2)(3n^2+17)^2}{4n^6+n-1}=\Bigl(\frac{\infty}{\infty}\Bigr)=\frac{-2\cdot3^2}{4}=-\frac{9}{2}$$


"""

n=Symbol('n')
a = (23 - 2 * n**2) * (3 * n**2 + 17)**2/( 4 * n**6 + n + 1)
a

print('Проверка через библиотеку sympy')
limit (a, n, oo)

"""### $б)$
$$\lim_{n\to \infty} \frac{(97-2n)^3}{2n(3n^2+15)+8n}=\Bigl(\frac{\infty}{\infty}\Bigr)=\frac{(-2)^3}{2\cdot3}=-\frac{4}{3}$$
"""

n = Symbol('n')
a = (97 - 2 * n)**3 / (2 * n * (3 * n**2 + 15) + 8 * n)
a

print('Проверка через библиотеку sympy')
limit (a, n, oo)

"""### $в)$

$$\lim_{n\to \infty} \frac{2n^3+13n(n+18)}{(27-n)(2n+19)^2}=\Bigl(\frac{\infty}{\infty}\Bigr)=\frac{2}{-1\cdot2^2}=-\frac{1}{2}$$
"""

n = Symbol('n')
a = (2 * n**3 + 13 * n * (n + 18)) / ((27 - n) * ( 2 * n + 19)**2)
a

print('Проверка через библиотеку sympy')
limit (a, n, oo)

"""### $г)$
$$\lim_{n\to \infty} (\sqrt{n^2+1}-n)=\Bigl(\infty-\infty\Bigr)=\lim_{n\to \infty} (\sqrt{n^2+1}-n)\cdot\frac{\sqrt{n^2+1}+n}{\sqrt{n^2+1}+n}=\lim_{n\to \infty} \frac{n^2+1-n^2}{\sqrt{n^2+1}+n}=\lim_{n\to \infty} \frac{1}{\sqrt{n^2+1}+n}=0$$
"""

n = Symbol('n')
a = (n**2 + 1)**(1/2) - n
a

print('Проверка через библиотеку sympy')
limit (a, n, oo)

"""###$д)$

$$\lim_{n\to \infty} \frac{(-4)^n+5\cdot7^n}{(-4)^{n-1}+7^{n+2}}=\Bigl(\frac{\infty}{\infty}\Bigr)=\lim_{n\to \infty} \frac{(-4)^n+5\cdot7^n}{\Bigl(-\frac{1}{4}\Bigr)\cdot(-4)^n+49\cdot7^n}=\lim_{n\to \infty} \frac{7^n\cdot\Bigl(\Bigl(-\frac{4}{7}\Bigr)^n+5\Bigr)}{7^n\cdot\Bigl(\Bigl(-\frac{1}{4}\Bigr)\cdot\Bigl(-\frac{4}{7}\Bigr)^n+49\Bigr)}=\frac{5}{49}$$
"""

n = Symbol('n')
a = ((-4)**n + 5 * 7**n) / ((-4)**(n-1) + 7**(n+2))
a

print('Проверка через библиотеку sympy даёт ошибку')
#limit (a, n, oo)

"""###$е)$

$$e)^*\,\,\,\,\lim_{n\to \infty} \Bigl(\frac{1}{1\cdot2}+\frac{1}{2\cdot3}+\frac{1}{3\cdot4}+...+\frac{1}{(n-1)\cdot n}\Bigr)$$

аликвотные дроби

$$\frac{1}{n\cdot(n+1)}=\frac{1}{n}-\frac{1}{n+1}$$
$$$$
$$\frac{1}{1\cdot2}=\frac{1}{1}-\frac{1}{2}$$
$$$$
$$\frac{1}{2\cdot3}=\frac{1}{2}-\frac{1}{3}$$
$$$$
$$\frac{1}{3\cdot4}=\frac{1}{3}-\frac{1}{4}$$
$$$$
$$\frac{1}{4\cdot5}=\frac{1}{4}-\frac{1}{5}$$
$$$$

$$\lim_{n\to \infty} \Bigl(\frac{1}{1}-\frac{1}{2}+\frac{1}{2}-\frac{1}{3}+...+\frac{1}{n-1}-\frac{1}{n}\Bigr)=\lim_{n\to \infty} \Bigl(1-\frac{1}{n}\Bigr)=1$$

2. Представьте  1  в виде суммы трех рациональных дробей с разными знаменателями и числителем равным  1.

$$\frac{1}{n}=\frac{1}{n + 1}+\frac{1}{n\cdot(n+1)}$$

$$ 1 = \frac{1}{2} + \frac{1}{2} = \frac{1}{2} + \frac{1}{3} + \frac{1}{6}$$

3 ∗ . Тоже задание, только в виде суммы шести дробей.
$$ 1 = \frac{1}{2} + \frac{1}{2} = \frac{1}{2} + \frac{1}{3} + \frac{1}{6} = \frac{1}{2} + \frac{1}{4} + \frac{1}{12} + \frac{1}{7} + \frac{1}{42} = \frac{1}{2} + \frac{1}{4} + \frac{1}{12} + \frac{1}{8} + \frac{1}{56} + \frac{1}{42} $$

__4.__ Пользуясь критерием Коши, докажите сходимость последовательности:

### $$a_n=\frac{\sin1}{2}+\frac{\sin2}{2^2}+\frac{\sin3}{2^3}+..\frac{\sin n}{2^n}\,\,\,\,\,\Rightarrow$$

### $$\Bigl\{a_n\Bigr\}_{n=1}^\infty=\Bigl\{\frac{\sin1}{2}, \frac{\sin1}{2}+\frac{\sin2}{2^2}, ..., a_n,...\Bigr\}$$
$$$$

$$a_n = \Bigr|\frac{sin(1)}{2} + \frac{sin(2)}{2^2} + ... + \frac{sin(n)}{2^n}\Bigl|$$
$$$$
$$a_{n+k} = \Bigr|\frac{sin(1)}{2} + \frac{sin(2)}{2^2} + ... + \frac{sin(n+k)}{2^{n+k}}\Bigl|$$
$$$$
$$|a_n - a_{n+k}|=\Big|-\Big(\frac{sin(n + 1)}{2^{n + 1}} + \frac{sin(n + 2)}{2^{n +2}} + ... + \frac{sin(n+k)}{2^{n+k}}\Big)\Big|\leq$$
$$$$
$$\leq\frac{|sin(n + 1)|}{2^{n + 1}} + \frac{|sin(n + 2)|}{2^{n + 2}} + ... + \frac{|sin(n + k)|}{2^{n + k}}\leq\frac{1}{2^{n + 1}} + \frac{1}{2^{n + 2}} + ... + \frac{1}{2^{n + k}}<$$
$$$$
$$<\frac{1}{2^{n + 1}} + \frac{1}{2^{n + 2}} + ... + \frac{1}{2^{n + k}}+...=$$
$$$$
$$ = \frac{\frac{1}{2^{n+1}}}{1-\frac{1}{2}} = \frac{2}{2^{n+1}}= \frac{1}{2^n}<\frac{1}{2^{N(\varepsilon)}}=\varepsilon$$

$^*$ Какой член последовательности можно взять в качестве предела с точностью $\varepsilon=10^{-7}$?

$$\frac{1}{2^{N(\varepsilon)}}=\varepsilon \,\,\,\Rightarrow\,\,\, 2^{N(\varepsilon)}=\frac{1}{\varepsilon}\,\,\,\Rightarrow\,\,\, N(\varepsilon)=-\log_2 \varepsilon$$
"""

import math
eps = 0.0000001
N = -math.log(eps,2)

print (f'eps={eps}', f'N={N}')

n = int(N+1)

print (f'Потребуется взять элемент с номером a_{n} = {1/2**n}')

"""__5$^*$.__  Пользуясь критерием Коши, докажите расходимость последовательности:

### $$b_n=1+\frac{1}{2}+\frac{1}{3}+...+\frac{1}{n}\,\,\,\,\,\Rightarrow$$

### $$\Bigl\{b_n\Bigr\}_{n=1}^\infty=\Bigl\{1, 1+\frac{1}{2},1+\frac{1}{2}+\frac{1}{3}, ..., b_n,...\Bigr\}$$

Будем доказывать от противного, т.е. рассмотрим критерий расходимости.
### $$\exists\varepsilon>0\,\,\,\forall N(\varepsilon), \,\,\,\exists n>N(\varepsilon)\,\,\,\exists k\geq1:|b_n-b_{n+k}|\geq\varepsilon$$

$$b_n = 1+\frac{1}{2}+\frac{1}{3}+...+\frac{1}{n}$$
$$b_n = 1+\frac{1}{2}+\frac{1}{3}+...+\frac{1}{n} + ... + \frac{1}{n + k}$$
$$|b_n-b_{n+k}|=\Big|\frac{1}{n+1}+...+\frac{1}{n+k}\Big|\geq\frac{k}{n+k}\geq\varepsilon$$

Вроде бы всё, если я правильно понял, что необходимо сделать. Т.е. у нас осталось k элементов, каждый из которых больше либо равен 1/(n+k). И мы можем предъявить такие n, k и эпсилон, что неравенство выполняется.
"""