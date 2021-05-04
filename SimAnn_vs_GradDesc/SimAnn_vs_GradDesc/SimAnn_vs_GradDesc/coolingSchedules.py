import math

# Cooling schedules Parameters include: Initial S.A. temperature (T0)
# or current S.A. temperature (T) where (t) is the temperature cycle
# and is based on the iteration (i) passed to it


# Lundy & Mees (L&M) cooling schedule
# def lundyMees(T):
    # k = 0.0001
    # return T / (1 + k*T)

# logarithmic cooling
def logarithmic_mult(T, t):
    k = 0.0001    #new run value
    #k = 0.01
    return T / (1 + k*(math.log(t+1)))

# linear cooling
def linear(T0, t):
    k = 0.001    #new run value
    #k = 1
    tNew = max(T0 - (t*k), 0)
    if tNew <= 0.00001:
        return 0.00001
    else:
        return tNew 

# exponential cooling
def exponential(T0, t):
    # k = 0.08    #new run value
    k = 0.8
    # t += 1
    return T0*(k**t)

# quadratic multiplicative cooling 
def quadratic_mult(T, t):
    # k = 0.000001    #new run value
    k = 0.00001
    return T / (1 + k*(t**2))

# stochastic tunneling (STUN) as cooling schedule
# def stun(T, t, fx, fx0):
    # gamma = 5
    # return T*(1 - math.exp((-gamma*t)*(fx - fx0)))
