import cv2
import pickle
import cvzone

cap = cv2.VideoCapture('carPark.mp4')
w, h = 103, 43
with open('polygons', 'rb') as f:
    posList = pickle.load(f)


def empty(a):
    pass
