from numpy import linspace
from matplotlib.pyplot import *
#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
class Error(Exception):
   """Base class for other exceptions"""
   pass
class ValueTooSmallError(Error):
   pass
while True:
    try:
        n = int(input("Podaj długość wykresu: "))
        if n  <  0:
           raise ValueTooSmallError
        x = linspace(0, n)
        y = x **2
        plot(x, y)
        show()
        break
    except ValueError:
        print("musisz podać liczbę")
    except ValueTooSmallError :
        print( "podaj liczbę nieujemną")
