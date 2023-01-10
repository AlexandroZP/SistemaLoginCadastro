import Telas.TelasIniciais as tli
import Telas.TelasDeUsuario as tlu
from PySimpleGUI import PySimpleGUI as sg


tela = tlu.TelaDeAdmin()

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