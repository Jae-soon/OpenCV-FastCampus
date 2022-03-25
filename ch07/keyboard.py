import sys
import numpy as np
import cv2


src = cv2.imread('keyboard.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

_, src_bin = cv2.threshold(src, 0, 255, cv2.THRESH_OTSU)

# retval, labels, stats, controids = (stats = 각 객체 바운딩 박스(픽셀 개수 정보 행렬), centroids = 각 객체의 무게 중심 위치 정보 행렬)
# 바운딩 박스 (x, y, width, height, 개수)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(src_bin)

dst = cv2.cvtColor(src, cv2.COLOR_GRAY2BGR)

for i in range(1, cnt):
    (x, y, w, h, area) = stats[i] # stats의 i번째 행

    if area < 20: # 노이즈 제거
        continue

    cv2.rectangle(dst, (x, y, w, h), (0, 0, 255), 2)

cv2.imshow('src', src)
cv2.imshow('src_bin', src_bin)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
