from PySimpleGUI import PySimpleGUI as sg


class TelaLogin:
    def __init__(self):
        # Layout
        sg.theme('Reddit')
        layout = [
            [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(20, 3),change_submits=True), 
            sg.Checkbox('Mostrar senha', key='showP', enable_events=True)],
            [sg.Checkbox('Salvar o login ?')],
            [sg.Button('Entrar')]
        ]
        # Janela
        self.janela = sg.Window('Tela de Login', layout)


class TelaCadastro:
    def __init__(self):
        # Layout
        sg.theme('Reddit')
        layout = [
            [sg.Text('Usuário:')],
            [sg.Input(key='usuario', size=(40, 1))],
            [sg.Text('Senha:')],
            [sg.Input(key='senha', password_char='*', size=(40, 3),change_submits=True)],
            [sg.Text('Digite a senha novamente:')],
            [sg.Input(key='r_senha', password_char='*', size=(40, 3),change_submits=True)],
            [sg.Checkbox('Mostrar senha', key='showP', enable_events=True)],
            [sg.Button('Cadastrar')]
        ]
        # Janela
        self.janela = sg.Window('Tela de Cadastro', layout)
        

