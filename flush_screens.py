import os,datetime
def delete():
    textfile=open("/home/abhijit/atom_projects/time.txt","r")
    now_time_str=textfile.read()

    textfile.close()
    now_date=datetime.datetime.now().date().strftime ("%d-%m-%y")
    now_date_str=str(now_date)
    textfile=open("/home/abhijit/atom_projects/count_screen.txt","r")
    limit=textfile.read()
    i=0
    name_screen="/home/abhijit/atom_projects/screen-"+now_date_str+"-"+now_time_str
    t=int(limit)
    while i<t:
        j=str(i)
        img_name=name_screen+"/screen"+j+".jpg"
        #imk=Image.open(img_name)
        #imk.load()
        #imk.show()
        i=i+1
        os.remove(img_name)
