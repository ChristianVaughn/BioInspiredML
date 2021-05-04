#import random
#import math
#import numpy as np
import matplotlib.pyplot as plt

T = 10000       #10k units
Tf = 0.1        #1/10th of a unit
k = 0.00001     #cooling factor (1/100k-th of a unit)

# for 2d plot of cooling schedule
iters = []
temps = []

i = 0
ppts = 0

iters.append(i)
temps.append(T)

while T > Tf:
    T = T / (1 + k*T) #cooling schedule (exponentially decreasing asymptotically)
    temps.append(T)
    ppts += 1
    i += 1
    iters.append(i)

print("# of plot points: ", ppts)
# show cooling schedule
plt.plot(iters, temps)
plt.xlabel("Iteration")
plt.ylabel("Temperature")
plt.show()
    