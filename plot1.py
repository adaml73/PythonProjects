
from pylab import figure, show
import numpy as np
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4, 5], [1, 4, 6, 16, 20], 'ro')
plt.axis([0, 6, 0, 20])
plt.ylabel("some numbers")
plt.ylim(1, 30)
plt.show()
