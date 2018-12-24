import cv2, time
import sys
from check_caller import caller
from screen_control import take_screen
from PIL import Image
from face_detect_sec import read_image
first_frame=None
status_list=[None,None]
img_counter=0
#t=0
video=cv2.VideoCapture(0)
count=0
textfile=open("count_screen.txt","w")
textfile.write('0')
textfile.close()
textfile=open("count.txt","w")
textfile.close()
sec = int(round(time.time()))
t=sec
print("press ctrl+c to exit")
while True:
    check, frame = video.read()
    status=0
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    sec2=int(round(time.time()))

    if first_frame is None:
        first_frame=gray
        continue

    key=cv2.waitKey(0)
    #t=t+1

    if key == 27:
      #ESC
      #print("closing")

      sys.exit()
      break

    if (sec2-sec)==3:  #SPACE
        img_ctr=str(img_counter)

        img_name="frame"+img_ctr+".jpg".format(img_counter)
        p=read_image(img_name)
        if p==1:
            take_screen()
        sec=sec2
        textfile=open("count.txt","w")
        textfile.write(img_ctr)
        textfile.close()
        cv2.imwrite(img_name,frame)
        #imk=Image.open(img_name)
        #imk.load()
        #imk.show()
        #print("written".format(img_name))
        img_counter+=1

video.release()
cv2.destroyAllWindows()
