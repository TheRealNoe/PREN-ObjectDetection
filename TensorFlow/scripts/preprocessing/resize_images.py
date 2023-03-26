import os
from pprint import pprint
import cv2 as cv

path = "../../../images/original/"
dirs = os.listdir(path)

def rotate():
    print("Start rotate")
    for item in dirs:
        if os.path.isfile(path + item):
            img = cv.imread(path + item)
            shape = img.shape

            if(shape[0] < shape[1]):
                image = cv.rotate(img, cv.cv2.ROTATE_90_CLOCKWISE)

                cv.imwrite(path + item, image)
                print(path + item)

def resize():
    print("Start resize")
    for item in dirs:
        if os.path.isfile(path + item):
            img = cv.imread(path + item)
            shape = img.shape
            
            targetHeight = 640
            targetWidth = int(640 / shape[0] * shape[1])

            img = cv.resize(img, (targetWidth, targetHeight), interpolation = cv.INTER_AREA)

            left = int((640 - targetWidth) / 2)
            right = 640 - targetWidth - left

            image = cv.copyMakeBorder(img, 0, 0, left, right, cv.BORDER_CONSTANT)
            
            cv.imwrite(path + "../resized/" + item, image)
            print(path + "../resized/" + item)

rotate()
resize()