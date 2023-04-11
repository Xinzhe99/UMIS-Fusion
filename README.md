# UMS-Fusion
**Unsupervised learning for multi-focused image stack fusion**
## Abstract
Multi-focus image fusion is an image processing method to generate a fully clarity image from two or more images, which solves the problem that optical lenses cannot obtain a full-frame clarity image due to physical limitations. Existing methods can achieve the fusion of two images with complementary clear and blurred regions by generating a binarized decision map or by direct end-to-end fusion. However, when we need to fuse a multi-focused image stack instead of two complementary image pairs, these fusion methods pose many problems, such as fusion failure, color shifts, etc. In this study, we propose a highly versatile and efficient method for fusing multi-focused image stacks using an unsupervised deep learning approach. Our proposed method includes the steps of acquiring deep features of an image with a neural network, calculating the pixel-level spatial frequency gradients of deep features, fusion decision matrix generation and optimization, and then generating a panoramic deep and clear image. The experimental results show that the proposed fusion method can achieve better fusion results than the professional depth-of-field stack software. 

## Requirements
torch 1.12.1\
torchvision 0.13.1\
python 3.8.13\
numba 0.56.4
## Visualization
### Fusion Process
![2](https://user-images.githubusercontent.com/113503163/231184175-7a70169f-4602-4887-93ed-1de1de060be7.png)
### Post-processing
![1](https://user-images.githubusercontent.com/113503163/231184215-7083abe8-3aaa-42a2-a842-4dcd7e72bf85.png)
### Comparison of the effect of fusion of two pictures
![图片3](https://user-images.githubusercontent.com/113503163/231184544-b0460dbb-bfb6-43eb-abb4-47a0abbe068d.png)

## Dataset used for unsupervised training
### Dataset used in the article
[Train dataset(1668 images)](https://pan.baidu.com/s/1QOToaNdLFY9kj_8YlqB_jw?pwd=8888)\
[Test dataset(214 images)](https://pan.baidu.com/s/1agQvFWlkx-tNA_h_nZDKSA?pwd=8888)
### New Dataset
[Dataset(2000 images without split)](https://pan.baidu.com/s/1KdytgF-v43MdzROpdw7Lsw?pwd=8888)
### EFTL shooting system(Graphical user interface with shooting system and fusion functions)
[For more](https://github.com/Xinzhe99/EFTL-System)

## Citation
TBD
## Recommendation
TBD
