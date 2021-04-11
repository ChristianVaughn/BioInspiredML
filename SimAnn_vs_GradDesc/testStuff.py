from coolingSchedules import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

T0 = 10000      #10k units
T = T0          #set temperature cycle to begin @ initial temperature: T0
Tf = 0.1        #1/10th of a unit
#k = 0.00001     #cooling factor (1/100k-th of a unit)

# for 2d plot of cooling schedule
iters = []
temps = []

i = 0
ppts = 0

iters.append(i)
temps.append(T)

while T > Tf:
    #T = T / (1 + k*T) #cooling schedule (exponentially decreasing asymptotically)
    #T = logarithmic_mult(T, i)
    #T = linear(T0, i)
    #T = exponential(T0, i)
    T = quadratic_mult(T, i)
    #T = stun(T, i, T, T)    
    ppts += 1
    i += 1
    iters.append(i)
    temps.append(T)
    plt.plot(i, T, markerfacecolor='c', markeredgecolor='c', marker='o', markersize=3)

print("# of plot points: ", ppts)
# show cooling schedule
x = np.array(iters)
y = np.array(temps)

# spline for smoothing out graph
xSmooth = np.linspace(x.min(), x.max(), 100)
spl = make_interp_spline(x, y, k=2)
ySmooth = spl(xSmooth)
plt.plot(xSmooth, ySmooth)
plt.grid(True)
plt.xlabel("Iterations (k)")
plt.ylabel("Temperature (T)")
plt.show()
    