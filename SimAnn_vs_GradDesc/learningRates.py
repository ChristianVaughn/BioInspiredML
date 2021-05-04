import math
from functions import rastrigin_ddx, rastrigin_ddy

# The learning rate (LR) is a meta-heuristic like cooling schedule in S.A.
# LR is roughly the step size of movement away from gradient (for minimization) and with (for maximization)
def lrStatic(k):
    return k

# scaling learning rate takes the initial k and reduces it based on the given rate as the algorithmic iterations are increasing
# k = learning rate
# reduction = factor to reduce LR by
# rate = number iterations at which learning rate is the same
def lrScaling(k, t, reduction, rate):
    step = int(t/rate)
    return k - k*step*reduction

# cosine learning rate returns the value of the cosine (decreasing) learning rate  on
# the given iteration based on the given period (maximum number of iterations).
# t = iteration number of learning rate
# T = period
def lrCosine(k, t, T):
    return k*(1 + math.cos(math.pi*t / T)) / 2

# Cosine cycles on a given period
# t = iteration number of learning rate
# T = period
# M = cycle
def lrPeriodic(k, t, T, M):
    return k*(1 + math.cos(math.pi*((t - 1) % (int(T/M) + 1)) / (int(T/M) + 1))) / 2


# MOMENTUM -> first attempt: [(stepSize*gradient) + (momentum*change)]... return k + P*delta?? 
# in Physics momentum(P) = mass(m)*velocity(V) or formally P = mV
# if velocity is a rate of change and we need the rate by which that changes in order
# to achieve a trajectory for P then we need both first and second derivatives of the
# objective function and some kind of weighted average between the two to optimize directions
# carrying more "weight" or "momentum"
# x = current x 
# y = current y 
# P = momentum [0..1] ~0.8-0.9 seems optimal @1 it never stops

### as funciton calls: takes too much time and freezing my computer
def lrMomentumX(x, A, P):
    # second derivative for determining momentum as exponentially weighted averages
    ddx = rastrigin_ddx(x, A)
    return (1 - P)*ddx

def lrMomentumY(y, A, P):
    # second derivative for determining momentum as exponentially weighted averages
    ddy = rastrigin_ddy(y, A)
    return (1 - P)*ddy