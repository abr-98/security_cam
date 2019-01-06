import pyscreenshot as ImageGrab
#import smtplib
import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from flush_screens import delete
from judge_diff import compare_images
import os,cv2,sys

def take_screen():
    textfile=open("/home/abhijit/atom_projects/time.txt","r")
    now_time_str=textfile.read()

    textfile.close()
    now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
    now_date_str=str(now_date)
    name_screen="/home/abhijit/atom_projects/screen-"+now_date_str+"-"+now_time_str
    textfile=open("/home/abhijit/atom_projects/count_screen.txt","r")
    img_ctr_2=textfile.read()
    textfile.close()
    img_counter=int(img_ctr_2)
    #print(img_counter)
    img_ctr=str(img_counter)
    image=name_screen+"/screen"+img_ctr+".jpg"
    image_f=name_screen+"/screen"+img_ctr+"_f.jpg"
    #print(image)
    now_time=datetime.datetime.now().time().strftime("%X")
    now_time_str=str(now_time)
    text=now_date_str+"-"+now_time_str
    ImageGrab.grab().save(image, "JPEG")
    img=Image.open(image)
    draw=ImageDraw.Draw(img)
    #font = ImageFont.truetype("sans-serif.ttf", 16)
    draw.text((0, 0),text,(255,255,255))
    img.save(image_f)
    #key = cv2.waitKey(1) & 0xFF
    #if key == ord("q"):
        #sys.exit()
        #break
    if img_counter==0:
       img_counter=img_counter+1
       #print(img_counter)
       textfile=open("/home/abhijit/atom_projects/count_screen.txt","w")
       textfile.write("%s" % img_counter)
       textfile.close()
    elif img_counter>0:
      img_prev=img_counter-1
      #print(img_prev)
      img_prev_str=str(img_prev)
      image_prev_n=name_screen+"/screen"+img_prev_str+".jpg"
      #print(image)
      #print(image_prev_n)
      p=compare_images(image,image_prev_n)
      if p==-1:
        img_counter=img_counter+1
        #print(img_counter)
        textfile=open("/home/abhijit/atom_projects/count_screen.txt","w")
        textfile.write("%s" % img_counter)
        textfile.close()
      else:
        os.remove(image)
        os.remove(image_f)
