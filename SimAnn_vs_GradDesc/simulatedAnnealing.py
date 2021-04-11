import random
import time
import numpy as np
import matplotlib.pyplot as plt
from functions import rastrigin
from coolingSchedules import *


# for plot points
arrX = []
arrY = []
arrZ = []


# for recording times and results
times = []
results = []


# hyper parameters and initializations
T0 = 10000           # starting temperature: hyper-parameter (T_max)
T = T0               # set our temperature cycle to begin at initial temperature
Tf = 0.0001          # terminal condition (non-zero temp to avoid a divide-by-zero error in cooling)
neighbor_dist = 1    # the distance that a possible neighbor can have in x or y directions
A = 10               # rastrigin constant
k = 0.001            # cooling factor (very slow but standard)


# bounds of our 3d space
ptsX = np.linspace(-5.12, 5.12, 300)
ptsY = np.linspace(-5.12, 5.12, 300)
X, Y = np.meshgrid(ptsX, ptsY)
euclidSpace = np.vectorize(rastrigin)
Z = euclidSpace(X, Y, A)

# plotting the objective function (Rastrigin), drawing its surface, and labeling axes
fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
# Rastrigin function global optima @ (x,y,z) = (0,0,0)

#this function prevents neighborhoods outside the bounds of the function and defines neighborhood
def getNeighborhood(current, fnLower, fnUpper): # creating random neighbor = neighbor(s)
    if current - neighbor_dist > fnLower:
        lower = current - neighbor_dist
    else:
        lower = fnLower
        
    if current + neighbor_dist < fnUpper:
        upper = current + neighbor_dist
    else:
        upper = fnUpper
        
    return random.uniform(lower, upper)     # this is 'S(new)' picked from neighborhood between lower and upper


# Begin the trials here:
trials = 1
for run in range(0, trials):
    # Uniformly random selection (equal probability) v.s. normal random selection (normalized bell curve distribution of selection probability)
    # Rastrigin function bounds [-5.12, 5.12],  (x,y) == s0 
    x = random.uniform(-5.12, 5.12)         # start x 
    y = random.uniform(-5.12, 5.12)         # start y
    z = rastrigin(x, y, A)
    print("Starting point on function: x =",x," y =",y," z =",z)  
    arrX.append(x)
    arrY.append(y)
    arrZ.append(z)
    ax.plot(x, y, z, markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
    
    # start the algorithm and timer
    begTime = time.perf_counter()
    i = 0
    ppts = 0
    while T > Tf:   # terminal condition is a near zero temperature
        
        # decrement the temperature via slow cooling
        #T = T / (1 + k*T) #cooling schedule - time variant temperature that decreases over time
        T = logarithmic_mult(T, i)
        #T = linear(T0, i)
        #T = exponential(T0, i)
        #T = quadratic_mult(T, i)
        #T = stun(T, i, fx, fx0)
        # get a random neighbor from neighborhood (sNew)
        
        
        neighborX = getNeighborhood(x, -5.12, 5.12)
        neighborY = getNeighborhood(y, -5.12, 5.12)
    
        eDiff = z - rastrigin(neighborX, neighborY, A) # rastrigin == objective function, z == E(s)
        if eDiff > 0:   # if new == better then accept (eDiff <= 0 => no change or change in the wrong direction)
            x = neighborX
            y = neighborY
            fx0 = rastrigin(x, y, A)  #this is best so far so saved to fx0 to be passed to STUN cooling method
        else:   # if new != better then still accept but with a diminishing probability
            if random.uniform(0, 1) < math.exp(eDiff / T):    # Probability = random(1) < e^[ (E(s) - E(sNew)) / T ]
                x = neighborX
                y = neighborY
         
        z = rastrigin(x, y, A)  # fx saved to be passed to STUN cooling method
        arrX.append(x)
        arrY.append(y)
        arrZ.append(z) 
    #needing to minimize plot points for readability and computation time
        #if i % 1000 == 5:  
        print("Iteration ",i,": x =",x," y =",y," z =",z)  # to check cooling schedule scaling with iterations 
        ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
        ppts += 1
    
        i += 1
        
    # finish algorithm and stop timer
    endTime = time.perf_counter()
    totalTime = endTime - begTime

    #store results and run times to aggregate and analyze data
    z = rastrigin(x, y, A)
    results.append((x, y, z))
    times.append(totalTime)
    print("***********************************************************************************************************************************")
    print("Simulated Annealing algorithm Optimizes to: x = ", x, " y = ", y, " z = ", rastrigin(x, y, A), " iterations = ", i)
    print("Number of plot points: ", ppts)
    print("Total computational time: ", totalTime, "sec.")
    print("***********************************************************************************************************************************")

# show the final graph
print("The average ")
ax.plot(arrX, arrY, arrZ, color = 'b')
plt.show()
######################## END PROGRAM & BEGIN DATA RECORDING ######################## 


# **ECLIPSE TIP: Press 'CTRL' + '/' to comment and uncomment multiple lines of code!

# to save data to an excel spreadsheet of format .xls
# import xlwt 
# from xlwt import Workbook 
 #
# wb = Workbook() 
# sheet1 = wb.add_sheet('simulated_annealing_rastrigin')
# i = 0
#
# sheet1.write(0, 1, "Results")
# sheet1.write(0, 2, "Times")
#
# for wr in results:
    # lbl = "Run #: %s" % i
    # sheet1.write(i+1, 0, lbl)
    # sheet1.write(i+1, 1, wr)
    # sheet1.write(i+1, 2, times[i])
    # i += 1
    #
# wb.save('simulated_annealing_rastrigin.xls')
# print("File saved (over) as:  \"simulated_annealing_rastrigin.xls\"")