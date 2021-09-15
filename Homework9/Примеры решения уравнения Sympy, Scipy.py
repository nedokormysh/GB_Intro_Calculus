from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt

def equations(p):
  n = p
  1/2*n**(1/2)
  return n
n = fsolve(equations, 42)
print(n)

from sympy.solvers import solve
from sympy import Symbol
n = Symbol('n')
solve(1/2*n**(1/2), n)

from sympy.solvers import solve
from sympy import Symbol
n = Symbol('n')
solve(-sqrt(n)/((n + 1)**2) + 1/(2*sqrt(n)*(n + 1)), n)

from math import cos
import scipy.optimize
def fun(y):
    x = y + 2*cos(y)
    return x
x = scipy.optimize.fsolve(fun, 0.2)
print (x)