
import os,glob
import matplotlib.pyplot as plt 
import cv2 
import numpy as np
from PIL import Image 


counter=0
for files in glob.glob('*'):
    #print(files)
    if files.endswith('.py') or files.endswith('.gif') or files.endswith('.svg'):
        
        print("here",files)
        continue
    img = Image.open(files)
    array = np.array(img)
    if len(array.shape)<3:
        array=array.reshape(1,array.shape[0]*array.shape[1])
    else:
        array=array.reshape(1,array.shape[0]*array.shape[1]*array.shape[2])
        mean=np.mean(array)
        os.remove(files)
        
        
              
        
        
        
        
        
        #cv2.imshow('image',cv2.imread(files))
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()  
    #print(files,np.mean(array))
    #break
    