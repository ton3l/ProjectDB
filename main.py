from tkinter import *
from BACK import script
from GUI.hub import HubScreen

""" Tela principal da aplicação """
ROOT = Tk();
ROOT.geometry("100x150");

TITTLE = Label(ROOT, text="Zoo management");
USER = Entry(ROOT);
PASSWORD = Entry(ROOT);
WRONG = Label(ROOT, text="");
CONFIRM = Button(ROOT, text="log in");

TITTLE.grid(column=0, row=0);
USER.grid(column=0,row=1,pady=2.5,padx=2.5);
PASSWORD.grid(column=0,row=2,pady=2.5,padx=2.5);
WRONG.grid(column=0,row=3);
CONFIRM.grid(column=0,row=4,pady=2.5,padx=2.5);

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