import random

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator # 导入 MaxNLocator 函数
from fusion import decisionmap_process
# create a 1d array of 0 to 99 with 400 elements

np.random.seed(2)
bc=16#need set
a = np.linspace(0, 100, bc*bc)

# shuffle the array randomly
np.random.shuffle(a)

# reshape the array into a 20*20 matrix
a = a.reshape(bc, bc)

# sort the matrix along each row
a = np.sort(a, axis=1)

# todo NEED SET
a=decisionmap_process(a,k_size=3,use_fuzzy_op=True)#post-process matrix


plt.imshow(a)
plt.imshow(a,origin='upper') # 显示矩阵的图像
plt.xlabel('Width')
plt.ylabel('Height')
# plt.title("Initial Decision Matrix", color="black")
plt.title("Fuzzy Decision Matrix", color="black")
plt.xticks(np.arange(0, bc, 2))
plt.yticks(np.arange(0, bc, 2))
#colorbar上下限手动设定
plt.clim(0, 100)
cbar=plt.colorbar(label='Imgage Layer Index') # 显示颜色条
cbar.ax.set_title('Layer')
cbar.locator = MaxNLocator(nbins=5) # 设置颜色条的刻度位置为 5 个整数
plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

for i in range(bc):
    for j in range(bc):
        plt.text(j, i, int(a[i][j]), ha='center', va='center', color='w')
plt.show()