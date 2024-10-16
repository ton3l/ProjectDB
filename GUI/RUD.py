from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco

class EditScreen:
    def updateTable(self, entryNm, entryId, oValues = [], bdcnct = CuidadorBanco(), refreshList = 0):
        nNm = entryNm.get()
        nId = entryId.get()
        nValues = [nNm, nId]
        if(nValues!=oValues):
            nValues.append(oValues[1])
            bdcnct.update(nValues)
            refreshList()

    def __init__(self, zkeeperSuper, refreshList):
        ROOT = Tk();
        ROOT.geometry("100x150");

        ZKEEPER_BD = CuidadorBanco()
        ZKEEPER = ZKEEPER_BD.getUser(zkeeperSuper)

        NAME = Entry(ROOT)
        ID = Entry(ROOT)
        CONFIRM = Button(ROOT)

        NAME.pack()
        ID.pack()
        CONFIRM.pack()

        NAME.insert(END, ZKEEPER[0])
        ID.insert(END, ZKEEPER[1])

        CONFIRM.configure(command=lambda: self.updateTable(NAME, ID, ZKEEPER, ZKEEPER_BD, refreshList = refreshList))

        #Algoritmo para conferir se os dados foram alterados: armazenar entradas em uma lista, fazer um for comparando com a lista retornada do postgre