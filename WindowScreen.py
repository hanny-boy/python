from tkinter import *
from datetime import date

window = Tk()
window.title("Window Screen")
window.geometry("400x300")

# Labels
lbl = Label(text="Heya :D", fg="white", bg="black", height=1, width=30)
name_lbl = Label(text="Full name:", bg="black", fg="white")

# Entry box
ne = Entry()


textbox = Text(height=4, width=40)


def display():
    name = ne.get()
    message = "Welcome to the application.\nToday's date is: "
    greet = "Hello " + name + "\n"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    textbox.insert(END, str(date.today()) + "\n")


btn = Button(text="Start", command=display, height=2, bg="black", fg="white")


lbl.pack()
name_lbl.pack()
ne.pack()
btn.pack()
textbox.pack()

window.mainloop()
