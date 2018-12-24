import os
textfile=open("count_scr.txt","r")
limit=textfile.read()
i=0
t=int(limit)
while i<t:
    j=str(i)
    img_name="frame"+j+".jpg"
    imk=Image.open(img_name)
    imk.load()
    imk.show()
    i=i+1
    os.remove(img_name)
