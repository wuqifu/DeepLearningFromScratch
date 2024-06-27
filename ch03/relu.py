# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg' 或 'Agg'，根据你的环境选择合适的后端

def relu(x):
    return np.maximum(0, x)

x = np.arange(-5.0, 5.0, 0.1)
y = relu(x)
plt.plot(x, y)
plt.ylim(-1.0, 5.5)
plt.show()
