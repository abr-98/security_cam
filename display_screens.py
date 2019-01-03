from PIL import Image
import datetime
import cv2
from tkinter import messagebox
import os,subprocess
import sys
def display_screen():
    textfile=open("time.txt","r")
    now_time_str=textfile.read()

    textfile.close()
    now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
    now_date_str=str(now_date)
    name_screen="screen-"+now_date_str+"-"+now_time_str+"/"
    message="Please go to "+name_screen+"/ in the installed folder"
    messagebox.showinfo("File location",message )

if __name__ == '__main__':
    display_screen()
