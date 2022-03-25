import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')

if classifier.empty():
    print('XML load failed!')
    sys.exit()
tm = cv2.TickMeter()
tm.start()
faces = classifier.detectMultiScale(src, scaleFactor=1.1, minSize=(100, 100))

tm.stop()
print(tm.getTimeMilli())
for (x, y, w, h) in faces:
    cv2.rectangle(src, (x, y, w, h), (255, 0, 255), 2)

cv2.imshow('src', src)
cv2.waitKey()
cv2.destroyAllWindows()
 