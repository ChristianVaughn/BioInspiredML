import math

# Cooling schedules Parameters include: Initial S.A. temperature (T0)
# or current S.A. temperature (T) where (t) is the temperature cycle
# and is based on the iteration (i) passed to it

# logarithmic cooling
def logarithmic_mult(T, t):
    k = 5
    return T / (1 + k*(math.log(t+1)))

# linear cooling
def linear(T0, t):
    k = 10
    tNew = max(T0 - (t*k), 0)
    if tNew <= 0.00001:
        return 0.00001
    else:
        return tNew 

# exponential cooling
def exponential(T0, t):
    k = 0.8
    return T0*(k**t)

# quadratic multiplicative cooling 
def quadratic_mult(T, t):
    k = 0.2
    return T / (1 + k*(t**2))

# stochastic tunneling (STUN) as cooling schedule
def stun(T, t, fx, fx0):
    gamma = 0.5
    return 1 - math.exp((-gamma)*(fx - fx0))
