from Telas.Users.TelaDeAdministrador import Administrador
from Telas.Users.TelaDeCliente import Cliente
from PySimpleGUI import PySimpleGUI as sg


def toAdmin(tela, user):
    try:
        tela.close()
        tela = Administrador(user)
    except:
        sg.popup('[ERROR]:Não foi possivel efetuar o login[Admin]...')


def toCliente(tela, user):
    try:
        tela.close()
        tela = Cliente(user)
    except:
        sg.popup('[ERROR]:Não foi possivel efetuar o login[Cliente]...')
