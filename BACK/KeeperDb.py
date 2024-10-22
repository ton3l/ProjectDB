import psycopg2
from dotenv import load_dotenv
import os
""" Conecção com a tabela de Cuidador no banco de dados """
class KeeperDb:
    def __init__(self) -> None:
        load_dotenv()
        DbPath = os.getenv("DB_Key")
        conection = eval(DbPath)
        self.db_connection = psycopg2.connect(**conection)
        self.it = self.db_connection.cursor()
        self.table = 'cuidador'
    
    def selectAll(self) -> list:
        command = f'SELECT * FROM {self.table}'
        self.it.execute(command)
        return self.it.fetchall()
    
    def insertInto(self, values) -> bool:
        command = f'INSERT INTO {self.table} VALUES (%s, %s)'
        self.it.execute(command, values)
        self.db_connection.commit()
        return True
    
    def getUser(self, id = "") -> list:
        command = f"SELECT * FROM {self.table} WHERE id='{id}'"
        self.it.execute(command)
        return self.it.fetchone()
    
    def update(self, values) -> bool:
        command = f"UPDATE {self.table} SET name = %s, id = %s WHERE id=%s"
        self.it.execute(command, values)
        self.db_connection.commit()
        return True
    
    def createTable(self) -> bool:
        command = f'CREATE TABLE {self.table}(name varchar(25), id varchar(6), CONSTRAINT pk_{self.table} PRIMARY KEY (id));'
        self.it.execute(command)
        self.db_connection.commit()
        return True
    
    def deleteRow(self, values) -> bool:
        command = f"DELETE FROM {self.table} WHERE id = %s"
        self.it.execute(command, values)
        self.db_connection.commit()
        return True