import random
import time
import numpy as np
import matplotlib.pyplot as plt

from functions import *
from learningRates import *


A = 10  # rastrigin constant

# for plot points
arrX = []
arrY = []
arrZ = []

# for recording times and results
times = []
results = []

# bounds of our 3D space
# ptsX = np.linspace(-2, 2, 30)
# ptsY = np.linspace(-2, 2, 30)
ptsX = np.linspace(-5.12, 5.12, 300)
ptsY = np.linspace(-5.12, 5.12, 300)
X, Y = np.meshgrid(ptsX, ptsY)
#euclidSpace = np.vectorize(rosenbrock)
euclidSpace = np.vectorize(rastrigin)
Z = euclidSpace(X, Y, A)

# plotting the objective function (Rastrigin / Rosenbrock), drawing its surface, and labeling axes
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno', alpha=.2)
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# initial conditions
x = random.uniform(-5.12, 5.12)         # start x 
y = random.uniform(-5.12, 5.12)         # start y
z = rastrigin(x, y, A)
########
# x = 2
# y = -2
#z = rosenbrock(x, y)

ax.plot(x, y, z, markerfacecolor='g', markeredgecolor='g', marker='o', markersize=5)
print("Starting point on function: x =",x," y =",y," z =",z)

arrX.append(x)
arrY.append(y)
arrZ.append(z)
 
# start the Gradient Descent algorithm and timer
begTime = time.perf_counter()
i = 1
ppts = 0
while z > 0.00001: #while we have not reached zero
    a = simpleLR(0.0001)
    # x = x - a*rosenbrock_dx(x, y)
    # y = y - a*rosenbrock_dy(x, y)
    # z = rosenbrock(x, y)
    
    x = x - a*rastrigin_dx(x, y, A)
    y = y - a*rastrigin_dy(x, y, A)
    z = rastrigin(x, y, A)
 
    if i == 1000:   # stop after one thousand iterations
        ax.plot(x, y, z, markerfacecolor='r', markeredgecolor='r', marker='o', markersize=5)
        ppts += 1
        print("Iteration ", i, ": x =", x, " y =", y, " z =", z)
        break
    
    # otherwise plot the points in yellow like normal
    ax.plot(x, y, z, markerfacecolor='y', markeredgecolor='y', marker='o', markersize=5)
    ppts += 1
    print("Iteration ", i, ": x =", x, " y =", y, " z =", z)
    
    # add our plot points to the arrays so we can draw our pathway later
    arrX.append(x)
    arrY.append(y)
    arrZ.append(z)
    i += 1

ax.plot(arrX, arrY, arrZ, color='b')
plt.show()
######################## END PROGRAM & BEGIN DATA RECORDING ######################## 

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