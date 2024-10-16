from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco

class EditScreen:
    def updateTable(self, entryNm, entryId, oValues = [], bdcnct = CuidadorBanco()):
        nValues = [entryNm.get("1.0", END), entryId.get("1.0", END)]
        if(nValues!=oValues):
            nValues.append(oValues[1])
            bdcnct.update(nValues)

    def __init__(self, zkeeperSuper):
        ROOT = Tk();
        ROOT.geometry("100x150");

        ZKEEPER_BD = CuidadorBanco()
        ZKEEPER = ZKEEPER_BD.getUser(zkeeperSuper)

        NAME = Text(ROOT, height=1)
        ID = Text(ROOT, height=1)
        CONFIRM = Button(ROOT)

        NAME.pack()
        ID.pack()
        CONFIRM.pack()

        NAME.insert(END, ZKEEPER[0])
        ID.insert(END, ZKEEPER[1])

        CONFIRM.configure(command=lambda: self.updateTable(NAME, ID, ZKEEPER, ZKEEPER_BD))

        #Algoritmo para conferir se os dados foram alterados: armazenar entradas em uma lista, fazer um for comparando com a lista retornada do postgre