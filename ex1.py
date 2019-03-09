#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
def funcion(x):
    return 2*x**2 + 2*x + 2
    
for i in range(0, 6):
    print(funcion(i))