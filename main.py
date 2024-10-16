"""
Padronizar nomes de variáveis, classes e tabelas em inglês
Extinguir uso de ;
Uso de classe para inicialização da tela principal
Configurar scrollbar na tela hub
Fazer try catch para criar tabelas e gerenciar erros
trocar caregiver(zkeeper) para zookeeper(zkeeper)

"""

from tkinter import *
from BACK import script
from GUI.hub import HubScreen

""" Tela principal da aplicação """
ROOT = Tk();
ROOT.geometry("100x150");
ROOT.title("Gerenciamento Zoologico")

TITTLE = Label(ROOT, text="Zoo management");
USER = Entry(ROOT);
PASSWORD = Entry(ROOT);
WRONG = Label(ROOT, text="");
CONFIRM = Button(ROOT, text="log in");

TITTLE.pack()
USER.pack()
PASSWORD.pack()
WRONG.pack()
CONFIRM.pack()

def authenticate():
    usnm = USER.get();
    passw = PASSWORD.get()

    if(script.authenticate(usnm, passw)):
        HubScreen();
        WRONG.configure(text="");
    else:
        WRONG.configure(text="acesso negado");

CONFIRM.configure(command=authenticate);

ROOT.mainloop();