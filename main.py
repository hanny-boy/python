from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename

window = Tk()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0,mainsize=800,weight=1)
window.columnconfigure(0,mainsize=800,weight=1)

def open_file():
   filepath = askopenfilename(filetypes=[("Text Files",".*.txt"),("All Files",".*.")])
   if not filepath:
      return
   textedit.delete(1.0,END)
   with open(filepath,"r") as input_file:
      text = input_file.read()
      textedit.insert(END,text)
      input_file.close()
   window.title(f"text editor"-{filepath})
def savefile():
   filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files","*.txt")])
   if not filepath:
      return
   with open(filepath,"w") as output_file:
      text = textedit.get(1.0,END)
      output_file.write(text)

   window.title(f"text editor"-{filepath})
textedit = Text(window)
frbuttons = Frame(window,relief=RAISED,bd = 2)
btn_open = Button(frbuttons,text="open",command=open_file)