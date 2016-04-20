import cv2
from numpy import *
import numpy as np
from matplotlib import pyplot as plt

stereo = cv2.StereoBM(cv2.STEREO_BM_BASIC_PRESET,ndisparities=16, SADWindowSize=15)


def get_net_input(right, left):
    right_gray = cv2.cvtColor(right, cv2.COLOR_BGR2GRAY)
    left_gray = cv2.cvtColor(left, cv2.COLOR_BGR2GRAY)
    disparity = stereo.compute(right_gray,left_gray   )
    disparity = cv2.resize(disparity,(32, 100))

    return disparity


def is_cross_view(right, left):
    return net.activate(get_net_input(right, left)) < 0.5


def split(url):
    cap = cv2.VideoCapture(url)
    ret, image = cap.read()
    image = cv2.resize(image, (200, 200))
    cv2.destroyAllWindows()

    left = image[0:200, 0:100]
    right = image[0:200, 100:200]
    return right, left
