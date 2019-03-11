#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
from cs50 import get_int

x = get_int("x: " )
y = get_int("y: ")
divisible = x % y ==0 ; divisibleLog = 'X is divisible by Y' if divisible else 'X is not divisible by Y'
print(divisibleLog)