from tkinter import *
from BACK.KeeperDb import KeeperDb
from .C import CreateScreen
from .RUD import EditScreen
from functools import partial

class HubScreen:
    def linkCreateScreen(self, refreshList):
        CreateScreen(refreshList) #Passa a função de atualizar lista por parâmetro
    def linkEditScreen(self, zkeeperId, refreshList):
        EditScreen(zkeeperId, refreshList)

    def refreshList(self):
        if(self.nameLabels and self.editButtons):
            for i in range(len(self.nameLabels)):
                self.nameLabels[i].destroy()
                self.editButtons[i].destroy()
            self.nameLabels.clear()
            self.editButtons.clear()
            
        zkeeperBd = KeeperDb()
        zkeepers = zkeeperBd.selectAll()

        for n,zkeeper in enumerate(zkeepers): #Dispõe os cuidadores encontrados na tela acompanhados de um botão para cada
            self.nameLabels.append(Label(self.CANVAS, text=zkeeper[0]))
            self.nameLabels[n].grid(row=n+1, column=0)
            self.editButtons.append(Button(self.CANVAS, text="ver cuidador", height=1, command=partial(self.linkEditScreen, zkeeper[1], lambda: self.refreshList())))
            self.editButtons[n].grid(row=n+1, column=2)


    def __init__(self):
        self.ROOT = Tk()
        self.ROOT.geometry("300x300")

        self.CANVAS = Canvas(self.ROOT)

        self.CREATE = Button(self.CANVAS, text="Inserir Cuidador", height=1, command=lambda: self.linkCreateScreen(lambda: self.refreshList()))
        self.SCROLL = Scrollbar(self.ROOT, orient=VERTICAL, command=self.CANVAS.yview)
        self.nameLabels = []
        self.editButtons = []
        
        self.CREATE.grid(row=0, column=1)
        self.SCROLL.pack(side=RIGHT, fill=Y)
        self.CANVAS.pack()

        self.CANVAS.configure(yscrollcommand=self.SCROLL.set)

        self.refreshList()