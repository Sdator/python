
import os
import cv2
import numpy as np


# 修改当前工作目录为脚本运行目录
os.chdir(os.path.dirname(__file__))


# 创建一个 5*5 的二维矩阵使用1填充 类型为无符号八位 0-255
kernel = np.ones((5, 5), np.uint8)

# 打开图片
img = cv2.imread("123.png")
# 在opencv中图像格式为BGR
# 颜色转换
# BGR转换为灰度图片
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0)  # 模糊 元组必须为奇数
imgBlur2 = cv2.GaussianBlur(img, (1, 19), 0)  # 模糊 元组必须为奇数

imgCanny = cv2.Canny(img, 150, 200)  # 边缘检测
imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)  # 边缘增大
imgEroded = cv2.erode(imgDialation, kernel, iterations=1)  # 矩阵黑点代替


cv2.imshow("Gray image", imgGray)
cv2.imshow("Blur image", imgBlur)
cv2.imshow("Blur image", imgBlur2)
cv2.imshow("Canny image", imgCanny)
cv2.imshow("Dialation image", imgDialation)
cv2.imshow("Eroded image", imgEroded)


cv2.waitKey(0)
