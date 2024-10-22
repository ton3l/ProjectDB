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
    KeeperDb().insertInto(["Marçal", "abc123"])
    KeeperDb().insertInto(["Fábio", "123abc"])
    KeeperDb().insertInto(["Thadeu", "456def"])
    EnclosureDb().createTable()
    EnclosureDb().insertInto(["", "", 0, "123456"])
    EnclosureDb().insertInto(["", "", 0, "abcdef"])
    EnclosureDb().insertInto(["", "", 0, "abc123"])
    EnclosureDb().insertInto(["", "", 0, "123abc"])
    EnclosureDb().insertInto(["", "", 0, "456def"])