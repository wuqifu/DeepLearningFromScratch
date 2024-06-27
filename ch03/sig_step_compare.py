# coding: utf-8
import numpy as np
import matplotlib.pylab as plt

import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg' 或 'Agg'，根据你的环境选择合适的后端

def sigmoid(x):
    return 1 / (1 + np.exp(-x))    


def step_function(x):
    return np.array(x > 0, dtype=int)

x = np.arange(-5.0, 5.0, 0.1)
y1 = sigmoid(x)
y2 = step_function(x)

plt.plot(x, y1)
plt.plot(x, y2, 'k--')
plt.ylim(-0.1, 1.1) #指定图中绘制的y轴的范围
plt.show()
