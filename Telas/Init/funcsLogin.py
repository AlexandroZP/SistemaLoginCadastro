import  Telas.Init.TelaDeCadastro as tlc
from PySimpleGUI import PySimpleGUI as sg


def toRegis(tela):
    try:
        tela.close()
        tela = tlc.Cadastro()
    except:
        sg.popup('[ERROR]:Não foi possivel chegar a tela de cadastro...')


def showPass(janela, tag):
    try:
        janela[tag].update(password_char="")
    except Exception:
        print('Tela ou TAG não foram passadas corretamente')


def hidePass(janela, tag):
    try:
        janela[tag].update(password_char="*")
    except Exception:
        print('Tela ou TAG não foram passadas corretamente')

