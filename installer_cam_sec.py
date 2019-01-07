import tkinter
import tkinter.filedialog
import os


root=tkinter.Tk()
root.withdraw()

#print("Select the destination directory")
#print(" PS:go inside it then select open")


filename=tkinter.filedialog.askdirectory(parent=root,initialdir="/home",title='Please select a destination directory')
command="cd "+filename
os.system(command)
name=filename+"/cam_security_setup"
cmd="mkdir "+ name
os.system(cmd)
os.system("cd cam_security_setup")
text_file=filename+"/cam_security_setup"+"/destination.txt"
app=filename+"/cam_security"+"/cam_sec.desktop"
textfile=open(text_file,"w")
textfile.write(filename)
textfile.close()
filename2=tkinter.filedialog.askdirectory(parent=root,initialdir="/home",title='Please go to desktop folder')

os.system("git clone https://github.com/abr-98/cam_security")
command2="cp "+app+" "+filename2
os.system(command2)
cmd="sudo chmod +x "+app
os.system(cmd)
