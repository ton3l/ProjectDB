class Usuario:
    def __init__(self, nome, username, idade, senha):
        self.nome = nome
        self.username = username
        self.idade = idade
        self.senha = senha
    
    def setnome(self,nome):
        self.nome = nome
        
    def getNome(self):
        return self.nome
    
    def setUsername(self,username):
        self.username = username

    def getUsername(self):
        return self.username
    
    def getSenha(self):
        return self.senha