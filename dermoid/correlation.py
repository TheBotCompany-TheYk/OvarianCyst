import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import time
def segmentation(gray):
    ret, thresh = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU) 
    histg = cv2.calcHist([img],[0],None,[256],[0,256]) 
    return histg

def edgedetect(gray):
    for i in range(0,400,50):
        for j in range(0,400,50):
            edges=cv2.Canny(gray,i,j)
            print(i,j)
            edges_high_thresh=cv2.Canny(gray,20,20)
            images=np.hstack((gray,edges,edges_high_thresh))
            cv2.imshow('Images',images)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
i=0
mean_arr=[]
std_arr=[]
median_arr=[]

while i<13:
    img=cv2.imread('Cropped-image'+str(i)+'.jpg')
    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    imagesShow.append(segmentation(gray))
    gray=gray.flatten()
    mean_arr.append(np.mean(gray))
    std_arr.append(np.std(gray))
    median_arr.append(np.median(gray))
    i+=1


cv2.imshow('output',np.hstack(imagesShow))
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
plt.scatter([i for i in range(13)],mean_arr,label="mean")
plt.scatter([i for i in range(13)],std_arr,label="std_deviation")
plt.scatter([i for i in range(13)],median_arr,label="median")
plt.xlabel('Cropped Image ')
plt.ylabel(' Statistical parameters')
plt.legend()
plt.show()
'''