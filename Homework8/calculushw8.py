# -*- coding: utf-8 -*-
"""CalculusHW8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T-gTSiOlO5MS7FsY8xt8h10mtNSbE7wB
"""

!pip install numpy

!pip install scipy

!pip install math

"""__1.__ Вычислить неопределенный интеграл

### $$\int \frac{2x+3}{(x-2)(x+5)}\,dx$$


$$\frac{2x+3}{(x-2)(x+5)}=\frac{A}{x-2}+\frac{B}{x+5}$$

$$\frac{A}{x-2}+\frac{B}{x+5}=\frac{A(x + 5)+ B(x - 2)}{(x-2)(x+5)}$$

$$\begin{cases}
A+B=2 \\
5A-2B=3 \end{cases}\Rightarrow$$

$$\begin{cases}
A=1 \\
B=1
\end{cases}$$

Тогда:

$$\int\frac{2x+3}{(x-2)(x+5)}\,dx=\int\frac{1}{x-2}\,dx+\int\frac{1}{x+5}\,dx=\ln|x-2|+\ln|x+5|+C$$
"""

from sympy import *
init_printing()
x = Symbol('x')
f = (2 * x + 3)/((x - 2)*(x + 5))
f

integrate(f, x)

"""__2.__ Вычислить неопределенный интеграл

### $$\int e^{2x}\cos 3x\,dx$$


$$U=e^{2x}\Rightarrow\, dU=e^{2x}*2dx$$
$$dV=\cos 3xdx\,\,\,\,\,\Rightarrow\,\,\,\,\, V=\frac{1}{3}\sin 3x$$

$$$$
$$\int e^{2x}\cos 3x\,dx = e^{2x}\frac{\sin 3x}{3} - \frac{2}{3}\int e^{2x}\cdot \sin 3x\,dx = *$$
$$$$

$$U=e^{2x}\,\Rightarrow\, dU=2e^{2x}dx$$
$$dV=\sin 3xdx\,\,\,\,\,\Rightarrow\,\,\,\,\, V=-\frac{1}{3}\cos 3x$$

$$* = e^{2x}\frac{\sin 3x}{3} - \frac{2}{3} \Big( -\frac{1}{3} \cos 3x * e^{2x} - \int -\frac{1}{3} \cos 3x * 2 * e^{2x} \,dx = e^{2x}\frac{\sin 3x}{3} + \frac{2}{9}\cos 3x * e^{2x} - \frac{4}{9} \int \cos 3x * e^{2x} \,dx  $$

$$$$
Переносим интеграл в левую часть.
$$$$
$$\int e^{2x}\cos 3x\,dx + \frac{4}{9} \int \cos 3x * e^{2x} \,dx = e^{2x}\frac{\sin 3x}{3} + \frac{2}{9}\cos 3x * e^{2x}$$
$$$$
$$ 9 \int e^{2x}\cos 3x\,dx + 4 \int  e^{2x} \cos 3x \,dx =  3 e^{2x}\sin 3x + 2\cos 3x * e^{2x}$$
$$$$
$$ \int e^{2x}\cos 3x\,dx  = \frac{3 e^{2x}\sin 3x + 2\cos 3x * e^{2x}}{13} +C$$
"""

from sympy import *
init_printing()
x = Symbol('x')
f = exp(2 * x) * cos(3 * x)
f

integrate(f, x)

"""__3.__ Вычислить определенный интеграл

### $$\int\limits_0^{\ln2} xe^{-x}\,dx$$


$$\int\limits_0^{\ln2} xe^{-x}\,dx$$
$$U=x\,\,\,\,\,\Rightarrow\,\,\,\,\, dU=dx$$
$$dV=e^{-x}dx\,\,\,\,\,\Rightarrow\,\,\,\,\, V=-e^{-x}$$
$$\int xe^{-x}\,dx = -xe^{-x} + \int e^{-x}dx = -xe^{-x} + - e^{-x} + C$$
$$\int\limits_0^{\ln2} xe^{-x}\,dx= (-xe^{-x} + - e^{-x}) \bigg|_0^{ln2} = -ln2\cdot e^{-ln2} - e^{-ln2} - (0 - 1) =\\= -\frac{ln2}{2} - \frac{1}{2} + 1 = \frac{1 - ln2}{2}$$
"""

from sympy import *
init_printing()
x = Symbol('x')
f = x * exp(-x)
f

integrate(f,(x, 0, ln(2)))

"""__4.__ Вычислить несобственный интеграл

### $$\int\limits_2^{+\infty} \frac{dx}{x^2+x-2}$$

$$\int\limits_2^{+\infty} \frac{dx}{x^2+x-2}=\int\limits_2^{+\infty} \frac{dx}{(x - 1)(x + 2)}$$

$$$$
$$\frac{1}{(x - 1)(x + 2)} = \frac{A}{x - 1}+\frac{B}{x + 2}=\frac{A(x + 2)+B(x - 1)}{(x+2)(x-1)}$$
$$$$
$$\begin{cases}
A + B = 0 \\
2A + B = 1
\end{cases}\Rightarrow
$$

$$\begin{cases}
A = \frac{1}{3} \\
B = -\frac{1}{3} \\
\end{cases}
$$


$$\int \limits_2^{+\infty} \frac{dx}{x^2 + x - 2} = \frac {1}{3} \int \limits_2^{+\infty} \frac{dx}{x - 1} - \frac {1}{3} \int \limits_2^{+\infty} \frac{dx}{x + 2} = \frac{1}{3}\lim_{a\to +\infty}\int\limits_{2}^{a}\frac{dx}{x - 1} - \frac{1}{3}\lim_{a\to +\infty}\int\limits_{2}^{a}\frac{dx}{x + 2} = \frac{1}{3}\lim_{a\to +\infty}\ln|x - 1|\bigg|_2^{a} -\frac{1}{3}\lim_{a\to +\infty}\ln|x + 2|\bigg|_2^{a} = \frac{1}{3} (\lim_{a\to +\infty}\ln|a - 1| - \lim_{a\to +\infty}\ln|2 - 1|) -\frac{1}{3}( \lim_{a\to +\infty}\ln|a + 2| - \ln |2 + 2|) = \frac{1}{3} (\lim_{a\to +\infty}\ln|a - 1| - \lim_{a\to +\infty}\ln 1) -\frac{1}{3}( \lim_{a\to +\infty}\ln|a + 2| - \ln 4) = \frac{1}{3} ( \lim_{a\to +\infty}\ln|a - 1| - \lim_{a\to +\infty}\ln|a + 2|) = \frac{1}{3} \Big (\lim_{a\to +\infty} \ln \frac{|a - 1|}{|a + 2|} - ln4 \Big) = \frac{1}{3}(\ln1 - \ln4) = \frac{1}{3} \ln 4$$




"""

x = Symbol('x')
f = 1 / (x**2 + x - 2)
f

integrate(f,(x, 2, +oo))

"""__5*.__ Вычислить несобственный интеграл


### $$\int\limits_0^{1} \ln x\,dx$$

$$U = \ln x$$
$$dV = dx$$

$$dU = d\ln x = (\ln x)'dx = \frac{dx}{x}$$
$$V = x$$

$$$$

$$\int\limits_0^{1} \ln x\,dx = \lim_{\varepsilon\to 0} \int\limits_\varepsilon^{1}lnx dx = \lim_{\varepsilon\to 0} (xlnx - x)\bigg|_\varepsilon^{1} =\\= \lim_{\varepsilon\to 0} \Bigl(0-1-(\varepsilon  ln \varepsilon - \varepsilon)\Bigr) = -1 -\lim_{\varepsilon\to 0} \varepsilon ln \varepsilon +  \lim_{\varepsilon\to 0} \varepsilon = -1$$

"""

x = Symbol('x')
f = ln(x)
f

integrate(f,(x, 0, 1))