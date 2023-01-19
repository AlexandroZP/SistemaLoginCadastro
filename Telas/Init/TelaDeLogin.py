from PySimpleGUI import PySimpleGUI as sg
from Telas.Users.toUser import toAdmin, toCliente
import Telas.Init.TelaDeLoginBackEnd as tB

class Login():   
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

        self.__layout = [
            [sg.Frame('LOGIN', self._frame_layout, pad=(0,0), element_justification='left')],           
            [sg.VerticalSeparator()],
            [sg.Text('Ainda não é cadastrado ?')],
            [sg.Button('Cadastrar !', key='-REGISTER_WINDOW-')]
        ]

        self.janela = sg.Window('Tela de Login', self.__layout)
        while True:
            events, values = self.janela.read()
            match(events):
                case None:
                    break
                case '-REGISTER_WINDOW-':
                    tB.toRegis(self.janela)
                    break
                case '-LOGIN_BUTTON-':
                    toCliente(self.janela)
                    break
                
            if values['-SHOWPASS-']:
                tB.showPass(self,'-PASSWORD-')
            else:
                tB.hidePass(self,'-PASSWORD-')