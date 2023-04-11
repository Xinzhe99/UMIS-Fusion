# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University
import os
import matplotlib.pyplot as plt
import cv2
folder_path = r"C:\Users\dell\Desktop\imagestacks\imagestacks\software_resize\img"#todo Need Set
file_names = os.listdir(folder_path)
#用来把自己的放在最后显示
file_names.remove('Proposed.jpg')
file_names.append('Proposed.jpg')

fig, axs = plt.subplots(3, 6,dpi=200)
fig.subplots_adjust(wspace=0.05)

plt.rcParams['font.sans-serif'] = ['Times New Roman']
plt.rcParams['font.weight'] = 'normal'
note=''
for i, ax in enumerate(axs.flat):
    if i < len(file_names):
        img = plt.imread(os.path.join(folder_path, file_names[i]))#rgb
        ax.imshow(img)
        # ax.set_title(file_names[i].split('.')[0])
        ax.set_title('({})'.format(chr(ord('a')+i)),y=-0.35)
        note=note+'({}).{}. '.format(chr(ord('a')+i),file_names[i].split('.')[0])
    ax.axis('off')
print(note)
plt.show()