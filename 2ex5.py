#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_float
i = get_float("podaj liczbę ktora wpłynie na kształt wykresu ")
if i == 0 :
    print("wykres jest pusty")
else:


    x_knots = np.linspace(-1*i * np.pi,i*np.pi,201)
    y_knots = np.linspace(-1*i * np.pi,i*np.pi,201)
    X, Y = np.meshgrid(x_knots, y_knots)
    R = np.sqrt(X**2+Y**2)
    Z = i * np.cos(i)*np.sin(i*R)**2*np.exp(- 0.1*i*R)
    ax = Axes3D(plt.figure(figsize=(8,5)))
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap= plt.cm.coolwarm, linewidth=0.4)
    plt.show()