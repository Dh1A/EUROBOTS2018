import cv2
import numpy as np
import pathlib
import os
from time import sleep
import Taking
import ColorPlot
import SlicingScript
import IntervalsCalc
#from lib_nrf24 import NRF24
# Radio_init

#pipes = [[0xe7, 0xe7, 0xe7, 0xe7, 0xe7], [0xc2, 0xc2, 0xc2, 0xc2, 0xc2]]

#radio = NRF24(GPIO, GPIO.SpiDev())
#radio.begin(10, 8) #Set spi-ce pin10, and rf24-CE pin 8
#time.sleep(1)
#radio.setRetries(15,15)
#radio.setPayloadSize(32)
#radio.setChannel(0x60)

#radio.setDataRate(NRF24.BR_2MBPS)
#radio.setPALevel(NRF24.PA_MIN)
#radio.setAutoAck(True)
#radio.enableDynamicPayloads()
#radio.enableAckPayload()


#radio.openWritingPipe(pipes[1])
#radio.openReadingPipe(1, pipes[0])
#radio.printDetails()



pictures = os.getcwd()

# For Colors Calibration
pathlib.Path('pictures/calibration/RGB').mkdir(parents=True, exist_ok=True)
pathlib.Path('pictures/calibration/HSV').mkdir(parents=True, exist_ok=True)
# For Decting actual Colors
pathlib.Path('pictures/detection/RGB').mkdir(parents=True, exist_ok=True)
pathlib.Path('pictures/detection/HSV').mkdir(parents=True, exist_ok=True)


def save(w,h,b,a,color,img,type):

    if type == 'c':

        saving = img[w:w+b, h:h+a]
        cv2.imwrite("pictures/calibration/RGB/color_sample%s_rgb.jpg"% color, saving)
        #print("Saving calibration %s" % color)

    elif type == 'd':

        saving = img[w:w + b, h:h + a]
        cv2.imwrite("pictures/detection/RGB/color_sample%s_rgb.jpg" % color, saving)
        print("Saving detection %s" % color)


def detectiontake(times):
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
        cap.release()
def detect():

    global firstcolor , secondcolor,thirddcolor

    detectiontake(1)
    Img = cv2.imread('pictures/detection/RGB/image1_rgb.jpg')


    #Reading coordinate from file
    file = open('Calibration.txt', "r")
    CaL = file.readlines()

    #affecting each coordinate to its color and slicing the image


    YellowW = CaL[0]
    print(YellowW)
    YellowW = int(YellowW)
    print(YellowW)
    YellowH = CaL[1]
    YellowH = int(YellowH)
    save(YellowW,YellowH,10,10,"Yellow",Img,"c")

    BlueW = CaL[2]
    BlueW=int(BlueW)
    BlueH = CaL[3]
    BlueH=int(BlueH)
    save(BlueW,BlueH,10,10,"Blue",Img,"c")

    BlackW = CaL[4]
    BlackW=int(BlackW)
    BlackH = CaL[5]
    BlackH=int(BlackH)
    save(BlackW,BlackH,10,10,"Black",Img,"c")


    GreyW = CaL[6]
    GreyW = int(GreyW)
    GreyH = CaL[7]
    GreyH = int(GreyH)
    save(GreyW,GreyH,10,10,"Grey",Img,"c")



    WhiteW = CaL[8]
    WhiteW=int(WhiteW)
    WhiteH = CaL[9]
    WhiteH=int(WhiteH)
    save(WhiteW,WhiteH,10,10,"White",Img,"c")


    GreenW = CaL[10]
    GreenW=int(GreenW)
    GreenH = CaL[11]
    GreenH=int(GreenH)
    save(GreenW,GreenH,10,10,"Green",Img,"c")


    OrangeW = CaL[12]
    OrangeW=int(OrangeW)
    OrangeH = CaL[13]
    OrangeH=int(OrangeH)
    save(OrangeW,OrangeH,10,10,"Orange",Img,"c")


    file.close()

    #TestCoordinate

    file1 = open("TestCoordinate.txt","r")
    DetL = file1.readlines()

    FirstW = DetL[0]
    FirstW=int(FirstW)
    FirstH = DetL[1]
    FirstH=int(FirstH)
    save(FirstW,FirstH,10,10,"First",Img,"d")

    SecondW = DetL[2]
    SecondW=int(SecondW)
    SecondH = DetL[3]
    SecondH=int(SecondH)
    save(SecondW,SecondH,10,10,"Second",Img,"d")


    ThirdW = DetL[4]
    ThirdW=int(ThirdW)
    ThirdH = DetL[5]
    ThirdH=int(ThirdH)
    save(ThirdW,ThirdH,10,10,"Third",Img,"d")

    file1.close()

    #SavingImages


    Black = IntervalsCalc.imtomatrix("Black","calibration",1.5)
    print("Black :",Black)

    Blue = IntervalsCalc.imtomatrix("Blue","calibration",1.5)
    print("Blue :", Blue)
    Yellow = IntervalsCalc.imtomatrix("Yellow","calibration",1.5)
    print("Yellow :", Yellow)
    Grey = IntervalsCalc.imtomatrix("Grey","calibration",1.5)
    print("Grey :", Grey)
    White = IntervalsCalc.imtomatrix("White","calibration",1.5)
    print("White :", White)
    Green = IntervalsCalc.imtomatrix("Green","calibration",1.5)
    print("Green :", Green )

    Orange = IntervalsCalc.imtomatrix("Orange","calibration",1.5)

    print("orange :" ,Orange)

    first = IntervalsCalc.imtomatrix("First","detection",1.5)
    print("first :" ,first)
    second = IntervalsCalc.imtomatrix("Second","detection",1.5)
    print("second : ",second)
    third = IntervalsCalc.imtomatrix("Third","detection",1.5)
    print("third : ",third)

    #Determinig the colors
     #first

    #x = np.array([Black,Blue,Yellow,Grey,Green,Orange])
    #x1 = np.array([first[0],first[1],first[2]])
    #result = np.array(([0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]), dtype=np.int8)
    #for i in range(5):
#
 #       result[i] = x[i]-x1
  #      print(x[i]-x1)
   # print(result)

    if np.allclose(Black,first,0,20):
        firstcolor = "Black"
    elif np.allclose(Blue,first,0,20):
        firstcolor = "Blue"
    elif np.allclose(Yellow,first,0,20):
        firstcolor = "Yellow"
    elif np.allclose(Grey,first,0,20):
        firstcolor = "Grey"
    elif np.allclose(Green,first,0,20):
        firstcolor = "Green"
    elif np.allclose(Orange,first,0,20):
        firstcolor = "Orange"
    else: firstcolor = "any"


    #second

    if np.allclose(Black,second,0,20):
        secondcolor = "Black"
    elif np.allclose(Blue,second,0,20):
        secondcolor = "Blue"
    elif np.allclose(Yellow,second,0,20):
        secondcolor = "Yellow"
    elif np.allclose(Grey,second,0,20):
        secondcolor = "Grey"
    elif np.allclose(Green,second,0,20):
        secondcolor = "Green"
    elif np.allclose(Orange,second,0,20):
        secondcolor = "Orange"
    else: secondcolor = "any"
    #third
    if np.allclose(Black,third,0,25):
        thirddcolor = "Black"
    elif np.allclose(Blue,third,0,25):
        thirddcolor = "Blue"
    elif np.allclose(Yellow,third,0,25):
        thirddcolor = "Yellow"
    elif np.allclose(Grey,third,0,25):
        thirddcolor = "Grey"
    elif np.allclose(Green,third,0,25):
        thirddcolor = "Green"
    elif np.allclose(Orange,third,0,25):
        thirddcolor = "Orange"
    else: thirddcolor = "any"
    print(firstcolor)
    print(secondcolor)
    print(thirddcolor)

def Sending():

    global firstcolor, secondcolor, thirddcolor

    packet = list(firstcolor + secondcolor + thirddcolor+" ")
    radio.write(packet)

detect()
