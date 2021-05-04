import math

### RASTRIGIN FUNCTION ###
def rastrigin(x, y, A):   # limits -5.12 <= x,y <= 5.12
    return 2*A + x**2 - A*math.cos(2*math.pi*x) + y**2 - A*math.cos(2*math.pi*y)

#gradient X
def rastrigin_dx(x, A):
    return 2*x + 2*math.pi*A*math.sin(2*math.pi*x)
#gradient Y
def rastrigin_dy(y, A):
    return 2*y + 2*math.pi*A*math.sin(2*math.pi*y)

#gradient double prime X (2nd derivative)
def rastrigin_ddx(x, A):
    return 2 + 4*(math.pi**2)*A*math.cos(2*math.pi*x)
#gradient double prime Y (2nd derivative)
def rastrigin_ddy(y, A):
    return 2 + 4*(math.pi**2)*A*math.cos(2*math.pi*y)
