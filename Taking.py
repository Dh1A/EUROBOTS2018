#Images taking script for the Eurobot2018 **Inial Commit by DH1A**

import freenect
import cv2

import pathlib
import os

pictures = os.getcwd()

class ImagesTaking :
    def __init__(self):
        #Create Saving Folders
            #For Colors Calibration
        pathlib.Path('pictures/calibration/RGB').mkdir(parents=True, exist_ok=True)
        pathlib.Path('pictures/calibration/HSV').mkdir(parents=True, exist_ok=True)
            #For Decting actual Colors
        pathlib.Path('pictures/detection/RGB').mkdir(parents=True, exist_ok=True)
        pathlib.Path('pictures/detection/HSV').mkdir(parents=True, exist_ok=True)


    def calibrationtake(self,times):
        count = 0
        while count < times:

            cap = cv2.VideoCapture(1) #uncomment this if you are using your webcam /unplug kinect
            ret, orig = cap.read()

            #orig = freenect.sync_get_video()[0]

            rgb = cv2.cvtColor(orig, cv2.COLOR_RGB2BGR)

            hsv = cv2.cvtColor(orig, cv2.COLOR_RGB2HSV)

            count += 1
            cv2.imwrite("pictures/calibration/RGB/image%d_rgb.jpg" % count, orig)
            print('writing image%d_rgb in pictures/calibration/RGB' % count)
            cv2.imwrite("pictures/calibration/HSV/image%d_hsv.jpg" % count, hsv)
            print('writing image%d_hsv in pictures/calibration/HSV' % count)
            cap.release()

    def detectiontake(self, times):
        count = 0
        while count < times:
            cap = cv2.VideoCapture(1) #uncomment this if you are using your webcam /unplug kinect
            ret, orig = cap.read()

            #orig = freenect.sync_get_video()[0]

            rgb = cv2.cvtColor(orig, cv2.COLOR_RGB2BGR)

            hsv = cv2.cvtColor(orig, cv2.COLOR_RGB2HSV)

            count += 1
            cv2.imwrite("pictures/detection/RGB/image%d_rgb.jpg" % count, orig)
            print('writing image%d_rgb in pictures/detection/RGB' % count)
            cv2.imwrite("pictures/detection/HSV/image%d_hsv.jpg" % count, hsv)
            print('writing image%d_hsv in pictures/detection/HSV' % count)
            cap.release()
if __name__==" main ":

    ImagesTaking.calibrationtake(1)
    ImagesTaking.detectiontake(1)




