"""
Padronizar nomes de variáveis, classes e tabelas em inglês
Configurar scrollbar na tela hub
"""

from tkinter import *
from GUI.hub import HubScreen
from BACK.UserDb import UserDb
from tkinter import messagebox
from BACK.seed import implantDb

""" Tela principal da aplicação """
class MainScreen:
    def authenticateDb(self, usnm, passw):
        usbd = UserDb()
        us = (usnm, passw)
        result = usbd.authenticate(us)
        if(result):
            return True
        return False

    def authenticate(self) -> None:
            usnm = self.USER.get()
            passw = self.PASSWORD.get()
            try:    
                if(self.authenticateDb(usnm, passw)):
                    HubScreen()
                    self.WRONG.configure(text="")
                else:
                    self.WRONG.configure(text="acesso negado")
            except:
                messagebox.showwarning('Aviso', f'Antes de tudo configure o usuário do banco de dados no arquivo .env, se já houver configurado aperte o botão e inicie novamente.')
                implantDb()
                self.ROOT.destroy()

    def __init__(self) -> None:
        self.ROOT = Tk()
        self.ROOT.geometry("100x150")
        self.ROOT.title("Gerenciamento Zoologico")

        self.TITTLE = Label(self.ROOT, text="Zoo management")
        self.USER = Entry(self.ROOT)
        self.PASSWORD = Entry(self.ROOT)
        self.WRONG = Label(self.ROOT, text="")
        self.CONFIRM = Button(self.ROOT, text="log in")
        
        self.TITTLE.pack()
        self.USER.pack()
        self.PASSWORD.pack()
        self.WRONG.pack()
        self.CONFIRM.pack()

        self.CONFIRM.configure(command=self.authenticate)
        self.ROOT.mainloop()

MainScreen();