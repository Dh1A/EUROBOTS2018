import cv2
import numpy as np
import pathlib
import os
from time import sleep
import Taking
import ColorPlot
import SlicingScript


take = Taking.ImagesTaking()

take.calibrationtake(3)

input("press enter to continue..")

take.detectiontake(3)

SlicingScript.CalibrationRGB(1)

SlicingScript.DetectionRGB(1)

