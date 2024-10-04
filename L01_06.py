#	to compute physical numbers with errors and unit measurement



from pint import UnitRegistry
ureg = UnitRegistry()


distance = 24.0 * ureg.meter
time = 65.0 * ureg.second

speed = distance / time

print(speed)


