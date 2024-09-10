from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
from mysql.connector import Error
from PIL import Image, ImageTk

root=Tk()
root.geometry("1400x1400")
root.title("CATALOGUE")
image = Image.open("rr4.jpg")
tk_image = ImageTk.PhotoImage(image)
label = Label(root, image=tk_image)
label.pack()

def Exit():
    result=tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

m1=Label(root, text="CATALOGUE",bg="#383733",fg="Red",font=("arial 28 bold")).place(x=600,y=25)
b1=Label(root, text="INDIAN",font="arial 20 bold",bg="#383733").place(x=100,y=100)
IN1=Label(root, text="TATA").place(x=100,y=150)
IN2=Label(root, text="MAHINDRA").place(x=100,y=200)
b2=Label(root, text="GERMAN",font="arial 20 bold", bg="#383733").place(x=300,y=100)
g1=Label(root, text="MERCEDES").place(x=300,y=150)
g2=Label(root, text="VOLKSWAGEN").place(x=300,y=200)
g3=Label(root, text="SKODA").place(x=300,y=250)
g4=Label(root, text="AUDI").place(x=300,y=300)
g5=Label(root, text="BMW").place(x=300,y=350)
g6=Label(root, text="PORSCHE").place(x=300,y=400)
b3=Label(root, text="ITALIAN",font="arial 20 bold",bg="#383733").place(x=500,y=100)
IT1=Label(root, text="FIAT").place(x=500,y=150)
IT2=Label(root, text="LAMBORGHINI").place(x=500,y=200)
IT3=Label(root, text="FERRARI").place(x=500,y=250)
IT4=Label(root, text="MASARATI").place(x=500,y=300)
It5=Label(root, text="PAGANI").place(x=500,y=350)
b4=Label(root, text="KOREAN",font="arial 20 bold",bg="#383733").place(x=700,y=100)
k1=Label(root, text="HYUNDAI").place(x=700,y=150)
k2=Label(root, text="KIA").place(x=700,y=200)
k3=Label(root, text="RENAULT").place(x=700,y=250)
b5=Label(root, text="US",font="arial 20 bold",bg="#383733").place(x=900,y=100)
u1=Label(root, text="JEEP").place(x=900,y=150)
u2=Label(root, text="RAM").place(x=900,y=200)
u3=Label(root, text="CHEVY").place(x=900,y=250)
u4=Label(root, text="TESLA").place(x=900,y=300)
u5=Label(root, text="DODGE").place(x=900,y=350)
u6=Label(root, text="GMC").place(x=900,y=400)
u7=Label(root, text="CADILLAC").place(x=900,y=450)
u8=Label(root, text="FORD").place(x=900,y=500)
b6=Label(root, text="JAPAN",font="arial 20 bold",bg="#383733").place(x=1100,y=100)
j1=Label(root, text="HONDA").place(x=1100,y=150)
j2=Label(root, text="TOYOTO").place(x=1100,y=200)
j3=Label(root, text="MITSUBISHI").place(x=1100,y=250)
j4=Label(root, text="MARUTI SUZUKI").place(x=1100,y=300)
j5=Label(root, text="NISSAN").place(x=1100,y=350)

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=Exit)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

root.mainloop()
