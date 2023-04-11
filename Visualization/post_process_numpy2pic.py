import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator # 导入 MaxNLocator 函数
from fusion import decisionmap_process

c1 = np.mat(
"0	0	0	0	1	1	1	1	2	2	2	3	4	4	5	5;"
"0	0	0	1	1	1	2	2	2	2	2	3	4	4	5	5;"
"0	0	0	1	4	2	2	2	2	3	3	3	4	3	5	5;"
"0	0	0	1	2	2	2	2	3	3	3	3	4	4	3	3;"
"1	0	0	1	2	2	2	2	3	3	3	4	4	4	5	5;"
"0	0	1	1	2	2	2	2	3	3	3	4	4	4	5	0;"
"0	0	1	1	2	2	2	2	3	3	3	4	4	4	5	5;"
"1	0	1	1	2	2	2	2	3	0	4	4	4	4	5	5;"
"0	0	1	1	2	2	4	2	3	3	4	4	1	4	5	4;"
"0	1	1	1	2	2	2	2	2	3	3	3	4	4	5	4;"
"0	1	1	1	0	2	2	2	2	3	3	3	4	4	5	5;"
"0	1	1	1	2	2	2	2	2	3	3	3	4	4	5	5;"
"0	1	0	1	2	2	2	2	4	3	3	4	4	4	5	5;"
"0	1	1	1	1	1	1	1	2	2	3	4	4	5	5	5;"
"0	1	1	1	1	1	1	1	2	2	3	5	4	5	5	5;"
"0	1	1	1	1	1	1	1	1	1	5	5	4	5	5	5")
c1=c1.A #original matrix
c2=decisionmap_process(c1,k_size=5)#post-process matrix

c=c2#need set
plt.figure(dpi=500)
plt.imshow(c,origin='upper') # 显示矩阵的图像
plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)
if np.array_equal(c,c2):
    plt.title("Processed Decision Matrix", color="black")
else:
    plt.title("Initial Decision Matrix", color="black")
plt.xlabel('Width')
plt.ylabel('Height')
cbar=plt.colorbar(label='Imgage Layer Index') # 显示颜色条
cbar.locator = MaxNLocator(nbins=5) # 设置颜色条的刻度位置为 5 个整数
cbar.ax.set_title('Layer')
cbar.ax.title.set_fontsize(10)
cbar.update_ticks() # 更新刻度显示
for i in range(c.shape[0]): # 遍历矩阵的行数
    for j in range(c.shape[1]): # 遍历矩阵的列数
        plt.text(j, i, c[i][j],ha="center", va="center", color="w", fontsize=10) # 在对应位置显示元素的值
plt.show() # 显示图像
