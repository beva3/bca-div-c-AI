import matplotlib.pyplot as plt
import numpy as np

class GraphOfFunction:
    def __init__(self, function, x_range):
        self.function = function
        self.x_range = x_range

    def plot(self):
        plt.title('Graph of Function')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        
        x = np.linspace(self.x_range[0], self.x_range[1], 1000)
        y = self.function(x)

        plt.plot(x, y, label=f'f(x) = {self.function.__name__}(x)', color='blue')
        
        
        plt.grid(True)
        plt.grid(True)
        # plt.legend()
        plt.show()
        
def f1(x):
    return x**3 - 2

def f2(x):
    return np.sin(x) + 2 * np.cos(x)

g = GraphOfFunction(f1, (-10, 10))
g.plot()

g2 = GraphOfFunction(f2, (-10, 10))
g2.plot()