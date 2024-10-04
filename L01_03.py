#	to compute the symbolic second order derivative of variable x


from sympy.abc import x, y, z

f = x**3 + 5*y**2

print(f.diff(x,2))
