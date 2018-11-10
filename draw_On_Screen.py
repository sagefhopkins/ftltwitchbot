import numpy as np
import cv2 as cv
import time
import re

def box_Image(dict, image):
    image = cv.imread(image)
    for key, value in dict.iteritems():
        regex = re.match(r"^\[(.*?),(.*?)\]$", value)
        name = key
        x = int(regex.group(1))
        y = int(regex.group(2))
        image = cv.rectangle(image, (x-25, y+25), (x+25, y-25), (0, 255, 0), 4 )
        cv. putText(image, name, (x-25, y-35), 0, .8, (0, 255, 0), 2, cv.LINE_AA)
    cv.namedWindow('FTL', cv.WINDOW_NORMAL)
    cv.resizeWindow('FTL', 480, 270)
    cv.imshow('FTL', image)
    cv.waitKey(1)
