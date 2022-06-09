import skimage.io as io
import math
import numpy as np
import cv2


def LoG(i, j):
    LoGvalue = np.array([[0, 0, -1, 0, 0],
                         [0, -1, -2, -1, 0],
                         [-1, -2, 16, -2, -1],
                         [0, -1, -2, -1, 0],
                         [0, 0, -1, 0, 0]])
    if i < 0 or i > 4 or j < 0 or j > 4:
        print("error: out of range in LoG()")
        exit()
    return LoGvalue[i, j]


def LateralInhibitionByLoG(img):
    LaplaceValue = np.array([[0, 0, -1, 0, 0],
                             [0, -1, -2, -1, 0],
                             [-1, -2, 16, -2, -1],
                             [0, -1, -2, -1, 0],
                             [0, 0, -1, 0, 0]])
    height = img.shape[0]
    width = img.shape[1]
    img = cv2.GaussianBlur(img, (5, 5), 0)
    result_img = np.zers((height, width), np.uint8)
    # if img.shape[0] < 5 or img.shape[1] < 5:  # 若图片宽、高小于模板则报错
    #     print("error: unsatisfied image size in LateralInhibitionByLoG()")
    #     exit()

    padding = np.zeros((height + 4, width + 4), np.uint8)
    padding[2:-2, 2:-2] = img1
    for i in range(0, height):
        for j in range(0, width):
            window = padding[i:i + 5, j:j + 5]
            result_img[i, j] = np.abs(np.sum(LaplaceValue * window))
    # img_after = img  # 定义为一样的目的是保留边缘像素值
    # for m in range(2, img.shape[0] - 2):
    #     for n in range(2, img.shape[1] - 2):  # 对img中的点(m,n)
    #         img_after[m, n] = 0  # 首先置零
    #         for i in range(m - 2, m + 3):
    #             for j in range(m - 2, m + 3):  # 对一个点套用模板，(i,j)是模板位置
    #                 img_after[m, n] += LoG(i - (m - 2), j - (m - 2)) * img[i, j]
    #                 if img_after[m, n] > 1:
    #                     img_after[m, n] = 1

    return result_img


img = cv2.imread('Lenna.jpg', as_gray=True)
# io.imshow(img)#
# io.show()
img1 = LateralInhibitionByLoG(img)
io.imshow(img1)
io.show()
