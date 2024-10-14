from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco
from .C import CreateScreen
from .RUD import EditScreen
from functools import partial

class HubScreen:
    def linkCreateScreen(self, refreshList):
        CreateScreen(refreshList) #Passa a função de atualizar lista por parâmetro
    def linkEditScreen(self, crgvrId):
        EditScreen(crgvrId)

    def refreshList(self, ROOT):
        cddrBd = CuidadorBanco()
        crgvrs = cddrBd.selectAll()
        nameLabels = [] 
        editButtons = []

        for n,crgvr in enumerate(crgvrs): #Dispõe os cuidadores encontrados na tela acompanhados de um botão para cada
            nameLabels.append(Label(ROOT, text=crgvr[0]))
            nameLabels[n].grid(row=n+1, column=0)
            editButtons.append(Button(ROOT, text="ver cuidador", height=1, command=partial(self.linkEditScreen, crgvr[1])))
            editButtons[n].grid(row=n+1, column=2)


    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("212x212");

        CREATE = Button(ROOT, text="Inserir Cuidador", height=1, command=lambda: self.linkCreateScreen(lambda: self.refreshList(ROOT)))
        SCROLL = Scrollbar(ROOT);
        
        CREATE.grid(row=0, column=1)

        self.refreshList(ROOT)