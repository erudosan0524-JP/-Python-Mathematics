#encoding=utf-8
import numpy as np
from matplotlib import pyplot as plt

#ベクトルの生成
#ベクトルの始点
startPoint = [0,1]

#ベクトルの成分
Component = [2,1]

#ベクトルの描画
plt.quiver(startPoint[0],startPoint[1],Component[0],Component[1],angles='xy',scale_units='xy',scale=1)

plt.xlim([-1,2])
plt.ylim([-1,2])
plt.grid()
plt.draw()
plt.show()
