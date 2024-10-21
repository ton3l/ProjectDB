from .EnclosureDb import EnclosureDb
from .KeeperDb import KeeperDb
from .UserDb import UserDb
from tkinter import messagebox

def implantDb():
    messagebox.showinfo('Aviso', 'O programa irá configurar tabelas de banco de dados com valores padrão')
    UserDb().createTable()
    UserDb().insertInto(["default", "user"])
    KeeperDb().createTable()
    KeeperDb().insertInto(["Daniel Enos", "123456"])
    KeeperDb().insertInto(["Galba Falcao", "abcdef"])