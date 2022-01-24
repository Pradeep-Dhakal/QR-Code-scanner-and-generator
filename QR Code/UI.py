#  dependencies
from random import *
from tkinter import *
from tkinter import font
from turtle import color, width
from PIL import Image, ImageTk
from matplotlib import colors
from numpy import size
from matplotlib.pyplot import title
import pyqrcode

# Files importing
# from Decode import *
# from generateWin import *
from Read1 import *


win = Tk()
win.geometry("420x500")
win.maxsize(width= 420, height= 500)
win.title("Qrcode Scanner: ")
win.iconbitmap("Reader\Qr.ico")


def DecodeFrame():
    win.destroy()
    import Decode


def generateQrCode():
    win.destroy()
    import generateWin

colors=["black", "red" , "green" , "blue"]

def lableanimation():
    
    fg = choice(colors)
    welcome_label.config(fg=fg)
    welcome_label.after(250, lableanimation)
    labels=["Welcom to QR code Genreator", "Scan Qr Code", "Generate Qr Code ", "Python Qr code "]
    text = choice(labels)
    welcome_label.config(text=text)


welcome_label = Label(font=('Times', '15', 'bold'))

welcome_label.place(x=40, y=20)
lableanimation()

Scan_Qr = Button(win, text="Scan by camera ", fg="Black", font=('Times', '11', 'bold'),
                 activebackground="green", activeforeground="white", height=2, width=13, command=ReadQrCode)
Scan_Qr.place(x=20, y=80)

Scan_cam_Qr = Button(win, text="Scan by upload", command=DecodeFrame, fg="Black", font=('Times', '11', 'bold'), activebackground="green", activeforeground="white", height=2, width=13
                     )
Scan_cam_Qr.place(x=150, y=80)

generate_Qr = Button(win, text="Generate QR", fg="Black", font=('Times', '11', 'bold'),
                     activebackground="green", activeforeground="white", height=2, width=12, command=generateQrCode)
generate_Qr.place(x=280, y=80)

photo=PhotoImage(file="Reader\Qricon.png")
photo_level=Label(image=photo)
photo_level.place(x=30,y=150)

win.mainloop()
