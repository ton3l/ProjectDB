import psycopg2
from . import dfFunctions


class UsuarioBanco:
    def __init__(self, table = ""):
        conection = {
        'dbname': '20221214010016',
        'user': 'postgres',
        'password': 'pabd',
        'port': 5432,
        'host': 'localhost'
        }
        self.db_connection = psycopg2.connect(**conection)
        self.it = self.db_connection.cursor()
        self.table = table
        

    def inserInto(self, listColunas = (), listValores = ()):
        command = dfFunctions.inserIntoTable(listColunas, self.table)
        self.it.execute(command, listValores)
        self.db_connection.commit()


    def getUser(self, username = ""):
        command = dfFunctions.get(username, self.table)
        self.it.execute(command)
        return self.it.fetchone()
    
    def authenticate(self, user = ()):
        listColunas = ("username","senha")
        command = dfFunctions.getAll(listColunas, self.table)
        self.it.execute(command)
        us = self.it.fetchall()
        for use in us:
            if(user == use):
                return True
        return False
