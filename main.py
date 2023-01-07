import Telas as tl
from PySimpleGUI import PySimpleGUI as sg


tela = tl.TelaLogin()

while True:
    # Extrair dados
    events, values = tela.janela.read()
    if events == sg.WINDOW_CLOSED:
        break
    if values['showP']:
        tela.showPass()
    else:
        tela.hidePass()
    if events == 'Entrar':
        if values['usuario'] == 'jhonatan' and values['senha'] == '123456':
            print('Bem-vindo!!')