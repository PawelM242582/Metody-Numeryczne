#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
import numpy as np
def minimum(x):
   z = min(x)
   y = x.index(min(x))
   index = []
   for index in range(len(array)):
       if array[index] == z:
           print("index minimum to : " , index)
   return z , y

while True :
    try:
        array=list(map(int,input("podaj liczby oddzielone spacjami").split()))
        print(array)
        print("minimum to " , minimum(array)[0])
        x = minimum(array)[0]
        index = []
        for index in range(len(array)):
           if array[index] == x:
               print("index minimum to : " , index)

        break
    except ValueError:
        print("musisz podać liczbę")