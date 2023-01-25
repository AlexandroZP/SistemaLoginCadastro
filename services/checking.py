import re
from services.connectBD import BaseDedados


def inBD(email, senha):
        dados = BaseDedados()
        if len(dados.bd) > 0:
                for dado in dados.bd:
                        if email == dado[1]:
                                if senha == dado[4]:
                                        return dado[3]
        return 'False'


def searchBd(email):
        dados = BaseDedados()
        for dado in dados.bd:
                if email == dado[1]:
                        return [str(dado[0]), str(dado[2]), str(dado[1])]       
       
        
        
def allFilled(nome, email, senha, conSenha):
        if nome != '' != email:
                if senha != '' != conSenha:
                        return True
                else:
                        return False
        else:
                return False


def validPass(senha, conSenha):
        if len(senha) >= 8 and senha == conSenha:
                return True
        else:
                return False


def validEmail(email):
        padrao = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', email)
        if padrao:
                return True
        else:
                return False


def validAll(email, senha, conSenha):

        vEmail = validEmail(email)
        vSenha = validPass(senha, conSenha)

        if vEmail == True and vSenha == True:
                return 'Válido'
        elif vEmail == False and vSenha == True:
                return 'Email inválido'
        elif vEmail == True and vSenha == False:
                return 'ERROR senha deve ter minimo 8 caracteres'
        else:
                return 'ERROR Email e  login invalidos'

