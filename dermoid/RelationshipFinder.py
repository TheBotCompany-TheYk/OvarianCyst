import cv2
from matplotlib import pyplot as plt
import ctypes
i=0
img=cv2.imread('dermoid0.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

while i<1:
    img=cv2.imread('dermoid'+str(i)+'.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #.imshow('image',gray)
    print(gray)
    r = cv2.selectROI(gray)
    imCrop = gray[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

    cv2.imshow("Image", imCrop)

    cv2.imwrite('Cropped-imagesvg'+str(i)+'.svg',imCrop)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    i+=1
