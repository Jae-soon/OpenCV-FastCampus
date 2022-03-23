import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

dst = cv2.add(src, 100) # 255를 초과하는 경우 255로 고정
# dst = cv2.add(src, (100, 100, 100, 0)) # Color 사용 시
# dst = src + 100 # 255를 초과하는 경우 발생(0에 가까운 값으로 변경)
# dst = np.clip(src + 100., 0, 255).astype(np.uint8) # 실수 단위로 계산 필요

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
