from tkinter import *
from BACK.CuidadorBanco import CuidadorBanco

class EditScreen:
    def __init__(self, crgvrSuper):
        ROOT = Tk();
        ROOT.geometry("100x150");

        crgvrBd = CuidadorBanco()

        LABEL = Text(ROOT, height=1)
        BUTTON = Button(ROOT)

        LABEL.pack()
        BUTTON.pack()

        a = crgvrBd.getUser(crgvrSuper)

        LABEL.insert(END, a[0])

        BUTTON.configure(command=lambda: print(LABEL.get("1.0", END)))

        #Algoritmo para conferir se os dados foram alterados: armazenar entradas em uma lista, fazer um for comparando com a lista retornada do postgre