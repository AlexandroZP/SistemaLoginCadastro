from  Telas.Init.TelaDeLogin import Login


def toLogin(tela):
    tela.close()
    tela = Login()


def showPass(janela, tag):
    janela[tag].update(password_char="")


def hidePass(janela, tag):
    janela[tag].update(password_char="*") 
