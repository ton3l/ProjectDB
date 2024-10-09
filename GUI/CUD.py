from tkinter import *
from BACK.UsuarioBanco import UsuarioBanco

class CUDScreen:
    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("200x350");

        SCROLL = Scrollbar(ROOT);
        LB = Listbox(ROOT, yscrollcommand=SCROLL.set, font=('Arial', ), width=10);

        SCROLL.pack(side=RIGHT, fill=Y)
        LB.pack(side=LEFT, fill=Y)
        


        usbd = UsuarioBanco()
        users = usbd.selectAll()

        for user in users:
            LB.insert(END, user[0])
            BUTTON = Button(ROOT, text="edit", height=1)
            BUTTON.pack(side=TOP)

        SCROLL.configure(command=LB.yview)

