# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University
from PIL import Image, ImageOps
import os

def resize_and_convert_to_gray(image_path, new_folder_path):
    # 打开图像文件
    image = Image.open(image_path)

    # 修改图像尺寸
    new_size = (820, 600)
    image = image.resize(new_size)

    # 转换为灰度图像
    image = image.convert('L')

    # 灰度均衡化
    image = ImageOps.equalize(image)

    # 保存到新文件夹
    new_image_path = os.path.join(new_folder_path, os.path.basename(image_path))
    image.save(new_image_path)

# 遍历文件夹中的所有图像文件
folder_path = r'C:\Users\dell\Desktop\show_dataset\g5'
new_folder_path = r'C:\Users\dell\Desktop\show_dataset\n5'
for filename in os.listdir(folder_path):
    if filename.endswith('.Bmp') or filename.endswith('.png'):
        image_path = os.path.join(folder_path, filename)
        resize_and_convert_to_gray(image_path, new_folder_path)