import Telas.Init.TelasIniciais as tli

def toLogin(tela):
    tela.close()
    tela = tli.Login()


def toRegis(tela):
    tela.close()
    tela = tli.Cadastro()    
