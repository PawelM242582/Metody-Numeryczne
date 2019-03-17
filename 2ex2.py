#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
from random import *
x = 9
y = 6
while x % 2 != 0 or y % 2 != 0 or x % y != 0  : 
    x = randint(1,100)
    
    y = randint(1,100)         
    
    
          
     
print("x= %s y= %s " %(x, y))