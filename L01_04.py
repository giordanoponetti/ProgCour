#	to solve a polynomial to variable x

from sympy.abc import x, y, z
from sympy import solve


f = x**3 + 3*x**2 + 5

print(solve(f,x))