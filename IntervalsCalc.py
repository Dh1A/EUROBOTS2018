import cv2
import numpy as np
import os
from matplotlib import pyplot as plt

def CalibRead():
        # Importing Sample Colors and converting to HSV
        Green = cv2.imread('pictures/calibration/RGB/color_sampleGreen_rgb.jpg')
        #Greenh = cv2.cvtColor(Green, cv2.COLOR_BGR2HSV)

        Blue = cv2.imread('pictures/calibration/RGB/color_sampleBlue_rgb.jpg')
        #Blueh = cv2.cvtColor(Blue, cv2.COLOR_BGR2HSV)

        Grey = cv2.imread('pictures/calibration/RGB/color_sampleGrey_rgb.jpg')
        #Greyh = cv2.cvtColor(Grey, cv2.COLOR_BGR2HSV)

        Yellow = cv2.imread('pictures/calibration/RGB/color_sampleYellow_rgb.jpg')
        #Yellowh = cv2.cvtColor(Yellow, cv2.COLOR_BGR2HSV)

        Black = cv2.imread('pictures/calibration/RGB/color_sampleBlack_rgb.jpg')
        #Blackh = cv2.cvtColor(Black, cv2.COLOR_BGR2HSV)

        Orange = cv2.imread('pictures/calibration/RGB/color_sampleOrange_rgb.jpg')
        #Orangeh = cv2.cvtColor(Orange, cv2.COLOR_BGR2HSV)

        White = cv2.imread('pictures/calibration/RGB/color_sampleWhite_rgb.jpg')
        #Whiteh = cv2.cvtColor(White, cv2.COLOR_BGR2HSV)


def imtomatrix(color,Type,gamma,hsv = 1):


        image = cv2.imread("pictures/%s/RGB/color_sample%s_rgb.jpg" %( Type, color))

        if hsv == 1:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        h, w, bpp = np.shape(image)


        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
                          for i in np.arange(0, 256)]).astype("uint8")
        image = cv2.LUT(image, table)

        average_color_per_row = np.average(image, axis =0)
        average_color = np.average(average_color_per_row, axis=0)
        average_color_f = np.uint8(average_color)
        average_color_f = np.array(average_color_f)
        print(average_color_f)
        cv2.imshow('tt',image)
        return average_color_f




