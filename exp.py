# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt

fig = plt.figure()

plt.style.use("ggplot")

#グラフの描画領域の追加
ax = fig.add_subplot(111)

ax.set_title("y=exp(x)", fontsize=16)

ax.set_xlabel("x",fontsize=16)
ax.set_ylabel("y",fontsize=16)

x = np.arange(-2,4,0.1)
y = np.exp(x)

ax.plot(x,y)
plt.show()