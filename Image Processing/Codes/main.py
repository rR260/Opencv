import cv2
import numpy as np
import os
import csv
import cv2

def partA():
    
    with open(r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Generated\stats.csv', 'w') as csvfile:
        for i in range(4):
            path = r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Images'
            if(i==0):
                v1='bird.jpg'
                image1=os.path.join(path,v1);
            elif(i==1):
                v1='cat.jpg'
                image1=os.path.join(path,v1);
            elif(i==2):
                v1='flowers.jpg'
                image1=os.path.join(path,v1);
            elif(i==3):
                v1='horse.jpg'
                image1=os.path.join(path,v1);
            image = cv2.imread(image1)
            window_name = 'image'
            heightc,widthc= image.shape[0:2]
            channelc= image.shape[2]
            (B,G,R)= image[int(heightc/2),int(widthc/2)]
            with open(r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Generated\stats.csv', 'a',newline='') as csvfile:
               filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
               filewriter.writerow([v1,heightc,widthc,channelc,B,G,R])



def partB():


    path = r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Images\cat.jpg' 
    image = cv2.imread(path)
    image2= image.copy()
    image2[:, :, 0]=0
    image2[:, :, 1]=0
    cv2.imwrite(r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Generated\cat_red.jpg',image2)
    cv2.waitKey(0)

    
def partC():

    path = r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Images\flowers.jpg' 
    image = cv2.imread(path)
    b_channel, g_channel, r_channel = cv2.split(image)
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 50 #creating a dummy alpha channel image.
    image1 = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))
    channelc= image1.shape[2]
    print("channel3",channelc)
    cv2.imwrite(r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Generated\flowers_alpha.png',image1)


    
def partD():



    path = r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Images\horse.jpg' 
    img = cv2.imread(path)
    height = img.shape[0]
    width = img.shape[1]
    gray = img[:, :, 0].copy()
    for x in range(img.shape[1]):
      for y in range(img.shape[0]):
         gray[y][x]= (0.11 * img[y][x][0] + 0.59 * img[y][x][1] + 0.3 * img[y][x][2])
    print(gray)
    #cv2.imshow('gray',gray)
    cv2.imwrite(r'C:\Users\HP\Downloads\SB#5020_Task0\Task0.2\Image Processing\Generated\horse_gray.jpg',gray)
    cv2.waitKey(0)

    

partA()
partB()
partC()
partD()

