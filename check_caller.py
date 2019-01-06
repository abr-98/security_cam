from judge_diff import compare_images
from PIL import Image
from flush_memo import delete
import os,cv2,datetime
def caller ():
  textfile=open("/home/abhijit/atom_projects/time.txt","r")
  now_time_str=textfile.read()

  textfile.close()
  textfile=open("/home/abhijit/atom_projects/count.txt","r")
  count2=textfile.read()
  now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
  now_date_str=str(now_date)
  textfile.close()
  name_frame="/home/abhijit/atom_projects/frame-"+now_date_str+"-"+now_time_str
  count=int(count2)
  count3=0
  count_scr=0
  count1=str(count3)
  img1_s=name_frame+"/frame"+count1+".jpg"
  img_s=img1_s

  textfile=open("/home/abhijit/atom_projects/count_scr.txt","w")
  textfile.write("%s" %count_scr)
  textfile.close()
  #print(img_s)
  #img_g=cv2.imread(img_s)
  while count3<(count-1):

    count4=count3+1
    count5=str(count4)
    img2_s=name_frame+"/frame"+count5+".jpg"
    img2_s_f=name_frame+"/frame"+count5+"_f.jpg"
    #print(img_s)
    #print(img2_s)
    #img2_g=cv2.imread(img2_s)
    #img_g=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #img2_g=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

    r=compare_images(img_s,img2_s)
    #print(r)
    if r==-1:


     # print(count_scr)
      count_str=str(count_scr)
     # print(count_str)
      count_scr=count_scr+1
      img_f_s=name_frame+"/frame"+count_str+".jpg"
      img_f_s_f=name_frame+"/frame"+count_str+"_f.jpg"
      #print(img_f_s)
      #print("k")
      os.rename(img2_s,img_f_s)
      os.rename(img2_s_f,img_f_s_f)
      img_s=img_f_s
      textfile=open("/home/abhijit/atom_projects/count_scr.txt","w")
      textfile.write("%s" %count_scr)
      textfile.close()
    if r==1:
      #print("l")
      os.remove(img2_s)
      os.remove(img2_s_f)
    count3=count3+1
  delete()
