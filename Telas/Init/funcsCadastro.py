from  Telas.Init.TelaDeLogin import Login
from PySimpleGUI import PySimpleGUI as sg
from datetime import date
def toLogin(tela):
    try:
        tela.close()
        tela = Login()
    except:
        sg.popup('[ERROR]:Não foi possivel encontrar a tela de login...')


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


def genID(lenght):
    ano = date.today().year
    if lenght > 9:
        return f'{ano}{lenght}'
    else:
        return f'{ano}0{lenght}'