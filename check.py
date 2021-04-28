from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

img = np.array(Image.open('/Users/JIE/GitHub/Image_Segmentation/dataset/train_GT/0.png'))  # 打开图像并转化为数字矩阵
plt.figure("cell")
plt.imshow(img)
plt.axis('off')
plt.show()
print(img.shape)
print(img.dtype)
print(img.size)
print(type(img))
print(img.shape[2])
