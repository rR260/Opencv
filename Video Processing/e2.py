   #part A
import cv2
import math
videoFile = "C:/Users/user/Desktop/RoseBloom.mp4"
imagesFolder = "C:/Users/user/Desktop"
cap = cv2.VideoCapture(videoFile)
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
fps = cap.get(cv2.CAP_PROP_FPS)
frameRate=format(fps)
frameRate=math.floor(int(float(frameRate)))
frameId=cap.get(1)
ret, frame = cap.read()
if (frameId % (frameRate*6) == 0):
        filename = imagesFolder + "/frame_as_6.jpg"
        cv2.imwrite(filename, frame)
cap.release()
#part B
image=cv2.imread(filename)
image2=image.copy()
image2[:,:,0]=0
image2[:,:,1]=0
cv2.imshow('R-RGB',image2)
cv2.imwrite("C:/Users/user/Desktop/frame_as_6_red21.jpg",image2)
cv2.waitKey(0)
