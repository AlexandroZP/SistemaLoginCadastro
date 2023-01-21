
class BaseDedados:
    def __init__(self):
        self.__bd = []
        with open('tempBD.txt','r') as BancoDeDados:
            for linha in BancoDeDados:
                self.__bd.append(linha.split(';'))

    @property
    def bd(self):
        return self.__bd
    
    def saveBd(self, id, email, nome, typ, senha):
        dados = [str(id),email, nome, typ, senha]
        dados = ';'.join(dados)
        with open('tempBD.txt','a') as BancoDeDados:
            BancoDeDados.write(f'{dados};\n')
 


    

    




