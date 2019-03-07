#2 ask the user for a number and print its factorial (1p)
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   pass
def factorial(x):
    f=1
    for i in range(1,x+1):
        f = f * i
    return f
while True :
    try:
        z = int(input("Podaj liczbe "))
        if z <  0:
           raise ValueTooSmallError
        print("factorial" , z , "=", factorial(z))
        break
    except ValueError:
        print("musisz podać poprawną liczbę")
    except ValueTooSmallError :
        print( "podaj liczbę nieujemną")

