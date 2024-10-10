import psycopg2

class CuidadorBanco:
    def __init__(self):
        conection = {
        'dbname': '20221214010016',
        'user': 'postgres',
        'password': 'pabd',
        'port': 5432,
        'host': 'localhost'
        }
        self.db_connection = psycopg2.connect(**conection)
        self.it = self.db_connection.cursor()
        self.table = 'cuidador'