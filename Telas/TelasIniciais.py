from PySimpleGUI import PySimpleGUI as sg


class TelasIniciais:
    def showPass(self):
        self.janela['senha'].update(password_char="")

    def hidePass(self):
        self.janela['senha'].update(password_char="*")


#Tela de login
class TelaLogin(TelasIniciais):
    def __init__(self):
        # Layout
        sg.theme('Reddit')
        self.layout = [
            [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20, 1))],
            [sg.Text('Senha:'), sg.Input(key='senha', password_char='*', size=(20, 3),change_submits=True), 
            sg.Checkbox('Mostrar senha', key='showP', enable_events=True)],
            [sg.Checkbox('Salvar o login ?')],
            [sg.Button('Entrar')]
        ]
        # Janela
        self.janela = sg.Window('Tela de Login', self.layout)



#Tela de cadastro
class TelaCadastro(TelasIniciais):
    def __init__(self):
        # Layout
        sg.theme('Reddit')
        self.layout = [
            [sg.Text('Usuário:')],
            [sg.Input(key='usuario', size=(40, 1))],
            [sg.Text('Senha:')],
            [sg.Input(key='senha', password_char='*', size=(40, 3),change_submits=True)],
            [sg.Checkbox('Mostrar senha', key='showP', enable_events=True)],
            [sg.Text('Digite a senha novamente:')],
            [sg.Input(key='r_senha', password_char='*', size=(40, 3),change_submits=True)],
            [sg.Button('Cadastrar')]
        ]
        # Janela
        self.janela = sg.Window('Tela de Cadastro', self.layout)




        
        

