from skimage.color import rgb2gray
import numpy as np
import cv2
import matplotlib.pyplot as plt
from scipy import ndimage
import os
image = plt.imread(os.getcwd()+'\\1.jpeg')
#image.shape
#plt.imshow(image)
# rgb2gray returns np array
gray = rgb2gray(image)
#plt.imshow(gray, cmap='gray')

# Reshape the ND array of x row and Y columns to 1 row with X*Y columns
#                    <-  Width ->|<- height ->|
Shape=gray.shape
gray= (gray.reshape(gray.shape[0]*gray.shape[1]))
#finds out the mean of the image
print(gray)
mean=gray.mean()

#threshold to be mean. Anything less than threshold would be 0 and wiz
for i in range(gray.shape[0]):
    if(gray[i]<mean):
        gray[i]=0
    else:
        gray[i]=1
print(gray)
gray=gray.reshape(Shape[0],Shape[1])
plt.imshow(gray, cmap='gray')


