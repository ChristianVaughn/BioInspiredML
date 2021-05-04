import numpy as np
import matplotlib.pyplot as plt
from functions import *

# for plot points
xarr=[]
yarr=[]
zarr=[]

### THESE COMMENTS CAN BE REMOVED AS I ONLY NEEDED THEM TO REFER BACK TO FOR MY OWN UNDERSTANDING ###

# learning rate can be considered a meta-heuristic like cooling schedule in S.A.
# returns the selected value of the learning rate
def simpleLR(value):
    return value

# scaling learning rate takes the initial value and reduces it based on the given rate as the iterations are increasing
# for example:
# learning rate = 0.5
# reduction = 10% or 0.1
# rate = 10 iterations
# 
# On the first 10 iterations the learning rate will be 0.5.
# On the next 10 it will be reduced by (0.1 x 1 x 0.5) = 0.05 so, lr = 0.45
def lrScaling(value, iteration, reduction, rate):
    step = int(iteration/rate)
    return value - step*reduction*value

# cosine learning rate returns the value of the cosine (decreasing) learning rate  on
# the given iteration based on the given period (maximum number of iterations).
# t is the iteration number and T is the period
def lrCosine(value, t, T):
    return value*(1 + math.cos(math.pi*t / T)) / 2

# periodic learning rate consists of a number of cosine cycles on a given period
# i is the iteration number, T is the period and M are the cycles
def lrPeriodic(value, t, T, M):
    return value*(1 + math.cos(math.pi*((t - 1) % (int(T/M) + 1)) / (int(T/M) + 1))) / 2

xvals = np.linspace(-2, 2, 30)
yvals = np.linspace(-2, 2, 30)

X, Y = np.meshgrid(xvals, yvals)
mc = np.vectorize(rosenbrock)
Z = mc(X,Y)

# plotting the function
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.65)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# gradient descent algorithm
x = 2
y = -2
z = rosenbrock(x, y)
ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
print("Initial guess: x =",x," y =",y," z =",z)
 
xarr.append(x)
yarr.append(y)
zarr.append(z)
 
i = 1
while z > 0.00001:
    a = simpleLR(0.0001)
    x = x - a*rosenbrock_dx(x, y)
    y = y - a*rosenbrock_dy(x, y)
    z = rosenbrock(x, y)
    ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
    print("Iteration ",i,": x =",x," y =",y," z =",z)
    print("Learning rate is ", a)
      
    if i == 1000:   # stop after a
        break       # thousand iterations
    xarr.append(x)
    yarr.append(y)
    zarr.append(z)
    i+=1

ax.plot(xarr, yarr, zarr, color='b')
plt.show()