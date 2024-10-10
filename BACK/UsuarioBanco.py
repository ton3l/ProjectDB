import psycopg2

class UsuarioBanco:
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