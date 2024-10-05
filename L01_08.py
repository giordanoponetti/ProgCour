#	plots

from scipy.integrate import odeint
import pylab as plt 

def harmonic(state,t):
	position, speed = state
	return (speed, -position)


time = plt.linspace(0,10,100)
y0 = [0,1]

result = odeint(harmonic, y0=y0, t=time)

lines=plt.plot(time,result)
plt.legend(lines,['position','velocity'])

plt.show()