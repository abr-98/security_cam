from judge_diff import compare_images
from PIL import Image
import os,cv2
def caller ():
  textfile=open("count.txt","r")
  count2=textfile.read()
  textfile.close()
  count=int(count2)
  count3=0
  count_scr=0
  count1=str(count3)
  img1_s="frame"+count1+".jpg"
  img_s=img1_s
  #print(img_s)
  #img_g=cv2.imread(img_s)
  while count3<(count-1):

    count4=count3+1
    count5=str(count4)
    img2_s="frame"+count5+".jpg"
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
      img_f_s="frame"+count_str+".jpg"

      #print(img_f_s)
      #print("k")
      os.rename(img2_s,img_f_s)
      img_s=img_f_s
      textfile=open("count_scr.txt","w")
      textfile.write("%s" %count_scr)
      textfile.close()
    if r==1:
      #print("l")
      os.remove(img2_s)
    count3=count3+1
