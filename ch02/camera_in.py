import sys
import cv2

# 카메라 열기
cap = cv2.VideoCapture('video2.mp4') # 0번째 카메라 open(사용)
# cap.open(0)

if not cap.isOpened():
    print('camera or video open failed!')
    sys.exit()

# frame 속성 받아오기(get)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # w값 구하기
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # h값 구하기

# frame 속성 수정(set)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

print(w, h)


while True:
    # 현재 오픈되어있는 카메라에서 한프레임씩 가져옴
    ret, frame = cap.read() # retval = True/False, image

    if not ret:
        break
    
    # frame을 사용하여 처리하는 코드 생성 area
    edge = cv2.Canny(frame, 50, 150) # 윤곽선을 만드는 전처리

    cv2.imshow('frame', frame)
    cv2.imshow('edge', edge)
    if cv2.waitKey(20) == 27: # ESC
        break

cap.release()
cv2.destroyAllWindows()
