from coolingSchedules import *
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.interpolate import make_interp_spline


A = 10          #rastrigin factor
T0 = 10000      #10k units
T = T0          #set temperature cycle to begin @ initial temperature: T0
Tf = 0.1        #1/10th of a unit
k = 0.00001     #cooling factor (1/100k-th of a unit)

# for 2d plot of cooling schedule
iters = []
temps = []

i = 0
ppts = 0

iters.append(i)
temps.append(T)


# one dimensional rastrigin function to visualize the STUN cooling schedule
# def rast_1d(x, A):
    # return A + x**2 - A*math.cos(math.pi*x)
# fig2 = plt.figure()
# Y = rast_1d()

while T > Tf:
    #T = lundyMees(T) # Lundy & Mees (L&M) cooling schedule model
    # T = logarithmic_mult(T, i)
    # T = linear(T0, i)
    # T = exponential(T0, i)
    T = quadratic_mult(T, i)
    #T = stun(T, i, T, T) 

    ppts += 1
    i += 1
    iters.append(i)
    temps.append(T)
    plt.plot(i, T, markerfacecolor='c', markeredgecolor='c', marker='o', markersize=0.5)

print("# of plot points: ", ppts)
# show cooling schedule
x = np.array(iters)
y = np.array(temps)

# spline for smoothing out graph
xSmooth = np.linspace(x.min(), x.max(), 100)
spl = make_interp_spline(x, y, k=1)
ySmooth = spl(xSmooth)
plt.plot(xSmooth, ySmooth, color='c')
plt.grid(True)
###*** TITLES ***###
# plt.title("Lundy & Mees Cooling Schedule", fontsize=14)
# plt.title("Logarithmic Multiplicative Cooling Schedule  k = 0.01", fontsize=14)
# plt.savefig("LogMultCS_k0.01.png")
# plt.title("Linear Cooling Schedule  k = 1", fontsize=14)
# plt.savefig("LinearCS_k1.png")
# plt.title("Exponential Cooling Schedule  k = 0.8", fontsize=14)
# plt.savefig("ExponentialCS_k0.8.png")
plt.title("Quadratic Multiplicative Cooling Schedule  k = 0.00001", fontsize=14)
plt.savefig("QuadMultCS_k0.00001.png")
# plt.title("Stochastic Tunneling Cooling Schedule", fontsize=14)
#####################
plt.xlabel("Temp. Cycles (t)")
plt.ylabel("Temperature (T)")
plt.show()


    