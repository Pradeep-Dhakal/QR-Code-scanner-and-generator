from tkinter import *
import pyqrcode  # Imported pyqrcode Module

# from Decode import *
# from generateWin import *
# from Read1 import *

def gotomain():
    genwin.destroy()
    import UI
    

genwin = Tk()
genwin.title("Geenerate Qr code ")
genwin.geometry("400x400")
genwin.iconbitmap("Qr.ico")
def generate():
    data = url.get()  # Declaring the Variables
    image = pyqrcode.create(data)  # Creating a Function
    image.png("QrCode.jpg", scale=8)  # Saving the Image
url = StringVar()
urlEntry = Label(genwin, text="Enter your Message URL: ", fg="Black",font=('Times', '11', 'bold'))
urlEntry.place(x=100, y=30)
URl = Entry(genwin, width=50, textvariable=url,font=('Times', '8'), insertborderwidth=10, selectbackground="green") 
URl.place(x=20, y=90)
generate_now = Button(genwin, text="Generate now", command= generate, fg="Black", font=('Times', '11', 'bold'), activebackground="green", activeforeground="white", height=2, width=11)
generate_now.place(x=20, y=150)
Back=Button(genwin,text="Back", command=gotomain,fg="Black", font=('Times', '11', 'bold'), activebackground="green", activeforeground="white", height=2, width=11)
Back.place(x=140,y=150)
photo=PhotoImage(file="Reader\Qricon.png")
photo_level=Label(image=photo)
photo_level.place(x=30,y=200)
mainloop() 
