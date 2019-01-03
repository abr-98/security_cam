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
first_frame=None
status_list=[None,None]
img_counter=0
#t=0
now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
now_date_str=str(now_date)
now_time=datetime.datetime.now().time().strftime("%X")
now_time_str=str(now_time)
name_frame="frame-"+now_date_str+"-"+now_time_str
name_screen="screen-"+now_date_str+"-"+now_time_str
os.makedirs(name_frame)
#os.chmod(name_frame, 0o777)
#os.chmod(name_frame, 0o755)
os.makedirs(name_screen)
#os.chmod(name_screen, 0o777)
#os.chmod(name_screen, 0o755)
video=cv2.VideoCapture(0)
count=0
textfile=open("count_screen.txt","w")
textfile.write('0')
textfile.close()
textfile=open("time.txt","w")
textfile.write(now_time_str)
textfile.close()
textfile=open("count.txt","w")
textfile.close()
sec = int(round(time.time()))
t=sec
print("press ctrl+c to exit")
while True:
    check, frame = video.read()
    status=0
    now_time=datetime.datetime.now().time().strftime("%X")
    now_time_str=str(now_time)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    sec2=int(round(time.time()))
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

    if (sec2-sec)==3:  #SPACE
        img_ctr=str(img_counter)

        img_name=name_frame+"/frame"+img_ctr+".jpg".format(img_counter)
        img_name_f=name_frame+"/frame"+img_ctr+"_f.jpg".format(img_counter)
        text=now_date_str+"-"+now_time_str
        sec=sec2
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
    #key = cv2.waitKey(1)
    #if key == ord("q"):
        #sys.exit()
        #break

video.release()
cv2.destroyAllWindows()
vedio.stop()
