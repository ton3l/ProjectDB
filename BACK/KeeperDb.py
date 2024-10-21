import psycopg2
from dotenv import load_dotenv
import os

class KeeperDb:
    def __init__(self):
        load_dotenv()
        DbPath = os.getenv("DB_Key")
        conection = eval(DbPath)
        self.db_connection = psycopg2.connect(**conection)
        self.it = self.db_connection.cursor()
        self.table = 'cuidador'
    
    def selectAll(self):
        command = f'SELECT * FROM {self.table}'
        self.it.execute(command)
        return self.it.fetchall()
    
    def insertInto(self, values):
        command = f'INSERT INTO {self.table} VALUES (%s, %s)'
        self.it.execute(command, values)
        self.db_connection.commit()
        return True
    
    def getUser(self, id = ""):
        command = f"SELECT * FROM {self.table} WHERE id='{id}'"
        self.it.execute(command)
        return self.it.fetchone()
    
    def update(self, values):
        command = f"UPDATE {self.table} SET nome = %s, id = %s WHERE id=%s"
        self.it.execute(command, values)
        self.db_connection.commit()
        return True
    
    def createTable(self):
        command = f'CREATE TABLE {self.table}(name varchar(25), id varchar(6), CONSTRAINT pk_{self.table} PRIMARY KEY (id));'
        self.it.execute(command)
        self.db_connection.commit()
    