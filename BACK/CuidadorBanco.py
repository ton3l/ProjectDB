import psycopg2

class CuidadorBanco:
    def __init__(self):
        conection = {
            'dbname': 'postgres',
            'user': 'postgres',
            'password': '1234',
            'port': 5432,
            'host': 'localhost'
        }
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