#Images color display with matplotlib script for the Eurobot2018 **Inial Commit by DH1A**

import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

pictures = os.getcwd()

def display(Type):
    if Type == 1:

        ImgRGB = cv2.imread('pictures/calibration/RGB/image1_rgb.jpg')
        ImgHSV = cv2.imread('pictures/calibration/HSV/image1_hsv.jpg')


        plt.subplot(211)
        plt.imshow(cv2.cvtColor(ImgRGB, cv2.COLOR_BGR2RGB))

        plt.subplot(212)
        plt.imshow(ImgHSV)

        plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
        plt.show()

        cv2.waitKey(0)
    elif Type == 2:

        ImgRGB = cv2.imread('pictures/detection/RGB/image1_rgb.jpg')
        ImgHSV = cv2.imread('pictures/detection/HSV/image1_hsv.jpg')

        plt.subplot(211)
        plt.imshow(cv2.cvtColor(ImgRGB, cv2.COLOR_BGR2RGB))

        plt.subplot(212)
        plt.imshow(ImgHSV)

        plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
        plt.show()

        cv2.waitKey(0)

    elif Type == 3:

        ImgRGBD = cv2.imread('pictures/detection/RGB/image1_rgb.jpg')
        ImgHSVD = cv2.imread('pictures/detection/HSV/image1_hsv.jpg')

        plt.subplot(211)
        plt.imshow(cv2.cvtColor(ImgRGBD, cv2.COLOR_BGR2RGB))

        plt.subplot(212)
        plt.imshow(ImgHSVD)

        ImgRGBC = cv2.imread('pictures/calibration/RGB/image1_rgb.jpg')
        ImgHSVC = cv2.imread('pictures/calibration/HSV/image1_hsv.jpg')

        plt.subplot(311)
        plt.imshow(cv2.cvtColor(ImgRGBC, cv2.COLOR_BGR2RGB))

        plt.subplot(312)
        plt.imshow(ImgHSVC)

        plt.subplots_adjust(bottom=0.1, right=0.8, top=0.9)
        plt.show()

        cv2.waitKey(0)
    else:
        print('non valid parameter enter 1 for detection or 2 for calibration or 3 for both')

if __name__ == "__main__":
    display(1)