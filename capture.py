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

video=cv2.VideoCapture(0)
check, frame = video.read()
status=0
now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
now_date_str=str(now_date)
now_time=datetime.datetime.now().time().strftime("%X")
now_time_str=str(now_time)
gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(21,21),0)
#sec2=int(round(time.time()))
#textfile=open("time.txt","a")
#textfile.write("%s,"%now_time_str )
#key = cv2.waitKey(1)
#if key == ord("q"):
  #sys.exit()
  #break

if first_frame is None:
  first_frame=gray
  continue


    #sys.exit()
    #break

if True:
  textfile=open("count.txt","r")
  img_ctr=textfile.read()

  textfile.close()#SPACE
  img_counter=int(img_ctr)
  #img_ctr=str(img_counter)

  img_name=name_frame+"/frame"+img_ctr+".jpg".format(img_counter)
  img_name_f=name_frame+"/frame"+img_ctr+"_f.jpg".format(img_counter)
  text=now_date_str+"-"+now_time_str
  #sec=sec2
  textfile=open("count.txt","w")
  textfile.write(img_ctr)
  textfile.close()
  cv2.imwrite(img_name,frame)
  img=Image.open(img_name)
  draw=ImageDraw.Draw(img)
  #font = ImageFont.truetype("sans-serif.ttf", 16)
  draw.text((0, 0),text,(255,255,255))
  img.save(img_name_f)

  p=read_image(img_name)
  if p==1:
    take_screen()
    #imk=Image.open(img_name)
    #imk.load()
    #imk.show()
    #print("written".format(img_name))
  img_counter+=1
  textfile=open("count.txt","w")
  textfile.write(img_ctr)
  textfile.close()
video.release()
cv2.destroyAllWindows()
vedio.stop()
