
import matplotlib.pyplot as plt
import numpy as np


Fs = 8000
f = 5
sample = 16
np.sin(np.array((0., 30., 45., 60., 90.)) * np.pi / 180.)


x = np.linspace(-np.pi, np.pi, 201)
#y = np.sin(2 * np.pi * f * x / Fs)
plt.plot(x, np.sin(x))
plt.xlabel('voltage(V)')
plt.ylabel('sample(n)')
ply.ylim(-3, 150)
plt.axis('tight')
plt.show()
