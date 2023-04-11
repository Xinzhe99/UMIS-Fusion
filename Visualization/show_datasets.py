# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University

import os
import matplotlib.pyplot as plt
import cv2
folder_path = r"C:\Users\dell\Desktop\imagestacks\imagestacks\Partial dataset for display (after grayscale equalization)"#todo Need Set
file_names = os.listdir(folder_path)
# #用来把自己的放在最后显示
# file_names.remove('Ours.jpg')
# file_names.append('Ours.jpg')

fig, axs = plt.subplots(2, 4, figsize=(20, 5))
fig.subplots_adjust(wspace=0.1,hspace=0.3)
for i, ax in enumerate(axs.flat):
    if i < len(file_names):
        #todo 写需求
        img = plt.imread(os.path.join(folder_path, file_names[i]))#rgb
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#gray
        equ = cv2.equalizeHist(gray)
        cv2.imwrite('{}.jpg'.format(i),equ)
        ax.imshow(cv2.cvtColor(equ, cv2.COLOR_GRAY2RGB))#rgb
        # ax.set_title(file_names[i].split('.')[0])
    ax.axis('off')
plt.show()