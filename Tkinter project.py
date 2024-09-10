from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk

base = Tk()  
base.geometry("1400x1400")  
base.title("APDM MULTI-BRAND MOTOR SPORTS")  
image = Image.open("rr2.jpg")

# Convert Image object to Tkinter PhotoImage object
tk_image = ImageTk.PhotoImage(image)

# Create a Tkinter label with the image
label = Label(base, image=tk_image)
label.pack()


NAME = StringVar()
EMAIL = StringVar()
CONTACT_NO = StringVar()
SEGMENT = StringVar()
FUEL_TYPE = StringVar()
BRAND = StringVar()
ADDRESS = StringVar()

def Database():
    global conn,cursor
    conn = mysql.connector.connect(host="localhost",user="root",passwd="0511",database="registration",auth_plugin="mysql_native_password")
    cursor = conn.cursor()
  
   
def Exit():
    result=tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        base.destroy()
        exit()

def Registration():
    Database()
    if NAME.get() == "" or EMAIL.get() == "" or CONTACT_NO.get() == "" or SEGMENT.get() == "" or FUEL_TYPE.get() == "" or BRAND.get() == "" or ADDRESS.get() == "":
        tkMessageBox.showerror("Error", "All fields are required")

    else:
            cursor.execute("INSERT INTO `persons` (name, email, contact_no, segment, fuel_type, brand, address) VALUES(%s, %s, %s, %s, %s, %s, %s)", (str(NAME.get()), str(EMAIL.get()), str(CONTACT_NO.get()), str(SEGMENT.get()), str(FUEL_TYPE.get()), str(BRAND.get()), str(ADDRESS.get())))
            conn.commit()
            NAME.set("")
            EMAIL.set("")
            CONTACT_NO.set("")
            SEGMENT.set("")
            FUEL_TYPE.set("")
            BRAND.set("")
            ADDRESS.set("")
        
                
            cursor.close()
            conn.close()
            tkMessageBox.showinfo("Information","registration successful")

def next():
   base.destroy()
   import catalogue            
    
Welcome1=Label(base, text="WELCOME  TO  APDM  MOTOR  SPORTS",font=("arial",26), fg="Red", bg="#969593").place(x=375,y=50)
Welcome2=Label(base, text="MULTI-BRAND SHOWROOM",font=("arial",20), fg="blue", bg="#969593").place(x=520,y=100)

lb1= Label(base, text="NAME", width=10, font=("arial",12)).place(x=500, y=200)  
en1= Entry(base, textvariable=NAME).place(x=750, y=200)  
  
lb2= Label(base, text="EMAIL", width=10, font=("arial",12)).place(x=500, y=250)  
en2= Entry(base, textvariable=EMAIL).place(x=750, y=250)  
  
lb3= Label(base, text="CONTACT NO", width=13,font=("arial",12)).place(x=500, y=300)  
en3= Entry(base, textvariable=CONTACT_NO).place(x=750, y=300)  
  
lb4= Label(base, text="SEGMENT", width=15, font=("arial",12)).place(x=500, y=350)  
en4= Entry(base, textvariable=SEGMENT).place(x=750,y=350)

lb5= Label(base, text="FUEL TYPE", width=13,font=("arial",12)).place(x=500,y=400)  
en5= Entry(base, textvariable=FUEL_TYPE).place(x=750,y=400)
  
lb6= Label(base, text="BRAND", width=13,font=("arial",12)).place(x=500, y=450)  
en6= Entry(base, textvariable=BRAND).place(x=750, y=450)  
  
lb7= Label(base, text="ADDRESS", width=15,font=("arial",12)).place(x=500, y=500)  
en7 =Entry(base, textvariable=ADDRESS).place(x=750, y=500)  

  
Button(base, text="REGISTER", font=("arial",15), width=20, bd=5, command=Registration).place(x=600,y=550)  
Button(base, text="Next",font=("arial",15), width=20, bd=5,command=next).place(x=600,y=600)
menubar = Menu(base)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
base.config(menu=menubar)


def next():
   base.destroy()
   import catalogue
   
base.mainloop()  
