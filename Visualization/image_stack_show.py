from PIL import Image
import os
import numpy as np
import matplotlib.pyplot as plt

# 读取文件夹中的所有图像
path = r"C:\Users\dell\Desktop\imagestacks\imagestacks\The data set used for the experiments(original size)"
files = os.listdir(path)
files.sort()

# 将所有图像转换为灰度图像
images = []
for file in files:
    with Image.open(os.path.join(path, file)) as img:
        img_gray = img.convert('L')
        images.append(np.array(img_gray))

# 将所有图像沿着z轴堆叠起来
stacked_images = np.stack(images, axis=-1)
print(stacked_images.shape)
print(stacked_images)

x, y, z = np.indices(stacked_images.shape)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
de=stacked_images.flatten()
ax.scatter(x, y, z, c=stacked_images.flatten(), alpha=0.1, cmap='gray')
ax.zaxis.set_major_locator(plt.NullLocator())

ax.set_zorder(0)
ax.set_zticks([])
ax.set_xticks([])
ax.set_yticks([])
# plt.savefig('demo.svg', format='svg')
plt.show()
