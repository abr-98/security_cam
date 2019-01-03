import datetime
import sys
import os
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
count=0
textfile=open("count_screen.txt","w")
textfile.write('0')
textfile.close()
textfile=open("time.txt","w")
textfile.write(now_time_str)
textfile.close()
textfile=open("count.txt","w")
textfile.write('0')
textfile.close()
