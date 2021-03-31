import random
import math
import numpy as np
import matplotlib.pyplot as plt
from functions import rastrigin

A = 10            # rastrigin constant
k = 0.00001       # cooling factor (very slow but standard)

# for plot points
arrX = []
arrY = []
arrZ = []

# Uniformly random selection (equal probability) v.s. normal random selection (normal distribution of selection probability)
# Rastrigin function bounds [-5.12, 5.12]
# (x,y) == s0
x = random.uniform(-5.12, 5.12)         # start x 
y = random.uniform(-5.12, 5.12)         # start y

T = 10000           # starting temperature: hyper-parameter (T_max)
Tf = 0.1            # terminal condition
neighbor_dist = 1   # the distance that a possible neighbor can have in x or y directions

# bounds of our 3d space
ptsX = np.linspace(-5.12, 5.12, 300)
ptsY = np.linspace(-5.12, 5.12, 300)
X, Y = np.meshgrid(ptsX, ptsY)
euclidSpace = np.vectorize(rastrigin)
Z = euclidSpace(X, Y, A)

# plotting the Rastrigin function and labeling axes
fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.65)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')


def getNeighborhood(current, fnLower, fnUpper): # creating random neighbor 
    if current - neighbor_dist > fnLower:
        lower = current - neighbor_dist
    else:
        lower = fnLower
        
    if current + neighbor_dist < fnUpper:
        upper = current + neighbor_dist
    else:
        upper = fnUpper
        
    return random.uniform(lower, upper)     # this is 's' picked from neighborhood between lower and upper

z = rastrigin(x, y, A)
print("Starting point on function: x =",x," y =",y," z =",z)

arrX.append(x)
arrY.append(y)
arrZ.append(z)
ax.plot(x, y, z, markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)

i = 0
ppts = 0
while T > Tf:
    # get a random neighbor from neighborhood (sNew)
    neighborX = getNeighborhood(x, -5.12, 5.12)
    neighborY = getNeighborhood(y, -5.12, 5.12)

    eDiff = z - rastrigin(neighborX, neighborY, A) # rastrigin == objective function, z == E(s)
    if eDiff > 0:   # if new == better then accept (eDiff <= 0 => no change or change in the wrong direction)
        x = neighborX
        y = neighborY
    else:   # if new != better then still accept but with a probability
        if random.uniform(0, 1) < math.exp(eDiff / T):    # Probability => random(1) < e^[ (E(s) - E(sNew)) / T ]
            x = neighborX
            y = neighborY
     
    z = rastrigin(x, y, A)
    if i % 1000000 < 10:
        print("Iteration ",i,": x =",x," y =",y," z =",z)  # to check cooling schedule scaling with iterations
        arrX.append(x)
        arrY.append(y)
        arrZ.append(z)  
        ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
        ppts += 1
    # decrement the temperature via slow cooling
    T = T / (1 + k*T) #cooling schedule - time variant temp. decreases over time
    i += 1

print("S.A. Optimizes to: x = ", x, " y = ", y, " z = ", rastrigin(x, y, A), " iterations = ", i)
print("Number of plot points: ", ppts)
# show the final graph
ax.plot(arrX, arrY, arrZ, color = 'b')
plt.show()