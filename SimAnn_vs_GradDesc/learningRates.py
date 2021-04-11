import math


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
