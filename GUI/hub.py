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

    def refreshList(self, ROOT, labels = [], buttons = []):
        if(labels and buttons):
            for i in range(len(labels)):
                labels[i].destroy()
                buttons[i].destroy()
            labels.clear()
            buttons.clear()
            
        zkeeperBd = CuidadorBanco()
        zkeepers = zkeeperBd.selectAll()
        for n,zkeeper in enumerate(zkeepers): #Dispõe os cuidadores encontrados na tela acompanhados de um botão para cada
            labels.append(Label(ROOT, text=zkeeper[0]))
            labels[n].grid(row=n+1, column=0)
            buttons.append(Button(ROOT, text="ver cuidador", height=1, command=partial(self.linkEditScreen, zkeeper[1], lambda: self.refreshList(ROOT))))
            buttons[n].grid(row=n+1, column=2)


    def __init__(self):
        ROOT = Tk()
        ROOT.geometry("212x212")

        CREATE = Button(ROOT, text="Inserir Cuidador", height=1, command=lambda: self.linkCreateScreen(lambda: self.refreshList(ROOT)))
        SCROLL = Scrollbar(ROOT)
        nameLabels = []
        editButtons = []
        
        CREATE.grid(row=0, column=1)

        self.refreshList(ROOT, nameLabels, editButtons)