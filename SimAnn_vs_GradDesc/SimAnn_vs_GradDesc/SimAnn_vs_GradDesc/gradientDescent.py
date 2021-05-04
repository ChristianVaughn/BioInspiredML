import random
import time
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from functions import *
from learningRates import *


# global variables and constants
A = 10

# for plot points
arrX = []
arrY = []
arrZ = []

# for recording times and results
times = []
results = []

# bounds of our 3D space
ptsX = np.linspace(-5.12, 5.12, 300)
ptsY = np.linspace(-5.12, 5.12, 300)
X, Y = np.meshgrid(ptsX, ptsY)
euclidSpace = np.vectorize(rastrigin)
Z = euclidSpace(X, Y, A)

# plotting the objective function: Rastrigin, drawing its surface, and labeling axes
plt.rcParams["figure.figsize"] = (10, 10)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

################################# FUNCTION TO PLOT POINTS OF ALGORITHIM ######################
def plotPoint(x, y, z, i, color): 
    arrX.append(x)
    arrY.append(y)
    arrZ.append(z)

    if (stagnation >= stagnantMax or i >= itersMax):
        #ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=5)
        print("Ending point on function: x =", x," y =", y," z =", z)
    else:
        #ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=3)
        print("Point ", i+1, "on function: x =", x," y =", y," z =", z)
################################# END FUNCTION ################################################

# grand total timer for all trials
gtTimeBeg = time.perf_counter()


#################################** BEGIN TRIALS HERE **#################################
trials = 100
for trial in range(0, trials):
    
    # iteration control and terminal condition
    i = 0
    ppts = 0
    stagnation = 0
    stagnantMax = 5
    itersMax = 1000
    
    # learning rate parameters
    T = 0.4             # for cosine and periodic LRs: this is the period
    M = 0.18            # for periodic LR: this is the cycle 
    reduction = 0.1     # for scaling LR: factor to reduce the LR by
    rate = 10           # for scaling LR: number of iterations at which the learning rate is the same 
    P = 0.9             # for momentum LR: the weight between average of previous values and current = new weighted average
    k = 0.001           # learning factor
    dX = 0              # past derivation for computing momentum with respect to X
    dY = 0              # past derivation for computing momentum with respect to Y
    
    # for plot points within one trial of the algorithm
    arrX = []
    arrY = []
    arrZ = []
    
    # initial point
    x = random.uniform(-5.12, 5.12)         # start x 
    y = random.uniform(-5.12, 5.12)         # start y  
    z = rastrigin(x, y, A)                  # start z
    
    # update point arrays
    arrX.append(x)
    arrY.append(y)
    arrZ.append(z)
    
    # plot the starting point per trial
    #ax.plot(x, y, z, markerfacecolor='k', markeredgecolor='k', marker='o', markersize=5)
    print("Starting point on function: x =", x," y =", y," z =", z)
    ppts += 1
    

     
    # start the Gradient Descent algorithm and timer
    begTime = time.perf_counter()
    while z > 0.00001: # while our gradient has not reached near zero
        LR = lrStatic(k)                             # flat learning rate
        # LR = lrScaling(k, i, reduction, rate)        # scaling learning rate params:(k, i, reduction, rate) 
        # LR = lrCosine(k, i, T)                       # scaling learning rate params:(k, i, T)
        # LR = lrPeriodic(k, i, T, M)                  # periodic learning rate params:(k, t, T, M)
        
        # MOMENTUM BASED function calls to learning rate
        dX = P*dX + (1-P)*rastrigin_ddx(x, A)
        dY = P*dY + (1-P)*rastrigin_ddy(y, A) 
             
        # MOMENTUM BASED update equations
        x = x - LR*dX # for updating x via momentum LR
        y = y - LR*dY # for updating y via momentum LR
        
        # ALL OTHER gradient descent update equations
        # x = x - LR*rastrigin_dx(x, A)
        # y = y - LR*rastrigin_dy(y, A) 
        
        # print("**[Learning Rate (X): ", dX, "]   [Learning Rate (Y)", dY, "]    I:", i, "\n")  
        z = rastrigin(x, y, A)
        

        # if (i > 1 and arrZ[i] == arrZ[i-1]):
            # stagnation += 1
            # print("    **stagnating...")
        # else:
            # stagnation = 0 # reset stagnation value (we want 5 consecutive unchanging z-values
        # if stagnation == stagnantMax:
        if i == itersMax:   # stop after maximum alloted iterations
            plotPoint(x, y, z, i, 'r')
            ppts += 1
            break
        
        # otherwise plot the points in blue like normal
        plotPoint(x, y, z, i, 'b')
        i += 1
        ppts += 1
        ### END WHILE LOOP / END OF ALGO
        
    # finish algorithm and stop timer
    endTime = time.perf_counter()
    totalTime = endTime - begTime

    # store results and trials times to aggregate and analyze data
    distFromOptima = sqrt(x**2 + y**2 + z**2)
    results.append(distFromOptima)
    times.append(totalTime)
    print("***********************************************************************************************************************************")
    print("Gradient Descent algorithm Optimizes to: x = ", x, " y = ", y, " z = ", z, " after", i,"iterations")
    print("Distance from global optima:", distFromOptima)
    print("Number of plot points:", ppts)
    print("Total computation time:", totalTime, "sec.")
    print("***********************************************************************************************************************************")
### END FOR LOOP / END # OF TRIALS

# grand total time of all trials
gtTotTime = (time.perf_counter() - gtTimeBeg) / 60


# get the percentage of accuracy according to LR distance of 1 from global optima       
numAccurate = 0
accPercent = 0
j = 0
for acc in results:
    if acc <= 1.0:
        numAccurate += 1
        print("Trial #:", j, "was accurate. Distance from global optima =", acc) 
    j += 1    
accPercent = (numAccurate / trials)*100

# connect the dots & plot the global optima in green
#ax.plot(arrX, arrY, arrZ, color = 'c')
#ax.plot(0, 0, 0, markerfacecolor='g', markeredgecolor='g', marker='o', markersize=8)
  
# titles for each plot
# plt.title("Gradient Descent Static Learning Rate", fontsize=14, pad=10.0)
# plt.title("Gradient Descent Scaling Learning Rate", fontsize=14, pad=10.0)
# plt.title("Gradient Descent Cosine-Based Learning Rate", fontsize=14, pad=10.0)
# plt.title("Gradient Descent Periodic (per-Cycle) Learning Rate", fontsize=14, pad=10.0)
plt.title("Gradient Descent with Damping LR & Momentum", fontsize=14, pad=10.0)

# for displaying average results
avgDistFromOpt = sum(results) / len(results)
avgTime = sum(times) / len(times)

print("===================================================")
print("The average and global statistics across all runs: ")
print("===================================================")
print("Average distance from optima:", avgDistFromOpt, "units")
print("Average computation time:", avgTime, "sec")
print("Grand Total Computation time:", gtTotTime, "min")
print("Number of trials ran:", trials)
print("Total plot points taken:", ppts)
print("Accuracy Percentage across all trials:", accPercent, "%")
# show the final graph
#plt.show()