def inserIntoTable(listColunas = (), table = ""):
        colunas = ",".join(listColunas)
        command = f'''
        INSERT INTO {table}({colunas})
        VALUES (%s, %s, %s, %s);
        '''
        return command

def get(username = "", table = ""):
        tabela = table
        command = f'''
            SELECT username, senha FROM {tabela} WHERE username='{username}'
        '''
        return command

def getAll(listColums = (), table = ""):
        listColunas = listColums
        colunas = ",".join(listColunas)
        command = f'''
        SELECT {colunas} FROM {table}
        '''
        return command
