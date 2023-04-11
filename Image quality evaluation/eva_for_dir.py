# -*- coding: utf-8 -*-
# @Author  : XinZhe Xie
# @University  : ZheJiang University

import numpy as np
import math
import os
import skimage
from PIL import Image
import pandas as pd

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


def entropy_number(image):
    return  skimage.measure.shannon_entropy(image, base=2)


def Mean(image):
    img_array = np.array(image)
    return np.mean(img_array)


def std_number(image):
    img_array = np.array(image)
    return np.std(img_array)

if __name__ == '__main__':

    input_folder = r"path"#todo need set
    output_path_root =os.path.join(os.path.expanduser("~"), 'Desktop')
    output_name='name.xlsx'#todo need set
    output_path=os.path.join(output_path_root,output_name)
    if not os.path.exists(os.path.join(output_path_root,output_name)):
        with open(output_name, 'w') as f:
            pass

    file_names = os.listdir(input_folder)
    df = pd.DataFrame(columns=('Method','AVG', 'SF', 'Mean', 'STD','Entropy'))

    for file_name in file_names:
        if file_name.endswith(".jpg") or file_name.endswith(".png"):
            with Image.open(os.path.join(input_folder, file_name)) as im:
                gray_img = im.convert('L')
                np_img = np.array(gray_img)
                avg=avgGradient(np_img)
                sf=spatialF(np_img)
                mean=Mean(np_img)
                std_num=std_number(np_img)
                entropy_num=entropy_number(np_img)
                new_row = {'Method':file_name.split('.')[0],'AVG': avg, 'SF': sf, 'Mean': mean, 'STD': std_num, 'Entropy': entropy_num}
                df = df.append(new_row, ignore_index=True)
                print(file_name,':','avg=',avg,'sf=',sf,'mean=',mean,'std=',std_num,'entropy=',entropy_num)
    print(df)
    df.to_excel(os.path.join(output_path_root,output_name))

