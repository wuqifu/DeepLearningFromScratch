# coding: utf-8
import matplotlib.pyplot as plt
from matplotlib.image import imread

import matplotlib
matplotlib.use('TkAgg')  # 或 'Qt5Agg' 或 'Agg'，根据你的环境选择合适的后端

img = imread('../dataset/lena.png') #读入图像
plt.imshow(img)

plt.show()