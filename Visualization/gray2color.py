import cv2
import matplotlib.pyplot as plt

from matplotlib.ticker import MaxNLocator # 导入 MaxNLocator 函数

import numpy as np
# 读取灰度图
# mark_np1=np.load('decision_map_np2022_12_20_22_14_22.npy').astype(np.uint8)
# mark_np2=np.load('decision_map_np2022_12_20_22_14_30optimized.npy').astype(np.uint8)
mark_np1=np.load(r'E:\Microscopic_image_stack_fusion\result\for_paper\无任何后处理.npy').resize((717,600)).astype(np.uint8)
mark_np2=np.load(r'E:\Microscopic_image_stack_fusion\result\for_paper\有后处理无fuzzy.npy').astype(np.uint8)
mark_np3=np.load(r'E:\Microscopic_image_stack_fusion\result\for_paper\fuzzy处理后.npy').astype(np.uint8)
mark_np4=np.load(r'E:\Microscopic_image_stack_fusion\result\for_paper_origin_1_3_0_0\1_3_0_0.npy').astype(np.uint8)
mark=mark_np1#todo Need set

plt.figure(dpi=600)
plt.imshow(mark,origin='upper') # 显示矩阵的图像
plt.tick_params(top=True, labeltop=True, bottom=False, labelbottom=False)

plt.xlabel('Width')
plt.ylabel('Height')

# plt.title("Initial Decision Matrix", color="black")
# plt.title("Processed Decision Matrix", color="black")
plt.title("Fuzzy Decision Matrix", color="black")
cbar=plt.colorbar(label='Imgage Layer Index',shrink=0.585) # 显示颜色条
cbar.locator = MaxNLocator(nbins=4) # 设置颜色条的刻度位置为 x 个整数
cbar.ax.set_title('Layer')
cbar.ax.title.set_fontsize(10)
cbar.update_ticks() # 更新刻度显示

# for i in range(mark_np1.shape[0]): # 遍历矩阵的行数
#     for j in range(mark_np1.shape[1]): # 遍历矩阵的列数
#         plt.text(j, i, mark_np1[i][j],ha="center", va="center", color="w", fontsize=10) # 在对应位置显示元素的值


plt.show() # 显示图像
#
# im1 = Image.fromarray(mark_np1)
# im1 = im1.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
# im2 = Image.fromarray(mark_np2)
# im2 = im2.convert('L')  # 这样才能转为灰度图，如果是彩色图则改L为‘RGB’
#
# im11=np.array(im1)
# im22=np.array(im2)
#
# im_color1 = cv2.applyColorMap(cv2.convertScaleAbs(im11, alpha=1), cv2.COLORMAP_HSV)
#
# im_color2 = cv2.applyColorMap(cv2.convertScaleAbs(im22, alpha=1), cv2.COLORMAP_HSV)
#
# cv2.imshow('t1',im_color1)
# cv2.imshow('t2',im_color2)
#
# cv2.waitKey()
#
