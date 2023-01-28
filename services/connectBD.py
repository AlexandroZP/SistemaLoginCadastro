
class BaseDedados:
    def __init__(self,):
        self.__bd = []
        with open('tempBD.txt','r') as BancoDeDados:
            for linha in BancoDeDados:
                self.__bd.append(linha.split(';'))

    @property
    def bd(self):
        return self.__bd
    
    @bd.setter
    def bd(self, dados):
        self.__bd = dados

    def delete(self, dados):
        with open('tempBD.txt', 'w') as BancoDeDados:
            BancoDeDados.write('')
        with open('tempBD.txt', 'a') as BancoDeDados:
            for dado in dados:
               bd = ';'.join(dado)            
               BancoDeDados.write(bd)


    def edit(self, dados):
        with open('tempBD.txt','r') as BancoDeDados:
            linhas = BancoDeDados.readlines()
            for linha in linhas:
                linha = linha.split(';')
                if linha[0] == dados[0]:
                    linha[2] = dados[1]
                    linha[1] = dados[2]
                    self.__bd[int(dados[0]) - 1] = linha
        with open ('tempBD.txt', 'w') as BancoDeDados:
            BancoDeDados.write('')
        with open('tempBD.txt','a') as BancoDeDados:
            for dado in self.__bd:
                dados = ';'.join(dado)
                BancoDeDados.write(dados)
            
                



    def saveBd(self, id, email, nome, typ, senha):
        dados = [str(id),email, nome, typ, senha]
        dados = ';'.join(dados)
        with open('tempBD.txt','a') as BancoDeDados:
            BancoDeDados.write(f'{dados};\n')
 


    

    




