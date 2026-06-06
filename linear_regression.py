import matplotlib.pyplot as plt
import numpy as np
import random

a =0.5
b= 100

def derivative_a(n,x,y,a,b):
    t = 0
    for i in range(n):
        t += x[i]*(y[i] - formula(x,i,a,b))
    return (-2/n)*t

def derivative_b(n,x,y,a,b):
    t = 0
    for i in range(n):
        t += (y[i] - formula(x,i,a,b))
    return (-2/n)*t

def formula(x,i,a,b):
    return a*x[i] + b 

def sum_of_points(n,x,y,a,b):
    t = 0
    for i in range(n):
        t += (y[i] - formula(x,i,a,b))**2
    return t

x = [-10, -8, -6, -4, -2, 0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
y = [-35, 3, -22, 15, -8, 25, -2, 34, 10, 45, 18, 58, 30, 72, 40, 85]

n = len(x)
E = (1/n) * sum_of_points(n,x,y,a,b)
print(E)
learning_rate = 0.0001
epochs = 50000

for epoch in range(epochs):
    da = derivative_a(n, x, y, a, b)
    db = derivative_b(n, x, y, a, b)

    a = a - learning_rate * da
    b = b - learning_rate * db

    E = (1/n) * sum_of_points(n, x, y, a, b)

    if epoch % 1000 == 0:
        print(epoch, E, a, b)

y_pred = []

for i in range(n):
    y_pred.append(formula(x, i, a, b))

print("Final E:", E)
print("Final a:", a)
print("Final b:", b)

plt.scatter(x, y, label="Real data")
plt.plot(x, y_pred, label="Learned line")
plt.legend()
plt.show()