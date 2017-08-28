# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 10:03:55 2017

@author: Anh
"""

import cv2
img = cv2.imread("lena.png")
crop_img = img[35:565, 1:421] # Crop from x, y, w, h -> 100, 200, 300, 400
# NOTE: its img[y: y + h, x: x + w] and *not* img[x: x + w, y: y + h]
cv2.imshow("cropped", crop_img)

resize_img = cv2.resize(crop_img, (80, 80))
cv2.imshow("resized", resize_img)
cv2.imwrite("resized.png", resize_img)

gray_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("grayed", gray_img)
cv2.imwrite("grayed.png", gray_img)

cv2.waitKey(0)