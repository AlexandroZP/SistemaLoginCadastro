import  Telas.Init.TelaDeCadastro as tlc


def toRegis(tela):
    tela.close()
    tela = tlc.Cadastro()


def showPass(janela, tag):
    janela[tag].update(password_char="")


def hidePass(janela, tag):
    janela[tag].update(password_char="*") 

