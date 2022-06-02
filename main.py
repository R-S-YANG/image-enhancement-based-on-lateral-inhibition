# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
#
# from skimage import io, data
# img = data.chelsea()
# io.imshow(img)
# print(type(img))  #显示类型
# print(img.shape)  #显示尺寸
# print(img.shape[0])  #图片高度
# print(img.shape[1])  #图片宽度
# print(img.shape[2])  #图片通道数
# print(img.size)   #显示总像素个数
# print(img.max())  #最大像素值
# print(img.min())  #最小像素值
# print(img.mean()) #像素平均值
# print(img[0][0])#图像的像素值

# import cv2
import numpy as np
import skimage.io as io
import math


def Inhibition(img, m, n, l):  # (m,n)是侧抑制中心坐标，l是侧抑制半径
    inhibition = 0
    beta = 100
    sigma = 100
    for i in range(m - l, m + l):
        for j in range(n - l, n + l):
            ### 求侧抑制参数k
            dist_pow = (m-i) ** 2 + (n-j) ** 2
            k = 1 / (beta * math.sqrt(2 * math.pi)*sigma) * math.exp(-dist_pow / 2 * pow(sigma, 2))
            inhibition = inhibition+ k * img[i, j]
    return inhibition


def Lateral_Inhibition(img, l):  # l是侧抑制半径
    for m in range(l, img.shape[0]-l):
        for n in range(l, img.shape[1]-l):
            img[m][n] = img[m][n] - Inhibition(img, m, n, l)
    print("done")
    return img


img = io.imread('登记照2019.jpg', as_gray=True)
# io.imshow(img)#
# io.show()
# img=Lateral_Inhibition(img,5)
io.imshow(img)
io.show()
print('abc')


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
