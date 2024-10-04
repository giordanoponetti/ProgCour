#	to compute physical numbers with errors and unit measurement


from uncertainties import ufloat
from pint import UnitRegistry
ureg = UnitRegistry()


# distance = 24.0 * ureg.meter
# time = 65.0 * ureg.second

distance = ureg.Quantity((12,.7),'meter')
time = ureg.Quantity((90,3),'seconds')

speed = distance / time

print(ufloat(speed.magnitude[0],speed.magnitude[1]), speed.units)


