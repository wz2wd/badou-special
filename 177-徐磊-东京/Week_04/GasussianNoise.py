# -*- coding: utf-8 -*-
"""
@author:rai
高斯噪声
"""

import numpy as np
import cv2
import random


def GaussianNoise(img, mean, sigma, ratio):
    noise_img = img
    pixels_total = img.shape[0] * img.shape[1]
    noise_num = int(np.floor(pixels_total * ratio))
    rand_num = random.sample(range(0, pixels_total), noise_num)  # 产生不重复的随机数
    for v in rand_num:
        x = v // img.shape[1]
        y = v % img.shape[1]
        noise_img[x, y] = int(np.floor(noise_img[x, y] + random.gauss(mean, sigma)))
        if noise_img[x, y] < 0:
            noise_img[x, y] = 0
        elif noise_img[x, y] > 255:
            noise_img[x, y] = 255
    return noise_img


if __name__ == '__main__':
    img = cv2.imread('lenna.png', 0)
    img_gaussian = GaussianNoise(img, 1, 4, 0.9)
    img = cv2.imread('lenna.png')
    img_gray_org = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_merge = np.hstack([img_gray_org, img_gaussian])
    cv2.imshow('Left: Original Image, Right: Gaussian Image', img_merge)
    cv2.imwrite('Gaussian Image.png', img_merge)
    cv2.waitKey(0)
