import matplotlib.pyplot as plt

# to handle number and create ranges
import numpy as np 

# 1.define function
def f(x):
    return x**2

#  2.create x values from -10 to 10 with 100 pts
x = np.linspace(-10, 10, 100)

#  3.create y values using the function f(x)
y = f(x)

#  4.create the plot
plt.plot(x, y, label='f(x) = x^2')
plt.title('Graph of f(x) = x^2')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()


