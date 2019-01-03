import numpy as np
import cv2,sys
from matplotlib import pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

def read_image(str):
    #print (str)
    img = cv2.imread(str)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#cv2.imshow('img',img)
#cv2.imshow('gray',gray)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)==0:
        #print("l")
        return -1
    for (x,y,w,h) in faces:


        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        if len(eyes)==0:
            return -1
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    #    print(x," ",y," ",x+w," ",y+w," ",ex," ",ey)


        #textfile=open("vertical_record.txt","w")
        #textfile.write('%s' %y)
        #textfile.close()
        #textfile=open("horizontal_record.txt","w")
        #textfile.write('%s' %x)
        #textfile.close()
        #key = cv2.waitKey(1) & 0xFF
        #if key == ord("q"):
            #sys.exit()
            #break
        #cv2.imshow('img',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return 1
#if __name__ == '__main__':
#    p=read_image("frame2.jpg")
#    print(p)
