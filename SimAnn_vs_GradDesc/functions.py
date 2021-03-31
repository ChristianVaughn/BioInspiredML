import math

### RASTRIGIN FUNCTION ###
def rastrigin(x, y, A):   # limits -5.12 <= x,y <= 5.12
    return 2*A + x**2 - A*math.cos(2*math.pi*x) + y**2 - A*math.cos(2*math.pi*y)
#grad X
def rastrigin_dx(x, y, A):
    return 2*x + 2*math.pi*A*math.sin(2*math.pi*x)
#grad Y
def rastrigin_dy(x, y, A):
    return 2*y + 2*math.pi*A*math.sin(2*math.pi*y)

### ROSENBROCK FUNCTION ###
def rosenbrock(x, y):
    return 100*(y - x**2)**2 + (1 - x)**2
#grad X
def rosenbrock_dx(x, y):
    return 400*x**3 + (2 - 400*y)*x - 2
#grad Y
def rosenbrock_dy(x, y):
    return 200*(y - x**2)