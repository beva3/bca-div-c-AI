import matplotlib.pyplot as plt
import numpy as np

def f1(x):
    return x**2 -2*x + 1
def f2(x):
    return x - 1

plt.title('Graph of Function')
I = np.linspace(-3, 5, 1000)

plt.axis("equal")
plt.plot(I, f1(I), label='f1(x) = x^2 - 2x + 1', color='blue')
plt.plot(I, f2(I), label='f2(x) = x - 1', color='red')



plt.grid(True)
plt.show()