import os
import cv2




img=("images/1.PNG","images/2.PNG","images/3.PNG","images/4.PNG","images/5.PNG","images/6.PNG","images/7.PNG","images/8.PNG","images/9.PNG","images/10.PNG","images/11.PNG","images/12.PNG","images/13.PNG","images/14.PNG","images/15.PNG","images/16.PNG","images/17.PNG","images/18.PNG","images/19.PNG","images/20.PNG",cv2.IMREAD_UNCHANGED)

count = len(img)
frame=cv2.imread(img[0])
height,width,channel= frame.shape
size= (width,height)

print(size)

out=cv2.VideoWriter("friends.mp4",cv2.VideoWriter.fourcc(*'mp4v'),0.8,size)

for i in range(0,count-1):
    video=cv2.imread(img[i])
    out.write(video)


cv2.VideoCapture("friends.mp4")