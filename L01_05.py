#	to compute operations where numbers have uncertainties

from uncertainties import ufloat

x = ufloat(3,0.1)
y = ufloat(2,0.5)

print((x+y)/x)