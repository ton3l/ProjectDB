from tkinter import *
from BACK.Usuario import Usuario
from BACK.UsuarioBanco import UsuarioBanco
from BACK import script

""" Tela principal da aplicação """


root = Tk();
root.geometry("400x400");

tittle = Label(root, text="Login");
user = Entry(root);
password = Entry(root);
confirm = Button(root, text="log in");

def authenticate():
    usnm = user.get();
    passw = password.get()

    if(script.authenticate(usnm, passw)):
        print('acesso concedido')

confirm.configure(command=authenticate)

tittle.grid(column=0, row=0);
user.grid(column=0,row=1,pady=2.5,padx=2.5);
password.grid(column=0,row=2,pady=2.5,padx=2.5);
confirm.grid(column=0,row=3,pady=2.5,padx=2.5);

root.mainloop();

