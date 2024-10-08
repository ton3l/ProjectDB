import psycopg2

class UsuarioBanco:
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
        self.table = "usuario"
        

    def selectAll(self):
        command = f'SELECT * FROM usuario'
        self.it.execute(command)
        return self.it.fetchall()


    def getUser(self, username = ""):
        command = f'''
            SELECT username, senha FROM usuario WHERE username='{username}'
        '''
        self.it.execute(command)
        return self.it.fetchone()
    
    def authenticate(self, user = ()):
        colunas = "username,senha"
        command = f'SELECT {colunas} FROM usuario'
        self.it.execute(command)
        users = self.it.fetchall()
        for us in users:
            if(user == us):
                return True
        return False