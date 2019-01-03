from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('500x500')
root.title("Registration Form")

Fullname=StringVar()
Email=StringVar()
def database():
   try:
       name1=Fullname.get()
   except:
        messagebox.showerror(
                "Input NOT valid.",
                "Please try again and enter a valid input."
            )
   try:
        email=Email.get()
   except:
        messagebox.showerror(
                "Input NOT valid.",
                "Please try again and enter a valid input."
            )


   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('INSERT INTO Cam_Sec (FullName,Email) VALUES(?,?)',(name1,email,))
   conn.commit()
   root.destroy()
   exec_code=call("python3 launch_window.py")

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="Full Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)


Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=300)

root.mainloop()
