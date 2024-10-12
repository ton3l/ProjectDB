from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco

class HubScreen:
    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("200x350");

        CREATE = Button(ROOT, text="Inserir Cuidador", height=1)
        SCROLL = Scrollbar(ROOT);
        
        CREATE.grid(row=0, column=1)

        cddr = CuidadorBanco()
        users = cddr.selectAll()
        text = []

        for n,user in enumerate(users):
            text.append(Label(ROOT, text=user[0]))
            text[n].grid(row=n+1, column=0)
            BUTTON = Button(ROOT, text="ver cuidador", height=1)
            BUTTON.grid(row=n+1, column=2)