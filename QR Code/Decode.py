# Importing Dependencies
from base64 import decode
from distutils.command.build import build
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os
from pyzbar.pyzbar import decode
# from generateWin import *
# from UI import *


def gomainwin():
    decodewin.destroy()
    import UI

def showImage():
    # it will teak image name with full path
    filenames = filedialog.askopenfilename(initialdir=os.getcwd(), title="Seletc Image", filetypes=(
        ("JPG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
    img = Image.open(filenames)  # it will open image
    img.thumbnail((350, 350))  # Resizing the image in thumbnail size
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img
    data = decode(Image.open(filenames))
    showqrmessage.configure(text=data[0].data.decode("ascii"))
    print(data[0].data.decode("ascii"))
decodewin = Tk()
decodewin.geometry("400x400")
decodewin.iconbitmap("Reader\Qr.ico")

showqrmessage = Label(decodewin,text="", )
showqrmessage.place(x=10, y=350)
lbl = Label(decodewin)
lbl.place(x=5, y=5)
uploadbtn = Button(decodewin, text="Upload Image", command=showImage,fg="Black", font=('Times', '10', 'bold'), activebackground="green", activeforeground="white", height=2, width=11)
uploadbtn.place(x=20, y=300)
Back=Button(decodewin,text="back", command=gomainwin,fg="Black", font=('Times', '10', 'bold'), activebackground="green", activeforeground="white", height=2, width=11)
Back.place(x=150,y=300)
mainloop()