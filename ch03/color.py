import sys
import numpy as np
import cv2


# 컬러 영상 불러오기
src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

# hsv변환
src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
src_split = cv2.split(src_hsv)
planes = cv2.split(src)

cv2.imshow('src', src)
cv2.imshow('planes[0]', planes[0])
cv2.imshow('planes[1]', planes[1])
cv2.imshow('planes[2]', planes[2])
cv2.imshow('src_split[0]', src_split[0])
cv2.imshow('src_split[1]', src_split[1])
cv2.imshow('src_split[2]', src_split[2])
cv2.waitKey()

cv2.destroyAllWindows()
