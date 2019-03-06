#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
def minimum(x):
   z = min(x)
   y = x.index(min(x))
   return z , y

while True :
    try:
        array=list(map(int,input("podaj liczby oddzielone spacjami").split()))
        print(array)
        print("minimum to " , minimum(array)[0])
        print("index minimum to " , minimum(array)[1] )
        break
    except ValueError:
        print("musisz podać liczbę")