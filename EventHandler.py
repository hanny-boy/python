from tkinter import *
window = Tk()
window.geometry("200x200")
window.title("Event Handler")
def handlekeypress(event):
    print(event.char)
window.bind("<Key>",handlekeypress)
def handleclick(event):
    print("The button was clicked!")
b = Button(text="Click ME!")
b.pack()
b.bind("<Button-1>",handleclick)
window.mainloop()