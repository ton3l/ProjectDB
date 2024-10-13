from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco
from .C import CreateScreen
from .RUD import EditScreen

class HubScreen:
    def linkCreateScreen(self, refreshList):
        CreateScreen(refreshList)
    def linkEditScreen(self):
        EditScreen()
    def refreshList(self, ROOT):
        cddr = CuidadorBanco()
        users = cddr.selectAll()
        text = []
        for n,user in enumerate(users):
            text.append(Label(ROOT, text=user[0]))
            text[n].grid(row=n+1, column=0)
            BUTTON = Button(ROOT, text="ver cuidador", height=1, command=self.linkEditScreen)
            BUTTON.grid(row=n+1, column=2)


    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("212x212");

        CREATE = Button(ROOT, text="Inserir Cuidador", height=1, command=lambda: self.linkCreateScreen(lambda: self.refreshList(ROOT)))
        SCROLL = Scrollbar(ROOT);
        
        CREATE.grid(row=0, column=1)

        self.refreshList(ROOT)