from Telas.Users.TelaDeAdministrador import Administrador
from Telas.Users.TelaDeCliente import Cliente

def toAdmin(tela, user):
    tela.close()
    tela = Administrador(user)


def toCliente(tela, user):
    tela.close()
    tela = Cliente(user)
