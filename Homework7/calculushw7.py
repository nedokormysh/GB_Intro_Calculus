# -*- coding: utf-8 -*-
"""CalculusHW7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rvx9EjGI7o7eug4aVQK_qDlXBpywhGYv

__1.__ Исследовать на условный экстремум функцию

### $$U=3-8x+6y,$$

если

### $$x^2+y^2=36$$
$$$$
$$L(x,y,\lambda)=3-8x+6y +\lambda \cdot (x^2+y^2-36)$$
$$$$
$$\begin{cases}
L'{x}=-8+\lambda \cdot2x=0,\\
L'{y}=6+\lambda \cdot2y=0,\\ 
L'_{\lambda}=x^2 + y^2-36=0 
\end{cases}$$

$$\begin{cases}
x=\frac{4}{\lambda},\\
y=-\frac{3}{\lambda}, \\
\Big(\frac{4}{\lambda}\Big)^2+\Big(-\frac{3}{\lambda}\Big)^2=36 
\end{cases}
$$

$$\begin{cases}
x=\frac{4}{\lambda},\\
y=-\frac{3}{\lambda}, \\
{\lambda}^2=\frac{25}{36} 
\end{cases}
$$

Две точки: 
$$\Big(\frac{24}{5},-\frac{18}{5},\frac{5}{6}\Big)$$ и $$\Big(-\frac{24}{5},\frac{18}{5},-\frac{5}{6}\Big)$$

$$$$
$$L_{xx}'' = 2\lambda$$
$$L_{xy}'' = 0$$
$$L_{x\lambda}'' = 2x$$
$$$$

$$L_{yy}'' = 2\lambda$$
$$L_{yx}'' = 0$$
$$L_{y\lambda}'' = 2y$$
$$$$

$$L_{\lambda\lambda}'' = 0$$
$$L_{\lambda x}'' = 2x$$
$$L_{\lambda y}'' = 2y$$
$$$$
$$\begin{pmatrix}
L''_{\lambda \lambda} & L''_{\lambda x} & L''_{\lambda y}\\ 
L''_{x \lambda} & L''_{xx} & L''_{xy}\\
L''_{y \lambda} & L''_{yx} & L''_{yy}\\
\end{pmatrix}\Rightarrow
\begin{pmatrix}
0 & 2x & 2y\\ 
2x & 2\lambda & 0\\
2y & 0 & 2\lambda\\
\end{pmatrix}$$
$$$$
$$\Delta=\begin{vmatrix}
0 & 2x & 2y\\ 
2x & 2\lambda & 0\\
2y & 0 & 2\lambda\\
\end{vmatrix}=
0\cdot
\begin{vmatrix}
2\lambda & 0\\
0 & 2y\\
\end{vmatrix}-2x\cdot
\begin{vmatrix}
2x & 0\\
2y & 2\lambda\\
\end{vmatrix}+2y\cdot
\begin{vmatrix}
2x & 2\lambda\\
2y & 0\\
\end{vmatrix} = -2x(2x2\lambda)+2y(-2y2\lambda) = -8x^2\lambda-8y^2\lambda = -8\lambda(x^2+y^2)=-288\lambda$$

а) $$\Big(\frac{24}{5},-\frac{18}{5},\frac{5}{6}\Big)$$
$$$$
$$\Delta<0$$
минимум
$$$$
б) $$\Big(-\frac{24}{5},\frac{18}{5},-\frac{5}{6}\Big)$$
$$$$
$$\Delta>0$$
максимум

__2.__ Исследовать на условный экстремум функцию

### $$U=2x^2+12xy+32y^2+15,$$

если

### $$x^2+16y^2=64$$

$$$$
$$L(x,y,\lambda)=2x^2+12xy+32y^2+15 +\lambda \cdot (x^2+16y^2-64)$$
$$$$

$$\begin{cases}
L'{x} = 4x + 12y +2x\lambda = 0,\\
L'{y} = 12x + 64y + 32y\lambda= 0,\\ 
L'_{\lambda} = x^2+16y^2-64 = 0 
\end{cases}$$

Корни найдены с помощью wolfram alpha.
Четыре точки: 
$$(-4\sqrt2;-\sqrt{2};-\frac{7}{2}), (4\sqrt2;\sqrt{2};-\frac{7}{2}) (-4\sqrt2;\sqrt{2};-\frac{1}{2}), (4\sqrt2;-\sqrt{2};-\frac{1}{2})$$

$$\lambda = \frac{-4x-12y}{2x}=\frac{-2x-6y}{x}$$
$$\lambda = \frac{-12x-64y}{32y}$$
$$$$
$$\frac{-2x-6y}{x} = \frac{-12x-64y}{32y}$$
$$$$
$$
\begin{cases}
\lambda = \frac{-4x-12y}{2x}=\frac{-2x-6y}{x}\\
\lambda = \frac{-12x-64y}{32y}\\
x^2+16y^2-64 = 0
\end{cases}$$
$$$$
$$
\begin{cases}
\lambda = \frac{-2x-6y}{x}\\
\frac{-2x-6y}{x} = \frac{-12x-64y}{32y}\\
x^2+16y^2-64 = 0
\end{cases}$$
$$$$
$$
\begin{cases}
\lambda = \frac{-2x-6y}{x}\\
32y(-2x-6y) = x(-12x-64y)\\
x^2+16y^2-64 = 0
\end{cases}$$
$$$$
$$
\begin{cases}
\lambda = \frac{-2x-6y}{x}\\
-64yx-192y^2 = -12x^2-64yx\\
x^2+16y^2-64 = 0
\end{cases}$$
$$$$
$$
\begin{cases}
\lambda = \frac{-2x-6y}{x}\\
16y^2 = x^2\\
x^2 + x^2-64 = 0
\end{cases}$$
$$$$
$$
\begin{cases}
\lambda = \frac{-2x-6y}{x}\\
16y^2 = x^2\\
x^2 = 32
\end{cases}$$

Четыре точки: 
$$(-4\sqrt2;-\sqrt{2};-\frac{7}{2}), (4\sqrt2;\sqrt{2};-\frac{7}{2}) (-4\sqrt2;\sqrt{2};-\frac{1}{2}), (4\sqrt2;-\sqrt{2};-\frac{1}{2})$$

$$$$
$$L_{xx}'' = 4 + 2\lambda$$
$$L_{xy}'' = 12$$
$$L_{x\lambda}'' = 2x$$

$$$$
$$L_{yy}'' = 64 + 32\lambda$$
$$L_{yx}'' = 12$$
$$L_{y\lambda}'' = 32y$$

$$$$
$$L_{\lambda\lambda}'' = 0$$
$$L_{\lambda x}'' = 2x$$
$$L_{\lambda y}'' = 32y$$

$$$$
$$\begin{pmatrix}
L''_{\lambda \lambda} & L''_{\lambda x} & L''_{\lambda y}\\ 
L''_{x \lambda} & L''_{xx} & L''_{xy}\\
L''_{y \lambda} & L''_{yx} & L''_{yy}\\
\end{pmatrix}\Rightarrow
\begin{pmatrix}
0 & 2x & 32y\\ 
2x & 4 + 2\lambda & 12\\
32y & 12 & 64 + 32\lambda\\
\end{pmatrix}$$
$$$$
$$\Delta=\begin{vmatrix}
0 & 2x & 32y\\ 
2x & 4 + 2\lambda & 12\\
32y & 12 & 64 + 32\lambda\\
\end{vmatrix}=
0\cdot
\begin{vmatrix}
4+ 2\lambda & 12\\
12 & 64 + 32\lambda\\
\end{vmatrix}-2x\cdot
\begin{vmatrix}
2x & 12\\
32y & 64 + 32\lambda\\
\end{vmatrix}+32y\cdot
\begin{vmatrix}
2x & 4 + 2\lambda\\
32y & 12\\
\end{vmatrix} = -2x(128x + 64\lambda - 384y) + 32y(24x-128y-64y\lambda) = -256x^2 - 128x^2\lambda + 768xy + 768xy - 4096y^2-2048y^2\lambda = -256x^2 - 128x\lambda + 1536xy - 4096y^2-2048y^2\lambda = -256(x^2 + 16y^2) - 128\lambda(x^2 + 16y^2) + 1536xy = -256\cdot64 - 128\lambda\cdot64 +  1536xy = -16384 - 8192\lambda + 1536xy$$
a) $$(-4\sqrt2;-\sqrt{2};-\frac{7}{2})$$
$$\Delta = -16384 + 28672 + 12288 > 0$$
максимум

б) $$(4\sqrt2;\sqrt{2};-\frac{7}{2})$$
$$\Delta = -16384 + 28672 + 12288 > 0$$
максимум

в) $$(-4\sqrt2;\sqrt{2};-\frac{1}{2})$$
$$\Delta = -16384 + 4096 - 12288 < 0$$
минимум

г) $$(4\sqrt2;-\sqrt{2};-\frac{1}{2})$$
$$\Delta = -16384 + 4096 - 12288 < 0$$
минимум

__3.__ Численно найти хотя бы один действительный корень системы нелинейных уравнений:
### $$\begin{cases}
   x^2-y^2+3xy^3-2x^2y^2+2x-3y-5=0 \\
   3y^3-2x^2+2x^3y-5x^2y^2+5=0
 \end{cases}$$
"""

from scipy.optimize import fsolve, broyden2
import math

def equations(p):
    x, y = p

    return ((x**2-y**2+3*x*(y**3) - 2*(x**2)*(y**2) + 2*x - 3*y - 5), (3*(y**3) - 2*(x**2) + 2*(x**3)*y - 5*(x**2)*(y**2) + 5))
 
# Численное решение системы уравнений
x, y =  fsolve(equations, (10, 10))
print (x, y)
x, y =  fsolve(equations, (1, 1))
print (x, y)
x, y =  fsolve(equations, (100, 100))
print (x, y)

"""__4*.__ Численно найти все $5$ действительных корней."""

# import numpy as np
# from scipy.optimize import fsolve, broyden2
# import math
def equations(p):
    x, y = p

    return ((x**2-y**2+3*x*(y**3) - 2*(x**2)*(y**2) + 2*x - 3*y - 5), (3*(y**3) - 2*(x**2) + 2*(x**3)*y - 5*(x**2)*(y**2) + 5))

solv = set()
for x in range(-20, 20, 3):
  for y in range(-20, 20, 3):
    (x,y), info, ier, mesg =  fsolve(equations, (x, y), full_output=True)
    # x, y = fsolve(equations, (x, y))
    # if (ier == 1): 
    #   solv.add((int(x*10**8)/10**8, int(y*10**8)/10**8))
    if (ier == 1):
      solv.add((round(x, 4), round(y, 4)) )
      

print(solv)

"""__5*.__ Даны две функции $y_{1}=f(x)$ и $y_{2}=g(x)$. Известно, что:

### $$f'(x)=\frac{1}{2}g(x)$$

### $$g'(x)=2-2f(x)$$

### $$f(0)=0$$

### $$g(0)=1$$

Восстановить функции $y_{1}=f(x)$ и $y_{2}=g(x)$ с помощью формулы:

### $$f(x+\Delta x) \approx f(x)+f'(x) \cdot \Delta x$$

на участке $[0, 20]$

В качестве решения построить график этих функций в одной системе координат.
"""

import numpy as np
from scipy.interpolate import splev, splrep


n = 50
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

print(f)
print(g)

from matplotlib import pylab as plt

plt.figure(figsize = (15, 6))
plt.axis([0, 20, -6, 8])

# plt.plot(x, f, c = 'b')
plt.plot(x, f, marker="x", label="f", ls="", c = 'b')
# plt.plot(x, g, c = 'g')
plt.plot(x, g, marker="o", ls="", label="g", c = 'r')
# plt.show()

splf = splrep(x, f)
# print(splf)
splg = splrep(x, g)

x2 = np.linspace(0, l, 200)
y2 = splev(x2, splf)
plt.plot(x2, y2, label="Кубический сплайн f", c = 'y')

x3 = np.linspace(0, l, 200)
y3 = splev(x3, splg)
plt.plot(x3, y3, label="Кубический сплайн g", c = 'g')
plt.legend()

"""__6**.__ Найти все корни уравнения:
    
### $$f(x)=g(x)$$

на участке $[0, 20]$

Где $y_{1}=f(x)$ и $y_{2}=g(x)$ - функции из предыдущего решения.
"""

# import numpy as np
# from scipy.optimize import fsolve, broyden2
# import math



def equations(p):
    x = p
    return (splev(x, splf)-splev(x, splg))

solv = set()
solvx = set()

for x in np.arange (0, l, h):
    x, info, ier, mesg =  fsolve(equations, x, full_output = True)
    if (ier == 1):
      solv.add(round(float(x), 8))
      solvx.add(int(x*10**8)/10**8)
    
print(solv)
print(solvx)