import psycopg2
from dotenv import load_dotenv
import os
""" Conecção com a tabela de Ambiente no banco de dados """
class EnclosureDb:
    def __init__(self) -> None:
        load_dotenv()
        DbPath = os.getenv("DB_Key")
        conection = eval(DbPath)
        self.db_connection = psycopg2.connect(**conection)
        self.it = self.db_connection.cursor()
        self.table = 'ambiente'
    
    def selectAll(self) -> list:
        command = f"SELECT * FROM {self.table} WHERE cuidador='123456'"
        self.it.execute(command)
        return self.it.fetchall()
    
    def getEnvironment(self, zkeeper = "") -> list:
        command = f"SELECT * FROM {self.table} WHERE cuidador='{zkeeper}'"
        self.it.execute(command)
        return self.it.fetchone()
    
    def update(self, values) -> bool:
        command = f"UPDATE {self.table} SET especie = %s, bioma = %s, quantidade = %s WHERE cuidador= %s"
        self.it.execute(command, values)
        self.db_connection.commit()
        return True
    
    def createTable(self) -> None:
        command = f'CREATE TABLE {self.table}(id serial, especie varchar(15), bioma varchar(15), quantidade smallint, cuidador varchar(6), CONSTRAINT pk_{self.table} PRIMARY KEY (id), CONSTRAINT fk_cuidador FOREIGN KEY (cuidador) REFERENCES cuidador(id));'
        self.it.execute(command)
        self.db_connection.commit()

    def insertInto(self, values) -> bool:
        command = f'INSERT INTO {self.table}(especie, bioma, quantidade, cuidador) VALUES (%s, %s, %s, %s)'
        self.it.execute(command, values)
        self.db_connection.commit()
        return True
    
    def deleteRow(self, values) -> bool:
        command = f"DELETE FROM {self.table} WHERE cuidador = %s"
        self.it.execute(command, values)
        self.db_connection.commit()
        return True