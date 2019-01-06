import datetime
import sys
import os
import subprocess
from subprocess import call
img_counter=0
exec_code=call("python3 /home/abhijit/atom_projects/permission.py",shell=True)
#t=0
now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
now_date_str=str(now_date)
now_time=datetime.datetime.now().time().strftime("%X")
now_time_str=str(now_time)
name_frame="/home/abhijit/atom_projects/frame-"+now_date_str+"-"+now_time_str
name_screen="/home/abhijit/atom_projects/screen-"+now_date_str+"-"+now_time_str
os.makedirs(name_frame)
subprocess.call(['chmod', '+x', name_frame])

os.chmod(name_frame, 0o777)
os.chmod(name_frame, 0o755)
os.chmod(name_frame, 0o744)
#os.chmod(name_frame, '+x')
os.makedirs(name_screen)
subprocess.call(['chmod', '+x', name_screen])
os.chmod(name_screen, 0o777)
os.chmod(name_screen, 0o755)
os.chmod(name_screen, 0o744)
#os.chmod(name_screen, '+x')
count=0
textfile=open("/home/abhijit/atom_projects/count_screen.txt","w")
textfile.write('0')
textfile.close()
textfile=open("/home/abhijit/atom_projects/time.txt","w")
textfile.write(now_time_str)
textfile.close()
textfile=open("/home/abhijit/atom_projects/count.txt","w")
textfile.write('0')
textfile.close()
