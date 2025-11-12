import tkinter as tk
from tkinter import ttk, messagebox
class RestrauntManagmentSystem:
    def  __init__(self,root):
        self.root = root
        self.root.title("Restraunt Managment")
        self.menu_items = {"Steak":67,"Fries":41,"Burger":21,"Pizza":31,"Non Alcoholic Drinks":10}
        self.exchangerate = 50
        frame = ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Restraunt Managment",font=("Cavet",20,"Bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menu_labels = {}
        self.menu_quantites = {}
        for i,(item,price) in eneomerate(self.menu_items.items(),start = 1):
            label = ttk.Label(frame,text="{Item}($){Price}:",font=("Cavet",15))