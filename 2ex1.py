#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
from math import pi
from cs50 import get_float

def perimeter(x):
    return 2* pi *x

def field(x):
    return pi * x * x

x = get_float("podaj x") 
y = get_float("podaj y")

print("Perimeter for %s is %s " %(x, perimeter(x)))
print("field for %s is %s " %(x, perimeter(x)))
print("Perimeter for %s is %s " %(y, perimeter(y)))
print("field for %s is %s " %(y, perimeter(y)))

