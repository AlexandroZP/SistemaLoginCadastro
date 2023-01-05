from PySimpleGUI import PySimpleGUI as sg

# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário:'),sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha:'),sg.Input(key='senha', password_char='*',size=(20,3),change_submits=True), sg.Checkbox('Mostrar senha', key='showP', enable_events=True)],
    [sg.Checkbox('Salvar o login ?')],
    [sg.Button('Entrar')]
]
# Janela
janela = sg.Window('Tela de Login', layout)
# Ler os eventos
while True:
    eventos, valores = janela.read()
    
    if eventos == sg.WINDOW_CLOSED:
        break
    if valores['showP'] == True:
        janela['senha'].update(password_char="")
    else:
        janela['senha'].update(password_char="*")
    if eventos == 'Entrar':
        if valores['usuario'] == 'jhonatan' and valores['senha'] == '123456':
            print('Bem-vindo!!')
