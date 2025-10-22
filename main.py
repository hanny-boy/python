from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("300x300")
window.title("Virus Detectar")
messagebox.showwarning("window name","Text to be displayed")
def msg():
    messagebox.showwarning("!ALERT!","!DON'T CLICK VIRUS FOUND!")
b = Button(window,text="SCAN FOR VIRUS",command=msg)
b.place(x=60,y=40)
window.mainloop()