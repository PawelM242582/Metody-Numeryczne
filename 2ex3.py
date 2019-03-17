#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
from cs50 import get_int , get_float

x = get_float("x: " )
y = get_float("y: ")
if y == 0:
    print("nie wolno dzielić przez 0")
else:
    print('X is divisible by Y') if (x % y == 0) else print('X is not divisible by Y')

