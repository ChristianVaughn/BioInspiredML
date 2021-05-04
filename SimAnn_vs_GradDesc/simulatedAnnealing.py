import random
import time
import numpy as np
import matplotlib.pyplot as plt

from functions import rastrigin
from coolingSchedules import *
from math import sqrt

# for all plot points across all runs
allXs = []
allYs = []
allZs = []

# for recording times and results (used to calculate averages)
times = []
results = []

# Globals
A = 10      # rastrigin constant

# bounds of our 3d space
ptsX = np.linspace(-5.12, 5.12, 300)
ptsY = np.linspace(-5.12, 5.12, 300)
X, Y = np.meshgrid(ptsX, ptsY)
euclidSpace = np.vectorize(rastrigin)
Z = euclidSpace(X, Y, A)

# plotting the objective function (Rastrigin), drawing its surface, and labeling axes
plt.rcParams["figure.figsize"] = (10, 10)
fig1 = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')



###########################  FUNCTION DEFINITIONS  #################################################################
# Function prevents neighborhoods outside the bounds of the function and defines a neighborhood within it
def getNeighborhood(current, fnLower, fnUpper): # creating random neighbor = neighbor(s)
    if current - neighborD > fnLower:
        lowerN = current - neighborD
    else:
        lowerN = fnLower 
    if current + neighborD < fnUpper:
        upperN = current + neighborD
    else:
        upperN = fnUpper       
    return random.uniform(lowerN, upperN)     # this is 'S(new)' picked from neighborhood between lowerN and upperN

# Function to plot each point 
def plotPoint(x, y, z, i, color, size, pltPts):
    # append all points regardless of whether we plot them or not
    arrX.append(x)
    arrY.append(y)
    arrZ.append(z)
    # determine which points to plot
    if(i == 0):
        print("============================================================================")
        print("Starting point on function: (x =", x, ", y =", y, ", z =", z, ")")
        print("============================================================================") 
        ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=size)
        pltPts += 1
    #elif((i > 0) and (i % 100000 == 1)):  # Lundy & Mees conditional
    elif((i > 0) and (i % 100 == 1)):  # logarithmic multiplicative conditional
    #elif((i > 0) and (i % 1000 == 1)):  # linear conditional
    #elif((i > 0) and (not ptFinal)):  # exponential conditional
    #elif(i > 0):  # quadratic multiplicative conditional
    #elif((i > 0) and (i % 100 == 10^i)):  # stochastic tunneling conditional
        print("Point ", i+1, ":  (x =",x, " y =", y, " z =", z,")")
        ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=size)
        pltPts += 1
    elif(ptFinal):
        print("Simulated Annealing algorithm Optimizes to:  x = ", x, " y = ", y, " z = ", z, " after ", i, "iterations")
        ax.plot(x, y, z, markerfacecolor=color, markeredgecolor=color, marker='o', markersize=size)
        pltPts += 1

###########################  End of Functions  #####################################################################





# Start Grand Total timer for all trials
gtTimeBeg = time.perf_counter()
#################################** BEGIN TRIALS HERE **#################################
trials = 1                                      
#########################################################################################
for trial in range(0, trials):
    # hyper parameters and initializations
    T0 = 10000           # starting temperature: hyper-parameter (T_max)
    T = T0               # set our temperature cycle to begin at initial temperature
    Tf = 0.01            # terminal condition (close-to-zero temp. to avoid a divide-by-zero error in cooling)
    neighborD = 1        # the distance that a possible neighbor can have in both the x and y directions
    fx = 0               # current functional evaluation for STUN cooling schedule
    fx0 = 0              # previous functional evaluation for STUN cooling schedule
    
    # Controls 
    i = 0               # iterator to control temperature cycle
    pltPts = 0          # accumulator to test # of plot points that are being produced
    ptFinal = False     # flag for determining if final point in plotPoint(..) function
    
    # for plot points within one trial of the algorithm
    arrX = []
    arrY = []
    arrZ = []
    
    
    # Uniformly random selection (equal probability) utilized over normal random selection (normalized bell curve distribution of selection probability)
    # Rastrigin function bounds [-5.12, 5.12]. Our point (x,y) == s0 
    x = random.uniform(-5.12, 5.12)         # start x 
    y = random.uniform(-5.12, 5.12)         # start y
    z = rastrigin(x, y, A) # fx0 = ... best point so far for STUN cooling, z-value necessary otherwise

    plotPoint(x, y, z, i, "black", 7, pltPts) #initial plot point for current trial
    
    # Start Algorithm and individual timer
    begTime = time.perf_counter()
    while T > Tf:   # terminal condition is a near zero temperature
        
        # Decrement the temperature via cooling schedule
        #T = lundyMees(T)             # Lundy & Mees (L&M) cooling schedule model
        T = logarithmic_mult(T, i)
        #T = linear(T0, i)
        #T = exponential(T0, i)
        #T = quadratic_mult(T, i)
        #T = stun(T, i, fx, fx0)       
        
        # get a random neighbor from neighborhood (sNew)
        neighborX = getNeighborhood(x, -5.12, 5.12)
        neighborY = getNeighborhood(y, -5.12, 5.12)
    
        eDiff = z - rastrigin(neighborX, neighborY, A) # rastrigin == objective function, z == E(s)
        if eDiff > 0:   # if new == better then accept (eDiff <= 0 implies no change or change in the wrong direction)
            x = neighborX
            y = neighborY
            fx0 = rastrigin(x, y, A)  # this is the best so far. Thus we save it to fx0 to be passed to STUN cooling method
        else:   # if new != better then we still accept but with a diminishing probability
                x = neighborX
                y = neighborY

        z = rastrigin(x, y, A)  # fx = ... saved to be passed to STUN cooling method
             
        i += 1   
        plotPoint(x, y, z, i, 'blue', 4, pltPts)            
        pltPts += 1
        ### END of ALGORITHM as While Loop
    
    
    # Finish algorithm, stop timer, get total time for one trial
    endTime = time.perf_counter()
    totalTime = endTime - begTime

    # Mark final point of current trial. Flip flag
    ptFinal = True
    z = rastrigin(x, y, A)
    plotPoint(x, y, z, i, "green", 7, pltPts) 
    
    # Store results and trial times to aggregate and analyze data
    distFromOptima = sqrt(x**2 + y**2 + z**2)
    results.append(distFromOptima)
    times.append(totalTime)
    
    print("Trial #: ", trial)
    print("Simulated Annealing algorithm Optimizes to: x = ", x, " y = ", y, " z = ", z, " after ", i, "iterations")
    print("Distance from global optima: ", distFromOptima)
    print("Number of plot points: ", pltPts)
    print("Total computation time: ", totalTime, "sec.")
    print("***********************************************************************************************************************************")
### END # OF TRIALS as For Loop

# Grand Total time of all trials (in minutes)
gtTotTime = (time.perf_counter() - gtTimeBeg) / 60

# Calculate accuracy (in %) according to a distance of 1 unit away from global optima       
numAccurate = 0
accPercent = 0
for acc in results:
    if acc <= 1.0:
        numAccurate += 1     
accPercent = (numAccurate / trials)*100

# connect the dots and plot the global optima in RED. Rastrigin function global optima in 3D @ (x,y,z) = (0,0,0)
ax.plot(arrX, arrY, arrZ, color = 'c')
ax.plot(0, 0, 0, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=8)
  
# titles for each plot
# plt.title("Simulated Annealing Lundy & Mees Cooling Method", fontsize=14, pad=10.0)
plt.title("Simulated Annealing Logarithmic Multiplicative Cooling", fontsize=14, pad=10.0)
plt.savefig("SA_LogMult_CS_k0.01.png")
# plt.title("Simulated Annealing Linear Cooling Schedule", fontsize=14, pad=10.0)
# plt.savefig("SA_Linear_CS_k0.01.png")
# plt.title("Simulated Annealing Exponential Cooling Schedule", fontsize=14, pad=10.0)
# plt.title("Simulated Annealing Quadratic Multiplicative Cooling Schedule", fontsize=14, pad=10.0)
# plt.title("Simulated Annealing Stochastic Tunneling Cooling Schedule", fontsize=14, pad=10.0)
  
# for displaying average results
avgDistFromOpt = sum(results) / len(results)
avgTime = sum(times) / len(times)
print("===================================================")
print("The average and global statistics across all runs: ")
print("===================================================")
print("Average distance from optima: ", avgDistFromOpt, "units")
print("Average computation time: ", avgTime, "sec")
print("Grand Total Computation time: ", gtTotTime, "min")
print("Number of trials ran: ", trials)
print("Total plot points taken: ", pltPts)
print("Accuracy Percentage across all trials: ", accPercent, "%")
# show the final graph
plt.show()