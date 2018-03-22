#Images Slicing Script for the EUROBOT2018 **Initial commit by DH1A

import cv2
import numpy as np
import os



def nothing(x):

    pass

def save(w,h,b,a,color,img,type):

    if type == 'c':

        saving = img[w:w+b, h:h+a]
        cv2.imwrite("pictures/calibration/RGB/color_sample%s_rgb.jpg"% color, saving)
        print("Saving calibration %s" % color)

    elif type == 'd':

        saving = img[w:w + b, h:h + a]
        cv2.imwrite("pictures/detection/RGB/color_sample%s_rgb.jpg" % color, saving)
        print("Saving detection %s" % color)


def CalibrationRGB(image):

    Img = cv2.imread('pictures/calibration/RGB/image%d_rgb.jpg' % image)

    #Windows Creation and resize

    cv2.namedWindow('RGB_Calibration',cv2.WINDOW_GUI_EXPANDED)
    cv2.namedWindow('RGB_',cv2.WINDOW_NORMAL )
    cv2.namedWindow('Config', cv2.WINDOW_AUTOSIZE)
    h, w, bpp = np.shape(Img)
    cv2.resizeWindow('RGB_', w,h)
    cv2.resizeWindow('RGB_Calibration', w, 1366)
    cv2.resizeWindow('Config', w, 200)
    cv2.moveWindow('RGB_Calibration',0,0)
    cv2.moveWindow('RGB_',w+10,0)
    cv2.moveWindow('Config', w+10,w+10 )


    #Grey_TrackBar
    cv2.createTrackbar('Grey_X','RGB_Calibration',0,h,nothing)
    cv2.createTrackbar('Grey_Y','RGB_Calibration',0,w,nothing)
    #Blue_TrackBar
    cv2.createTrackbar('Blue_X','RGB_Calibration',0,h,nothing)
    cv2.createTrackbar('Blue_Y','RGB_Calibration',0,w,nothing)
    # Yellow_TrackBar
    cv2.createTrackbar('Yellow_X', 'RGB_Calibration', 0, h, nothing)
    cv2.createTrackbar('Yellow_Y', 'RGB_Calibration', 0, w, nothing)
    # Black_TrackBar
    cv2.createTrackbar('Black_X', 'RGB_Calibration', 0, h, nothing)
    cv2.createTrackbar('Black_Y', 'RGB_Calibration', 0, w, nothing)
    # Green_TrackBar
    cv2.createTrackbar('Green_X', 'RGB_Calibration', 0, h, nothing)
    cv2.createTrackbar('Green_Y', 'RGB_Calibration', 0, w, nothing)
    # Orange_TrackBar
    cv2.createTrackbar('Orange_X', 'RGB_Calibration', 0, h, nothing)
    cv2.createTrackbar('Orange_Y', 'RGB_Calibration', 0, w, nothing)
    # White_TrackBar
    cv2.createTrackbar('White_X', 'RGB_Calibration', 0, h, nothing)
    cv2.createTrackbar('White_Y', 'RGB_Calibration', 0, w, nothing)
    # Square_Dim_TrackBar
    cv2.createTrackbar('Square_H', 'Config', 0, 20, nothing)
    cv2.createTrackbar('Square_W', 'Config', 0, 20, nothing)
    #SlicingExec_TrackBar
    switch = '0 : -- \n1 : Capture'
    cv2.createTrackbar(switch, 'Config',0,1,nothing)
    C = 0

    while True:
        #refresh image
        Img = cv2.imread('pictures/calibration/RGB/image%d_rgb.jpg' % image)



        #Getting TrackBars positions
        # SlicingExec_TrackBar
        C = cv2.getTrackbarPos(switch, 'Config')
        #Blue_Trackbar
        blh = cv2.getTrackbarPos('Blue_X', 'RGB_Calibration')
        blw = cv2.getTrackbarPos('Blue_Y', 'RGB_Calibration')
        # Grey_Trackbar
        gh = cv2.getTrackbarPos('Grey_X', 'RGB_Calibration')
        gw = cv2.getTrackbarPos('Grey_Y', 'RGB_Calibration')
        # Green_Trackbar
        grh = cv2.getTrackbarPos('Green_X', 'RGB_Calibration')
        grw = cv2.getTrackbarPos('Green_Y', 'RGB_Calibration')
        # Orange_Trackbar
        oh = cv2.getTrackbarPos('Orange_X', 'RGB_Calibration')
        ow = cv2.getTrackbarPos('Orange_Y', 'RGB_Calibration')
        # Black_Trackbar
        bh = cv2.getTrackbarPos('Black_X', 'RGB_Calibration')
        bw = cv2.getTrackbarPos('Black_Y', 'RGB_Calibration')
        # Yellow_Trackbar
        yh = cv2.getTrackbarPos('Yellow_X', 'RGB_Calibration')
        yw = cv2.getTrackbarPos('Yellow_Y', 'RGB_Calibration')
        # White_Trackbar
        wh = cv2.getTrackbarPos('White_X', 'RGB_Calibration')
        ww = cv2.getTrackbarPos('White_Y', 'RGB_Calibration')
        # Rectangle_size_Trackbar
        a = cv2.getTrackbarPos('Square_H', 'Config')
        b = cv2.getTrackbarPos('Square_W', 'Config')

        #displaying rectangles
        #Grey_Rectangle
        cv2.rectangle(Img, (gh, gw), (gh + a, gw + b), (108, 108, 112), 1)
        # Orange_Rectangle
        cv2.rectangle(Img, (oh, ow), (oh + a, ow + b), (4, 168, 250), 1)
        # Yellow_Rectangle
        cv2.rectangle(Img, (yh, yw), (yh + a, yw + b), (92, 236, 252), 1)
        # Black_Rectangle
        cv2.rectangle(Img, (bh, bw), (bh + a, bw + b), (0, 0, 0), 1)
        # Green_Rectangle
        cv2.rectangle(Img, (grh, grw), (grh + a, grw + b), (35, 189, 50), 1)
        # Blue_Rectangle
        cv2.rectangle(Img, (blh, blw), (blh + a, blw + b), (255, 0, 0), 1)
        # White_Rectangle
        cv2.rectangle(Img, (wh, ww), (wh + a, ww + b), (255, 255, 255), 1)

        #Display
        cv2.imshow('RGB_', Img)
        cv2.waitKey(1)

        #This is a simulation of the button function since it's not available without Qt Support
        if C == 1:
            #File in which to save each square cordinate for automated execution//
            file = open('Calibration.txt', "w")
            #Yellow Sample Save
            save(yw,yh,b,a,"Yellow",Img,'c')
            file.write('%d\n' % yw)
            file.write('%d\n' % yh)
            # Blue Sample Save
            save(blw, blh, b, a, "Blue", Img,'c')
            file.write('%d\n' % blw)
            file.write('%d\n' % blh)
            # Black Sample Save
            save(bw, bh, b, a, "Black", Img,'c')
            file.write('%d\n' % bw)
            file.write('%d\n' % bh)
            # Grey Sample Save
            save(gw, gh, b, a, "Grey", Img,'c')
            file.write('%d\n' % gw)
            file.write('%d\n' % gh)
            # White Sample Save
            save(ww, wh, b, a,"White", Img,'c')
            file.write('%d\n' % ww)
            file.write('%d\n' % wh)
            # Green Sample Save
            save(grw, grh, b, a, "Green", Img,'c')
            file.write('%d\n' % grw)
            file.write('%d\n' % grh)
            # Orange Sample Save
            save(ow, oh, b, a, "Orange", Img,'c')
            file.write('%d\n' % ow)
            file.write('%d\n' % oh)
            file.write('file layout : (yellow w/h)(line1/2) (blue w/h)(line3/4)\n')
            file.write('file layout : (black w/h)(line5/6)(grey w/h)(line7/8)\n')
            file.write('file layout : ( white w/h)(line9/10)(green w/h)(line11/12)\n')
            file.write('file layout : ( orange w/h)(line13/14)\n')
            file.close()
            cv2.destroyAllWindows()
            break
        else:
            pass

def DetectionRGB(image):

    Img = cv2.imread('pictures/detection/RGB/image%d_rgb.jpg' % image)

    #Windows Creation and resize

    cv2.namedWindow('RGB_Testing',cv2.WINDOW_GUI_EXPANDED)
    cv2.namedWindow('RGB_',cv2.WINDOW_NORMAL )
    cv2.namedWindow('Config', cv2.WINDOW_AUTOSIZE)
    h, w, bpp = np.shape(Img)
    cv2.resizeWindow('RGB_', w,h)
    cv2.resizeWindow('RGB_Testing', w, 1366)
    cv2.resizeWindow('Config', w, 200)
    cv2.moveWindow('RGB_Testing',0,0)
    cv2.moveWindow('RGB_',w+10,0)
    cv2.moveWindow('Config', w+10,w+10 )


    #FirstColor TrackBar
    cv2.createTrackbar('First_X','RGB_Testing',0,h,nothing)
    cv2.createTrackbar('First_Y','RGB_Testing',0,w,nothing)
    #SecondColor_TrackBar
    cv2.createTrackbar('Second_X','RGB_Testing',0,h,nothing)
    cv2.createTrackbar('Second_Y','RGB_Testing',0,w,nothing)
    # ThirdColor_TrackBar
    cv2.createTrackbar('Third_X', 'RGB_Testing', 0, h, nothing)
    cv2.createTrackbar('Third_Y', 'RGB_Testing', 0, w, nothing)
    # Square_Dim_TrackBar
    cv2.createTrackbar('Square_H', 'Config', 0, 30, nothing)
    cv2.createTrackbar('Square_W', 'Config', 0, 30, nothing)
    #SlicingExec_TrackBar
    switch = '0 : -- \n1 : Capture'
    cv2.createTrackbar(switch, 'Config',0,1,nothing)
    C = 0

    while True:
        #refresh image
        Img = cv2.imread('pictures/detection/RGB/image%d_rgb.jpg' % image)



        #Getting TrackBars positions
        # SlicingExec_TrackBar
        C = cv2.getTrackbarPos(switch, 'Config')
        # FirstColor TrackBar
        Fx = cv2.getTrackbarPos('First_X', 'RGB_Testing')
        Fy = cv2.getTrackbarPos('First_Y', 'RGB_Testing')
        # SecondColor TrackBar
        Sx = cv2.getTrackbarPos('Second_X', 'RGB_Testing')
        Sy = cv2.getTrackbarPos('Second_Y', 'RGB_Testing')
        # ThirdColor TrackBar
        Tx = cv2.getTrackbarPos('Third_X', 'RGB_Testing')
        Ty = cv2.getTrackbarPos('Third_Y', 'RGB_Testing')
        #h=x Rectangle_size_Trackbar
        a = cv2.getTrackbarPos('Square_H', 'Config')
        b = cv2.getTrackbarPos('Square_W', 'Config')

        #displaying rectangles
        #First_Rectangle Grey
        cv2.rectangle(Img, (Fx, Fy), (Fx + a, Fy + b), (108, 108, 112), 1)
        # Second_Rectangle Orange
        cv2.rectangle(Img, (Sx, Sy), (Sx + a, Sy + b), (4, 168, 250), 1)
        # Yellow_Rectangle Yellow
        cv2.rectangle(Img, (Tx, Ty), (Tx + a, Ty + b), (92, 236, 252), 1)

        #Display
        cv2.imshow('RGB_', Img)
        cv2.waitKey(1)

        #This is a simulation of the button function since it's not available without Qt Support
        if C == 1:
            #File in which to save each square cordinate for automated execution//
            file = open('TestCoordinate.txt', "w")
            #FirstColor Save
            save(Fy,Fx,b,a,"First",Img,'d')
            file.write('%d\n' % Fy)
            file.write('%d\n' % Fx)
            #SecondColor Save
            save(Sy, Sx, b, a, "Second", Img,'d')
            file.write('%d\n' % Sy)
            file.write('%d\n' % Sx)
            #ThirdColor Save
            save(Ty, Tx, b, a, "Third", Img,'d')
            file.write('%d\n' % Ty)
            file.write('%d\n' % Tx)
            file.write('file layout : (First w/h)(line1/2) (Second w/h)(line3/4)\n')
            file.write('file layout : (Third w/h)(line5/6)\n')
            file.close()
            cv2.destroyAllWindows()
            break
        else:
            pass
if __name__ == " main ":


    DetectionRGB(1)











