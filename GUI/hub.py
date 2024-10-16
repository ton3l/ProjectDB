from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco
from .C import CreateScreen
from .RUD import EditScreen
from functools import partial

class HubScreen:
    def linkCreateScreen(self, refreshList):
        CreateScreen(refreshList) #Passa a função de atualizar lista por parâmetro
    def linkEditScreen(self, zkeeperId, refreshList):
        EditScreen(zkeeperId, refreshList)

    def refreshList(self, ROOT):
        zkeeperBd = CuidadorBanco()
        zkeepers = zkeeperBd.selectAll()
        nameLabels = [] 
        editButtons = []

        for n,zkeeper in enumerate(zkeepers): #Dispõe os cuidadores encontrados na tela acompanhados de um botão para cada
            nameLabels.append(Label(ROOT, text=zkeeper[0]))
            nameLabels[n].grid(row=n+1, column=0)
            editButtons.append(Button(ROOT, text="ver cuidador", height=1, command=partial(self.linkEditScreen, zkeeper[1], lambda: self.refreshList(ROOT))))
            editButtons[n].grid(row=n+1, column=2)


    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("212x212");

        CREATE = Button(ROOT, text="Inserir Cuidador", height=1, command=lambda: self.linkCreateScreen(lambda: self.refreshList(ROOT)))
        SCROLL = Scrollbar(ROOT);
        
        CREATE.grid(row=0, column=1)

        self.refreshList(ROOT)