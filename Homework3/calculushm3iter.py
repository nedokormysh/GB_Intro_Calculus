import math
import sympy


eps = 0.000001

# n = int(input('n = '))
def factorial(n):
    temp = 1
    if (n == 0):
       return temp
    else:
        for i in range(1, n + 1):
            temp = temp * i
            return temp


def limF(n):
    b = sympy.factorial(n)
    c = 1/n
    #print(type(b))
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

# def f(n):
#     return n / pow(sympy.factorial(n), 1 / n)
#
# eps = 10 ** -7
# i = 1
# n = 1
# x0 = f(n)
# while True:
#     i += 1
#     n += 1
#     x1 = f(n)
#     if abs(x0 - x1) <= eps:
#         break
#     x0 = x1
# print(f'n_iter: {i}')
# print(f'f(n) = {x0}')