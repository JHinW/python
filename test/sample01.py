from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "last_expr"
import numpy as np
from matplotlib import pyplot as plt

def f(x):
    return (x)**2 + x

x = np.array(range(0, 11))
y = np.array([0,10])

plt.xlabel('x')
plt.ylabel('y')
plt.grid()

plt.plot(x, f(x), color='g')
plt.plot(y, f(y), color='m')

plt.show()