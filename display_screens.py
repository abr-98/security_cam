from PIL import Image
import datetime
import cv2
from tkinter import messagebox
import os,subprocess
import sys
def display_screen():
    textfile=open("/home/abhijit/atom_projects/time.txt","r")
    now_time_str=textfile.read()

    textfile.close()
    now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
    now_date_str=str(now_date)
    name_screen="/home/abhijit/atom_projects/screen-"+now_date_str+"-"+now_time_str+"/"
    message="Please go to "+name_screen+"/ in the installed folder"
    messagebox.showinfo("File location",message )

if __name__ == '__main__':
    display_screen()
