# %%
import os
import cv2
import numpy as np

# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))


# 创建一个 5*5 的二维矩阵使用1填充 类型为无符号八位 0-255
kernel = np.ones((5, 5), np.uint8)

# 打开图片
img = cv2.imread("123.png")

# %%

设置图片大小 = cv2.resize(img, (500, 200))
图片剪切 = img[0:170, 20:100]


def 显示图片(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


print(img.shape)
# print(设置图片大小.shape)
显示图片("A image", img)
显示图片("B image", 设置图片大小)
显示图片("C image", 图片剪切)


# %%
