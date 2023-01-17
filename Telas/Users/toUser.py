from Telas.Users.TelaDeAdministrador import Administrador
from Telas.Users.TelaDeCliente import Cliente

def toAdmin(tela):
    tela.close()
    tela = Administrador()

def toCliente(tela):
    tela.close()
    tela = Cliente()