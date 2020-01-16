import cv2
import numpy as np
import os
import math

def partA():


    videoFile = r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Video Processing\Videos\RoseBloom.mp4'
    cap = cv2.VideoCapture(videoFile)
    (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
    fps = cap.get(cv2.CAP_PROP_FPS)
    frameRate=format(fps)
    frameRate=math.floor(int(float(frameRate)))
    frameId=cap.get(1)
    ret, frame = cap.read()
    if (frameId % (frameRate*6) == 0):
            filename = r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Video Processing\Generated\frame_as_6.jpg'
            cv2.imwrite(filename, frame)
            print(filename)
    cap.release()


def partB():


    image=cv2.imread(r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Video Processing\Generated\frame_as_6.jpg')
    
    image[:,:,0]=0
    image[:,:,1]=0
    cv2.imshow('R-RGB',image)
    cv2.imwrite(r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Video Processing\Generated\frame_as_6_red.jpg',image)
    cv2.waitKey(0)


partA()
partB()
