# Import all the required libraries for our program.
import cv2
import numpy as np
from pyzbar.pyzbar import decode

#  Access webcam 
captureImage=cv2.VideoCapture(0)
captureImage.set(3,640) #defining height of our output window as 640 (3 is use for height)
captureImage.set(4,480) #defining height of our output window as 480 (4 is use for height)


# Reading The Captured Frame 

#  Creating  2 variable ret and myframe 
def ReadQrCode():
    while True:
        ret, Myframe=captureImage.read()

        for image in decode(Myframe): # reading data from code and storing in variabke named mydata 
            print(image.data)
            mydata=image.data.decode('utf-8')
            print(mydata)

    # Drawing rectange Around Qr code and  didplaying data 
    # So first we will create a variable name pts which is points which will gives 
    # us 4 corner points of our QR code
            pts=np.array([image.polygon],np.int32)
            cv2.polylines(Myframe,[pts],True,(255,0,0), 5)

            pts2=image.rect
            cv2.putText(Myframe,mydata,[pts2[0],pts2[1], cv2.FONT_HERSHEY_COMPLEX ,1,(255,0,0),2])

    
        cv2.imshow('Camera Frame ',Myframe)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
