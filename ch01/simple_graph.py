# coding: utf-8
import numpy as np
import matplotlib.pyplot as plt

import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg' 或 'Agg'，根据你的环境选择合适的后端

# 生成数据
x = np.arange(0, 6, 0.1) # 以0.1为单位，生成0到6的数据
y = np.sin(x)

# 绘制图形
plt.plot(x, y)
plt.show()