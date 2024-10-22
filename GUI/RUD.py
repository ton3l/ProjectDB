from tkinter import *
from BACK.KeeperDb import KeeperDb
from BACK.EnclosureDb import EnclosureDb

class EditScreen:
    def deleteRow(self):
        self.ENV_BD.deleteRow([self.ZKEEPER[1]])
        self.ZKEEPER_BD.deleteRow([self.ZKEEPER[1]])
        self.refreshList()
        self.ROOT.destroy()

    def updateTableEnv(self):
        newSpcs = self.SPECIES_E.get()
        newBiome = self.BIOME_E.get()
        newQuant = self.QUANT_E.get()
        nValues = [newSpcs, newBiome, newQuant]
        if(nValues!=self.ENV):
            nValues.append(self.ENV[4])#Adiciono o id antigo a lista de novos valores para facilitar o processo de atualização;
            self.ENV_BD.update(nValues)

    def updateTableKeeper(self):
        newNm = self.NAME_E.get()
        newId = self.ID_E.get()
        nValues = [newNm, newId]
        if(nValues!=self.ZKEEPER):
            nValues.append(self.ZKEEPER[1])#Adiciono o id antigo a lista de novos valores para facilitar o processo de atualização;
            self.ZKEEPER_BD.update(nValues)
            self.refreshList()
            self.updateTableEnv()
            self.ROOT.destroy()

    def __init__(self, zkeeperSuper, refreshList):
        self.ROOT = Tk()
        self.ROOT.geometry("250x300")

        self.refreshList = refreshList
        self.ZKEEPER_BD = KeeperDb()
        self.ENV_BD = EnclosureDb()
        self.ZKEEPER = self.ZKEEPER_BD.getUser(zkeeperSuper)
        self.ENV = self.ENV_BD.getEnvironment(self.ZKEEPER[1])

        self.NAME_L = Label(self.ROOT, text="Nome:")
        self.NAME_E = Entry(self.ROOT)
        self.ID_L = Label(self.ROOT, text="Id:")
        self.ID_E = Entry(self.ROOT)
        self.DIVISOR = Label(self.ROOT, text="Informações do ambiente que trabalha", pady=2)
        self.SPECIES_L = Label(self.ROOT, text="Espécie:")
        self.SPECIES_E = Entry(self.ROOT)
        self.BIOME_L = Label(self.ROOT, text="Bioma:")
        self.BIOME_E = Entry(self.ROOT)
        self.QUANT_L = Label(self.ROOT, text="Quantidade:")
        self.QUANT_E = Entry(self.ROOT)
        self.CONFIRM = Button(self.ROOT, text="Confirmar")
        self.DELETE = Button(self.ROOT, text="Deletar cuidador")

        self.NAME_L.pack()
        self.NAME_E.pack()
        self.ID_L.pack()
        self.ID_E.pack()
        self.DIVISOR.pack()
        self.SPECIES_L.pack()
        self.SPECIES_E.pack()
        self.BIOME_L.pack()
        self.BIOME_E.pack()
        self.QUANT_L.pack()
        self.QUANT_E.pack()
        self.CONFIRM.pack()
        self.DELETE.pack()

        self.NAME_E.insert(END, self.ZKEEPER[0])
        self.ID_E.insert(END, self.ZKEEPER[1])
        self.SPECIES_E.insert(END, self.ENV[1])
        self.BIOME_E.insert(END, self.ENV[2])
        self.QUANT_E.insert(END, self.ENV[3])

        self.CONFIRM.configure(command=self.updateTableKeeper)
        self.DELETE.configure(command=self.deleteRow)

        #Algoritmo para conferir se os dados foram alterados: armazenar entradas em uma lista, fazer um for comparando com a lista retornada do postgre