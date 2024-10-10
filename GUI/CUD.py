from tkinter import *
from BACK.UsuarioBanco import UsuarioBanco

class CUDScreen:
    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("200x350");

        SCROLL = Scrollbar(ROOT);
        
        SCROLL.pack(side=RIGHT, fill=Y)

        usbd = UsuarioBanco()
        users = usbd.selectAll()
        text = []
        for user in users:
            text.append(Text(ROOT, height=1))

        for n,user in enumerate(users):
            text[n].insert(END, user[0])
            text[n].pack()
            BUTTON = Button(ROOT, text="edit", height=1)
            BUTTON.pack(side=TOP)


