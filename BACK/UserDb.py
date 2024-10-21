import psycopg2
from dotenv import load_dotenv
import os

class UserDb:
    def __init__(self):
        load_dotenv()
        DbPath = os.getenv("DB_Key")
        conection = eval(DbPath)
        self.db_connection = psycopg2.connect(**conection)
        self.it = self.db_connection.cursor()
        self.table = "usuario"
        

    def selectAll(self):
        command = f'SELECT * FROM {self.table}'
        self.it.execute(command)
        return self.it.fetchall()


    def getUser(self, username = ""):
        command = f'''
            SELECT username, senha FROM {self.table} WHERE username='{username}'
        '''
        self.it.execute(command)
        return self.it.fetchone()
    
    def authenticate(self, user = ()):
        colunas = "username,senha"
        command = f'SELECT {colunas} FROM {self.table}'
        self.it.execute(command)
        users = self.it.fetchall()
        for us in users:
            if(user == us):
                return True
        return False
    
    def createTable(self):
        command = f'CREATE TABLE {self.table}(username varchar(15), senha varchar(15), CONSTRAINT pk_{self.table} PRIMARY KEY (username));'
        self.it.execute(command)
        self.db_connection.commit()

    def insertInto(self, values):
        command = f'INSERT INTO {self.table} VALUES (%s, %s)'
        self.it.execute(command, values)
        self.db_connection.commit()
        return True