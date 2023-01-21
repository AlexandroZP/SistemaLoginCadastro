from PySimpleGUI import PySimpleGUI as sg
import services.checking as chk
from connectBD import BaseDedados
import Telas.Init.connectCadastro as tB

class Cadastro():
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
        self.__layout = [
            [sg.Frame('CADASTRAR', self._frame_layout)],
            [sg.VerticalSeparator()],
            [sg.Text('Já é cadastrado ?')],
            [sg.Button('Fazer Login', key='-LOGIN_WINDOW-')]
        ]

        self.janela = sg.Window('Tela de Cadastro', self.__layout)


        while True:
            events, values = self.janela.read()



            match(events):
                case None:
                    break
                case '-LOGIN_WINDOW-':
                    tB.toLogin(self.janela)
                    break
                case '-REGISTER_BUTTON-':
                    nome = str(values['-NAME-'])
                    email = str(values['-EMAIL-'])
                    senha = str(values['-PASSWORD-'])
                    conSenha = str(values['-CONFIRM_PASS-']) 

                    allFilled = chk.allFilled(nome,email, senha ,conSenha)

                    if allFilled == True:
                        if chk.validAll(email, senha, conSenha) == 'Válido':
                            bd = BaseDedados()
                            print(email, senha, nome,"Cliente")
                            if chk.inBD(email, senha) == False:
                                bd.saveBd(len(bd.bd)+1,email,  nome, 'Cliente', senha)
                                sg.popup('Cadastrado')
                            else:
                                sg.popup('ERROR Usuario já existe')
                        else:
                            sg.popup(chk.validAll(email, senha, conSenha))
                    else:     
                        sg.popup('ERROR! Preencha todos os campos')
            

            if values['-SHOW_PASS-']:
                tB.showPass(self.janela, '-PASSWORD-')
            else:
                tB.hidePass(self.janela, '-PASSWORD-')
            
            if values['-SHOW_CONF_PASS-']:
                tB.showPass(self.janela, '-CONFIRM_PASS-')
            else:
                tB.hidePass(self.janela, '-CONFIRM_PASS-')












        
        

