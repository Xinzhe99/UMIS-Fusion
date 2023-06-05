# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University
import cv2
import os

# 读取4张图片路径
img_paths = [
    r'E:\Microscopic_image_stack_fusion\result\val_Dataset_full_loss\SSIM+MSE+SF+Gra.jpg',
    r'E:\Microscopic_image_stack_fusion\result\val_Dataset_noga\SSIM+MSE+SF.jpg',
    r'E:\Microscopic_image_stack_fusion\result\val_Dataset_nosf\SSIM+MSE+Gra.jpg',
    r'E:\Microscopic_image_stack_fusion\result\val_Dataset_nosfnogra\SSIM+MSE.jpg'
]

# 获取保存路径
save_path = '../compare3/'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# 依次读取图片,灰度化并均衡化
for img_path in img_paths:
    # 读取图片
    img = cv2.imread(img_path)
    # 图片宽高
    h, w = img.shape[:2]

    # 中心坐标
    center_x = w // 2
    center_y = h // 2

    # 宽高
    width = 300
    height = 300

    # 取中心区域
    crop_img = img[center_y - height // 2:center_y + height // 2, center_x - width // 2:center_x + width // 2]
    # 转灰度图
    gray = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)

    # # 均衡化
    # equ = cv2.equalizeHist(gray)
    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    # 获取图片名称
    name = os.path.basename(img_path)


    cv2.imwrite(os.path.join(save_path, name), thresh)

print('Done!')