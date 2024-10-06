from tkinter import StringVar
import tkinter
from tkinter import ttk
from .UsuarioBanco import UsuarioBanco

def authenticate(usnm, passw):
    usbd = UsuarioBanco()
    us = (usnm, passw)
    result = usbd.authenticate(us)
    return True


