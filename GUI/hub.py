from tkinter import *
from .CUD import CUDScreen
from .R import ReadScreen

class HubScreen:
    def linkCreateScreen(self):
        CUDScreen();
    
    def linkReadScreen(self):
        ReadScreen()

    def __init__(self):
        ROOT = Tk();
        ROOT.geometry("100x150");

        CREATEEDIT = Button(ROOT, text="Criar/Editar Cuidador");
        READ = Button(ROOT, text="Lista cuidadores");

        CREATEEDIT.grid(column=0, row=0, pady=2.5, padx=2.5);
        READ.grid(column=0, row=1, pady=2.5, padx=2.5);

        CREATEEDIT.configure(command=self.linkCreateScreen);
        READ.configure(command=self.linkReadScreen);

    

