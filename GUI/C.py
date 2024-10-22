from tkinter import *
from BACK.KeeperDb import KeeperDb
from BACK.EnclosureDb import EnclosureDb

class CreateScreen:
    def insertCuidador(self):
        values = [self.NAME.get(), self.ID.get()]#Recebendo valores e inserindo no banco de dados, através de uma instância de Cuidador Banco(self.zkeeperBd)
        self.zkeeperBd.insertInto(values)
        self.EnclosureDb.insertInto(["", "", 0, values[1]])
        self.CONFIRM_L.configure(text="Cuidador criado")
        self.refresh()

    def __init__(self, refreshSuperList):
        self.ROOT = Tk()
        self.ROOT.geometry("100x150")
        
        self.refresh = refreshSuperList
        self.zkeeperBd = KeeperDb()
        self.EnclosureDb = EnclosureDb()

        self.NAME_L = Label(self.ROOT, text="Nome:")
        self.NAME = Entry(self.ROOT)
        self.ID_L = Label(self.ROOT, text="Id:")
        self.ID = Entry(self.ROOT)
        self.CONFIRM = Button(self.ROOT, text="Confirmar")
        self.CONFIRM_L = Label(self.ROOT)

        self.NAME_L.pack()
        self.NAME.pack()
        self.ID_L.pack()
        self.ID.pack()
        self.CONFIRM.pack()
        self.CONFIRM_L.pack()

        self.CONFIRM.configure(command=lambda: self.insertCuidador())

