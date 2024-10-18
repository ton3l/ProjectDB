from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco

class EditScreen:
    def updateTable(self, entryNm, entryId, oValues = [], bdcnct = CuidadorBanco(), root = 0, refreshList = 0):
        nNm = entryNm.get()
        nId = entryId.get()
        nValues = [nNm, nId]
        if(nValues!=oValues):
            nValues.append(oValues[1])
            bdcnct.update(nValues)
            refreshList()
            root.destroy()

    def __init__(self, zkeeperSuper, refreshList):
        ROOT = Tk()
        ROOT.geometry("250x300")

        ZKEEPER_BD = CuidadorBanco()
        ZKEEPER = ZKEEPER_BD.getUser(zkeeperSuper)

        NAME_L = Label(ROOT, text="Nome:")
        NAME_E = Entry(ROOT)
        ID_L = Label(ROOT, text="Id:")
        ID_E = Entry(ROOT)
        DIVISOR = Label(ROOT, text="Informações do ambiente que trabalha", pady=2)
        SPECIES_L = Label(ROOT, text="Espécie:")
        SPECIES_E = Entry(ROOT)
        BIOME_L = Label(ROOT, text="Bioma:")
        BIOME_E = Entry(ROOT)
        QUANT_L = Label(ROOT, text="Quantidade:")
        QUANT_E = Entry(ROOT)
        CONFIRM = Button(ROOT, text="Confirmar")


        NAME_L.pack()
        NAME_E.pack()
        ID_L.pack()
        ID_E.pack()
        DIVISOR.pack()
        SPECIES_L.pack()
        SPECIES_E.pack()
        BIOME_L.pack()
        BIOME_E.pack()
        QUANT_L.pack()
        QUANT_E.pack()
        CONFIRM.pack()
        

        NAME_E.insert(END, ZKEEPER[0])
        ID_E.insert(END, ZKEEPER[1])

        CONFIRM.configure(command=lambda: self.updateTable(NAME_E, ID_E, ZKEEPER, ZKEEPER_BD, ROOT, refreshList = refreshList))

        #Algoritmo para conferir se os dados foram alterados: armazenar entradas em uma lista, fazer um for comparando com a lista retornada do postgre