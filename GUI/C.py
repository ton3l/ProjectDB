from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco

class CreateScreen:
    def insertCuidador(self, bdcnct, name, id, label, refreshList):
        values = [name, id]#Recebendo valores e inserindo no banco de dados, através de uma instância de Cuidador Banco(bdcnct)
        bdcnct.insertInto(values)

        label.configure(text="Cuidador criado")
        refreshList()

    def __init__(self, refreshSuperList):
        ROOT = Tk()
        ROOT.geometry("100x150")
        
        zkeeperBd = CuidadorBanco()

        NAME_L = Label(ROOT, text="Nome:")
        NAME = Entry(ROOT)
        ID_L = Label(ROOT, text="Id:")
        ID = Entry(ROOT)
        CONFIRM = Button(ROOT, text="Confirmar")
        CONFIRM_L = Label(ROOT)

        NAME_L.pack()
        NAME.pack()
        ID_L.pack()
        ID.pack()
        CONFIRM.pack()
        CONFIRM_L.pack()

        CONFIRM.configure(command=lambda: self.insertCuidador(zkeeperBd, NAME.get(), ID.get(), CONFIRM_L, refreshSuperList))

