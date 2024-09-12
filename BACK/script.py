from tkinter import StringVar
import tkinter
from tkinter import ttk
from .UsuarioBanco import UsuarioBanco

def authenticate():
    usbd = UsuarioBanco()
    usnmVar = StringVar()
    paswVar = StringVar()
    usnm = usnmVar.get()
    pasw = paswVar.get()
    us = (usnm, pasw)
    result = usbd.authenticate(us)
    return True


