# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University
from PIL import Image
import os

# 输入文件夹路径和输出文件夹路径
input_folder = r"C:\Users\dell\Desktop\imagestacks\imagestacks\software"
output_folder = r"C:\Users\dell\Desktop\imagestacks\imagestacks\software123"



if not os.path.exists(output_folder):
    os.makedirs(output_folder)
# 获取输入文件夹中所有图片的文件名
file_names = os.listdir(input_folder)

# 遍历所有图片并resize它们
for file_name in file_names:
    # 仅处理.jpg和.png格式的图片
    if file_name.endswith(".jpg") or file_name.endswith(".png"):
        # 打开图片并resize它
        with Image.open(os.path.join(input_folder, file_name)) as im:
            im_resized = im.resize((717, 600)).convert('RGB')
            # 保存resize后的图片到输出文件夹中
            output_file_path = os.path.join(output_folder, file_name)
            im_resized.save(output_file_path)