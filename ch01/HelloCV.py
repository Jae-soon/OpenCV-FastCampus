import sys
import cv2

print("Hello, OpenCV", cv2.__version__)

img = cv2.imread('ch01/cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print("Image load failed!")
    sys.exit()

cv2.imwrite('ch01/cat_gray.png', img)

cv2.namedWindow('image')
cv2.imshow('image', img)

while True:
    # esc 키만 누를 경우 종료(ord를 사용하여 작성 가능)
    if cv2.waitKey() == 27:
        break
# waitKey 는 ASCII 코드 반환(아무것도 누르지 않으면 '-1' 출력)
# key = cv2.waitKey(2000)
# print(key)

cv2.destroyWindow('image')