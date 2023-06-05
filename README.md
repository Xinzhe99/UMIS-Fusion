# UMIS-Fusion
**Unsupervised learning for multi-focused image stack fusion**
## Abstract
Multi-focus image fusion is an image processing method used to generate full-clear images from two or more images, which solves the problem of optical lenses that cannot obtain full-clear images due to physical limitations. Existing methods focus on fusing complementary multi-focus image pairs by generating binarized decision maps or end-to-end fusion. However, it is more common to fuse multiple images focused at different areas. Fusing image pairs is not enough to conform to realistic demands, moreover, simply repeatedly using these fusion methods for image pairs to fuse image stacks can cause many problems such as fusion errors and color shifts. To overcome these problems, this study proposes a network based on unsupervised deep learning, named UMIS-fusion, to fuse multi-focused image stacks on different application fields with variable sizes and numbers. The neural network is concentrated on the deep spatial frequency gradient features of image stacks, and a customized loss function group is proposed to grab the accurate features from the spatial frequency gradient. Furthermore, compared to the best results of commercial software, the fusion results of the proposed network have comparable speed, but achieve 1.39 better clarity performance on both Spatial Frequency and Average Gradient.

## Requirements
torch 1.12.1\
torchvision 0.13.1\
python 3.8.13\
numba 0.56.4
## Visualization
### Fusion Process
![Schematic diagram of the proposed method](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/60129bba-e83d-41b3-b72f-9e5aa6e563f5)
### Network
![The training block diagram of the network](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/0cba1928-951d-4c90-9677-15313e86e4d0)
### Comparison of the effect of fusion of two pictures
![图片3](https://user-images.githubusercontent.com/113503163/231184544-b0460dbb-bfb6-43eb-abb4-47a0abbe068d.png)

## Dataset
### Dataset used in the article
[Train dataset(1668 images)](https://pan.baidu.com/s/1QOToaNdLFY9kj_8YlqB_jw?pwd=8888)\
[Test dataset(214 images)](https://pan.baidu.com/s/1agQvFWlkx-tNA_h_nZDKSA?pwd=8888)
### New Dataset
[Dataset(2000 images without split)](https://pan.baidu.com/s/1KdytgF-v43MdzROpdw7Lsw?pwd=8888)
### Zhejiang University Logo
[Logo data](https://pan.baidu.com/s/1Y0Dj932wiY3yePyfeEUT-A?pwd=8888)

### EFTL shooting system(Graphical user interface with shooting system and fusion functions)
If you want to make your own new dataset you can click [here](https://github.com/Xinzhe99/EFTL-System)

## Citation
TBD
## Recommendation
TBD
## Acknowledgements
The research was supported by Hainan Provincial Joint Project of Sanya Yazhou Bay Science and Technology City (No. 2021JJLH0079), Project of Sanya Yazhou Bay Science and Technology City (No. SKJC-2022-PTDX-006) and the Research Startup Funding from Hainan Institute of Zhejiang University (NO. 0208-6602-A12204). 
