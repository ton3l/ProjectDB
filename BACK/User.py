class User:
    def __init__(self, nome, username, idade, senha):
        self.username = username
        self.senha = senha
    
    def getUsername(self):
        return self.username
    
    def getSenha(self):
        return self.senha