import mysql.connector
from secret import password

class BaseDedados:

    def __init__(self):
        # Criar conexão
        self.conexao = mysql.connector.connect(
            host ='localhost',
            user='root',
            password=password,
            database='bdusers'
        )
        self.cursor =  self.conexao.cursor()
    

    def delete(self, lista):
        for item in lista:
            comando = f'DELETE FROM usuarios WHERE idUsuarios = {item[0]}'
            self.cursor.execute(comando)
            self.conexao.commit() #Edita o banco de dados


    def edit(self, dados):
        comando = f'UPDATE usuarios SET nome_usuario = "{dados[1]}", email_usuario = "{dados[2]}" WHERE idUsuarios = {dados[0]}'
        self.cursor.execute(comando)
        self.conexao.commit() #Edita o banco de dados
                           
    def read(self):
        comando = f'SELECT * FROM usuarios;'
        self.cursor.execute(comando)
        dados = self.cursor.fetchall() 
        return dados

    def saveBd(self, email, nome, typ, senha):
        comando = f'INSERT INTO usuarios (nome_usuario, email_usuario, senha_usuario, tipo_usuario) VALUES ("{nome}", "{email}","{senha}","{typ}")'
        self.cursor.execute(comando)
        self.conexao.commit() 
 


    

    




