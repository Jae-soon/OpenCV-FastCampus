import sys
import numpy as np
import cv2


mat = np.array([
    [0, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]], np.uint8)

# retval, labels = (객체 개수 + 1, 레이블 맵 행렬(ndarray))
cnt, labels = cv2.connectedComponents(mat)
# retval, labels, stats, controids = (stats = 각 객체 바운딩 박스(픽셀 개수 정보 행렬), centroids = 각 객체의 무게 중심 위치 정보 행렬)
# 바운딩 박스 (x, y, width, height, 개수)
# cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(mat)


print('sep:', mat, sep='\n')
print('cnt:', cnt)
print('labels:', labels, sep='\n')
