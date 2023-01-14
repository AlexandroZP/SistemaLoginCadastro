from PySimpleGUI import PySimpleGUI as sg

class TelasIniciais:


    def windowTrasition(self, janela, nome):
        if nome == 'Login':
            janela.close()
            janela = Cadastro()
        elif nome == 'Cadastro':
            janela.close()
            janela = Login()


    def showPass(self, tag):
        self.janela[tag].update(password_char="")


    def hidePass(self, tag):
        self.janela[tag].update(password_char="*")


class Login(TelasIniciais):   
    def __init__(self):
        self.className = __class__.__name__
        sg.theme('TanBlue')
        self._frame_layout = [
            [sg.T('Email:'),sg.Input(key='-EMAIL-',pad=(4,10),size=(20,0))],
            [sg.T('Senha:'),sg.Input(password_char='*',key='-PASSWORD-',pad=(0,0),size=(20,0)), 
            sg.Checkbox('Mostrar senha', key='-SHOW_PASS-', enable_events=True)],
            [sg.Checkbox('Salvar o login ?')],
            [sg.Button('Entrar', key='-LOGIN_BUTTON-')]
        ]

        self.layout = [
            [sg.Frame('LOGIN', self._frame_layout, pad=(0,0), element_justification='left')],           
            [sg.VerticalSeparator()],
            [sg.Text('Ainda não é cadastrado ?')],
            [sg.Button('Cadastrar !', key='-REGISTER_WINDOW-')]
        ]

        self.janela = sg.Window('Tela de Login', self.layout)
        while True:
            events, values = self.janela.read()
            match(events):
                case None:
                    break
                case '-REGISTER_WINDOW-':
                    Login.windowTrasition(self, self.janela, self.className)
                    break
                case '-LOGIN_BUTTON-':
                    sg.popup('LOGADO')
            
            if values['-SHOW_PASS-']:
                Login.showPass(self,'-PASSWORD-')
            else:
                Login.hidePass(self,'-PASSWORD-')


class Cadastro(TelasIniciais):
    def __init__(self):
        self.className = __class__.__name__
        sg.theme('TanBlue')
        self._frame_layout = [
            [sg.Text('Nome:')],
            [sg.Input(key='-NAME-', size=(40, 1))],
            [sg.Text('Email:')],
            [sg.Input(key='-EMAIL-', size=(40, 1))],
            [sg.Text('Senha:')],
            [sg.Input(key='-PASSWORD-', password_char='*', size=(40, 3),change_submits=True),sg.Checkbox('Mostrar', key='-SHOW_PASS-', enable_events=True)],
            [sg.Text('Digite a senha novamente:')],
            [sg.Input(key='-CONFIRM_PASS-', password_char='*', size=(40, 3),change_submits=True) ,sg.Checkbox('Mostrar', key='-SHOW_CONF_PASS-', enable_events=True)],
            [sg.Button('Cadastrar', key='-REGISTER_BUTTON-')],
        ]
        self.layout = [
            [sg.Frame('CADASTRAR', self._frame_layout)],
            [sg.VerticalSeparator()],
            [sg.Text('Já é cadastrado ?')],
            [sg.Button('Fazer Login', key='-LOGIN_WINDOW-')]
        ]

        self.janela = sg.Window('Tela de Cadastro', self.layout)


        while True:
            events, values = self.janela.read()           
            match(events):
                case None:
                    break
                case '-LOGIN_WINDOW-':
                    Cadastro.windowTrasition(self, self.janela, self.className)
                    break
                case '-REGISTER_BUTTON-':
                    sg.popup('CADASTRADO')
            
            if values['-SHOW_PASS-']:
                Cadastro.showPass(self, '-PASSWORD-')
            else:
                Cadastro.hidePass(self, '-PASSWORD-')
            
            if values['-SHOW_CONF_PASS-']:
                Cadastro.showPass(self, '-CONFIRM_PASS-')
            else:
                Cadastro.hidePass(self, '-CONFIRM_PASS-')












        
        

