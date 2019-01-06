import cv2, time
import datetime
import sys
import os
from check_caller import caller
from screen_control import take_screen
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from face_detect_sec import read_image
now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
now_date_str=str(now_date)


video=cv2.VideoCapture(0)

while True:
    check, frame = video.read()
    status=0

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    if True:
      textfile=open("/home/abhijit/atom_projects/count.txt","r")
      img_ctr=textfile.read()

      textfile.close()#SPACE
      img_counter=int(img_ctr)
      #img_ctr=str(img_counter)
      textfile=open("/home/abhijit/atom_projects/time.txt","r")
      now_time_str=textfile.read()
      name_frame="/home/abhijit/atom_projects/frame-"+now_date_str+"-"+now_time_str
      textfile.close()
      img_name=name_frame+"/frame"+img_ctr+".jpg"
      img_name_f=name_frame+"/frame"+img_ctr+"_f.jpg"
      text=now_date_str+"-"+now_time_str
      #sec=sec2
      textfile=open("/home/abhijit/atom_projects/count.txt","w")
      textfile.write(img_ctr)
      textfile.close()
      cv2.imwrite(img_name,frame)
      img=Image.open(img_name)
      draw=ImageDraw.Draw(img)
      #font = ImageFont.truetype("sans-serif.ttf", 16)
      draw.text((0, 0),text,(255,255,255))
      img.save(img_name_f)
      print(img_name)
      p=read_image(img_name)
      if p==1:
        take_screen()
        #imk=Image.open(img_name)
        #imk.load()
        #imk.show()
        #print("written".format(img_name))
      img_counter+=1
      img_ctr_2=str(img_counter)
      textfile=open("/home/abhijit/atom_projects/count.txt","w")
      textfile.write(img_ctr_2)
      textfile.close()
      break

video.release()
cv2.destroyAllWindows()
#video.stop()
