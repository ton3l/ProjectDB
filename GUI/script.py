from tkinter import *
from tkinter import ttk
from Back.UsuarioBanco import UsuarioBanco

def authenticate():
    usbd = UsuarioBanco()
    usnmVar = StringVar()
    paswVar = StringVar()
    usnm = usnmVar.get()
    pasw = paswVar.get()
    us = (usnm, pasw)
    result = usbd.authenticate(us)
    return True


