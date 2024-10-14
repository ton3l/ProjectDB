from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco

class EditScreen:
    def updateTable(self, nValues = [], oValues = []):
        if(nValues!=oValues):
            


    def __init__(self, crgvrSuper):
        ROOT = Tk();
        ROOT.geometry("100x150");

        ZKEEPER_BD = CuidadorBanco()
        ZKEEPER = ZKEEPER_BD.getUser(crgvrSuper)

        NAME = Text(ROOT, height=1)
        ID = Text(ROOT, height=1)
        CONFIRM = Button(ROOT)

        NAME.pack()
        ID.pack()
        CONFIRM.pack()

        NAME.insert(END, ZKEEPER[0])
        ID.insert(END, ZKEEPER[1])

        CONFIRM.configure(command=lambda: print(NAME.get("1.0", END)))

        #Algoritmo para conferir se os dados foram alterados: armazenar entradas em uma lista, fazer um for comparando com a lista retornada do postgre