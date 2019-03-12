#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
from cs50 import get_float

x = get_float("x: ")
y = get_float("y: ")
a = x/y
print("x/y = " , "%.2f" %a)
