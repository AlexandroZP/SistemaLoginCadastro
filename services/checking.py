import re
from services.connectBDMySQL import BaseDedados


def inBD(email, senha):
        try:
                dados = BaseDedados().read() 
                for dado in dados:
                        if email in dado and senha in dado:
                                return dado[4]
                else:
                        return 'False'
        except:
                return 'Algo deu errado ao buscar no banco de dados'

def searchBd(email):
        try:
                dados = BaseDedados().read()
                for dado in dados:
                        if email == dado[2]:
                                return list(dado)      
                else:
                        return 'False'
        except:
                return 'False'
       
        
        
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

