import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture('carPark.mp4')
w, h = 107, 45

try:
    with open("CarParkPos", "rb") as f:
        posList = pickle.load(f)
except:
    posList = []


def checkParkingSpace(imgPro):
    left = 0
    for pos in posList:
        x, y = pos
        imgCrop = imgPro[y:y+h, x:x+w]
        #cv2.imshow(str(x+y), imgCrop)
        cnt = cv2.countNonZero(imgCrop)
        cvzone.putTextRect(img, str(cnt), (x, y+h-5),
                           scale=1.5, thickness=1, offset=0)

        if cnt < 900:
            color = (0, 255, 0)
            thickness = 5
            left += 1
        else:
            color = (0, 0, 255)
            thickness = 2
        cv2.rectangle(img, pos, (pos[0]+w, pos[1]+h), color, thickness)
        cvzone.putTextRect(img, f'Available{left}', (
            100, 50), scale=3, thickness=5, offset=20, colorR=(0, 200, 0))


while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    success, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    imgThreshold = cv2.adaptiveThreshold(
        imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgThreshold, 5)
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)
    checkParkingSpace(imgDilate)
    # for pos in posList:
    #     cv2.rectangle(img, pos, (pos[0]+w, pos[1]+h), (255.0, 255), 2)
    cv2.imshow("Image", img)
    cv2.waitKey(1)
