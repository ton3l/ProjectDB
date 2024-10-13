from tkinter import *

class EditScreen:
    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("100x150");

        LABEL = Label(ROOT, bg="blue")

        LABEL.pack()

        LABEL.configure(text="AAAAAAAAAAAAAAAAA")