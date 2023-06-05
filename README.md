# UMIS-Fusion
**Unsupervised learning for multi-focused image stack fusion**\
**Multi-focus image fusion from pairs to stacks**
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
### The fusion result of three professional image stacking software
![The fusion result of three professional image stacking software](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/966d4ad9-612b-4768-a860-f7096b79b101)
### Visualization of layer selection
![Visualization of layer selection](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/6ce3a438-05b4-4aab-8179-5f9cf5afce1f)
### Visualization of partial fusion results on the Lytro dataset
![Visualization of partial fusion results on the Lytro dataset](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/52c8d287-36f1-41c7-8ebb-63dedbd29456)

## Dataset
### Dataset used in the article
[Train dataset(1668 images)](https://pan.baidu.com/s/1QOToaNdLFY9kj_8YlqB_jw?pwd=8888)\
![Part of the dataset used for network training (after pre-processing)](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/f1648315-5ad4-4af8-b2e9-6bc82e4de4fb)

[Test dataset(214 images)](https://pan.baidu.com/s/1agQvFWlkx-tNA_h_nZDKSA?pwd=8888)
![image](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/a45b8085-0704-40f2-b044-062d7dc02d44)

### New Dataset(Better light conditions)
[Dataset(2000 images without split)](https://pan.baidu.com/s/1KdytgF-v43MdzROpdw7Lsw?pwd=8888)
![image](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/64e7233e-d292-45de-bc98-669a7a07c0ff)

### Zhejiang University Logo
[Logo data](https://pan.baidu.com/s/1Y0Dj932wiY3yePyfeEUT-A?pwd=8888)
![image](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/d8d1122f-e369-4407-8d5f-66547eac059c)

### SESF:45 decisionmaps
[Logo data]([https://pan.baidu.com/s/1Y0Dj932wiY3yePyfeEUT-A?pwd=8888](https://pan.baidu.com/s/1arQz0RHxGzxwCK4jjuFI8A?pwd=8888 ))
![decisionmap](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/e8be20ee-f03b-474d-a627-a257988d3d30)
![image](https://github.com/Xinzhe99/UMIS-Fusion/assets/113503163/fcb2b5a6-e543-497f-ba1a-d727ef1cba98)

### EFTL shooting system(Graphical user interface with shooting system and fusion functions)
If you want to make your own new dataset you can click [here](https://github.com/Xinzhe99/EFTL-System)

## Citation
TBD
## Recommendation
TBD
## Acknowledgements
The research was supported by Hainan Provincial Joint Project of Sanya Yazhou Bay Science and Technology City (No. 2021JJLH0079), Project of Sanya Yazhou Bay Science and Technology City (No. SKJC-2022-PTDX-006) and the Research Startup Funding from Hainan Institute of Zhejiang University (NO. 0208-6602-A12204). 
