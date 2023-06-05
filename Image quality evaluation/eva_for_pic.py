# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University
import cv2
import numpy as np
import math
from PIL import Image
import os
import skimage

def avgGradient(image):
    width = image.shape[1]
    width = width - 1
    heigt = image.shape[0]
    heigt = heigt - 1
    tmp = 0.0

    for j in range(width):
        for i in range(heigt):
            dx = float(image[i, j + 1]) - float(image[i, j])
            dy = float(image[i + 1, j]) - float(image[i, j])
            ds = math.sqrt((dx * dx + dy * dy) / 2)
            tmp += ds

    imageAG = tmp / (width * heigt)
    return imageAG


def spatialF(image):
    M = image.shape[0]
    N = image.shape[1]

    cf = 0
    rf = 0

    for i in range(1, M - 1):
        for j in range(1, N - 1):
            dx = float(image[i, j - 1]) - float(image[i, j])
            rf += dx ** 2
            dy = float(image[i - 1, j]) - float(image[i, j])
            cf += dy ** 2

    RF = math.sqrt(rf / (M * N))
    CF = math.sqrt(cf / (M * N))
    SF = math.sqrt(RF ** 2 + CF ** 2)

    return SF

# 信息熵
def entropy(image):
    return  skimage.measure.shannon_entropy(image, base=2)


if __name__ == '__main__':

    img=cv2.imread(r'xxx')
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (mean, std) = cv2.meanStdDev(gray_img)

    #输出平均梯度,用于衡量融合图像的清晰程度，可以认为平均梯度越大，图像清晰度越好
    print('avg:',avgGradient(gray_img))
    #输出空间频率，越大越好
    print('sf:', spatialF(gray_img))
    #输出均值,均值衡量是一个反映亮度信息的指标，均值适中，则融合图像质量越好。
    print('mean:',mean[0][0])
    #输出标准差,标准差是度量图像信息丰富程度的一个客观评价指标，该值越大，则图像的灰度级分布就越分散，图像携带的信息量就越多，融合图像质量就越好
    print('std:',std[0][0])
    #输出信息熵，越大越好
    print('entropy:',entropy(gray_img))
