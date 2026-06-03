import matplotlib.pyplot as plt
import numpy as np
import random

a =1.8
b= 32

def formula(x,i,a,b):
    return a*x[i] + b 

def sum_of_points(n,x,y,a,b):
    t = 0
    for i in range(n):
        t += (y[i] - formula(x,i,a,b))**2
    return t

x = [-40, -30, -20, -10, -5, 0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
y = [-40, -22, -4, 14, 23, 32, 41, 50, 59, 68, 77, 86, 95, 104, 113, 122, 131, 140, 149, 158, 167, 176, 185, 194, 203, 212]

n = len(x)
E = (1/n) * sum_of_points(n,x,y,a,b)
print(E)


plt.scatter(x, y)
plt.show()