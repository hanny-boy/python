from tkinter import *
window = Tk()
window.geometry('250x300')
window.title("Number Pad")
f = Frame(master=window,width=200,height=250,bg="black")
nums = [[7,8,9],[4,5,6],[1,2,3],['*',0,'#']]
for i in range(4):
    window.rowconfigure(i,weight=1,minsize=50)
    window.columnconfigure(i,weight=1,minsize=75)
    for j in range(0,3):
        f = Frame(master=window,relief=SUNKEN,borderwidth=1)
        f.grid(row=i,column=j)
        l = Label(master=f,text=nums[i][j],bg='gray')
        l.pack(padx=3,pady=3)
window.mainloop()