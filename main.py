import Telas as tl
from PySimpleGUI import PySimpleGUI as sg


tela = tl.TelaCadastro()

while True:
    # Extrair dados
    events, values = tela.janela.read()
    if events == sg.WINDOW_CLOSED:
        break
    if values['showP'] == True:
        tela.janela['senha'].update(password_char="")
        tela.janela['r_senha'].update(password_char="")
    else:
        tela.janela['senha'].update(password_char="*")
        tela.janela['r_senha'].update(password_char="*")
    if events == 'Entrar':
        if values['usuario'] == 'jhonatan' and values['senha'] == '123456':
            print('Bem-vindo!!')