import cv2
import math

videoFile = "C:/Users/user/Desktop/RoseBloom.mp4"
print(videoFile)
imagesFolder = "C:/Users/user/Desktop"
cap = cv2.VideoCapture(videoFile)
print(cap)
(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
     
if int(major_ver)  < 3 :
        fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
        frameRate=format(fps)
else :
        fps = cap.get(cv2.CAP_PROP_FPS)
        frameRate=format(fps)
print(frameRate)
print(type(frameRate))
frameRate=math.floor(int(float(frameRate)))
while(cap.isOpened()):
    print(1)
    frameId = cap.get(3)
    print(frameId)#current frame number
    ret, frame = cap.read()
    print(frame)
    if (ret != True):
        break
    if (frameId % (frameRate*10) == 0):
        filename = imagesFolder + "/image1" +  str(int(frameId)) + ".jpg"
        cv2.imwrite(filename, frame)
cap.release()
print('Done!')
