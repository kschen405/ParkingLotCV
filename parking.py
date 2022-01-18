import cv2
import pickle

img = cv2.imread('carParkImg.png')

w, h = 107, 48
posList = []


def Click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if event == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1+w and y1


while True:
    # cv2.rectangle(img, (50,192),(157,240),(255,0,255),2)

    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+w, pos[0]+h), (255, 0, 255), 2)
    cv2.imshow('image', img)
    cv2.setMouseCallback('image', Click)
    cv2.waitKey(1)
