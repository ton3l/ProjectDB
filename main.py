from BACK.Usuario import Usuario
from BACK.UsuarioBanco import UsuarioBanco


user = Usuario("jorge", "j", 12, "123")
userbd = UsuarioBanco("usuario")

createTable = '''
        CREATE TABLE Usuario(
        nome varchar(50),
        username varchar(50),
        idade smallint,
        senha varchar(24)
        CONSTRAINT pk_usuario PRIMARY KEY 
    );
'''



listColunas = ("username", "senha")
tabela = "usuario"
us = ("a", "123")



result = userbd.authenticate(us)

#result = userbd.selectAllLines(listColunas)

print(result)
"""it.execute(f"insert into usuario({colunas}) values(%s,%s,%s,%s)",(listValores))
db_connection.commit()"""