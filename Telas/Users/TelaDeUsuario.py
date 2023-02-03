from PySimpleGUI import PySimpleGUI as sg
import Telas.Init.funcsCadastro as tB
from services.connectBDMySQL import BaseDedados 

class TelaDeUsuario:
    def __init__(self, user):
        self.className = self.__class__.__name__
        lista = BaseDedados().read()
        baseDeDados = []
        for item in lista:
            baseDeDados.append(list(item))
        sg.theme('TanBlue')
        self._col_layout = [[sg.T('#ID'),sg.Input(user[0],key='-USER_DATE_ID-',pad=(5,0),border_width=0,size=(23,0),disabled=True,change_submits=True)],
                            [sg.T('Nome:'),sg.Input(user[1],key='-USER_DATE_NAME-',pad=(5,0),border_width=0,size=(23,0),disabled=True,change_submits=True)],
                            [sg.T('Email:'),sg.Input(user[2],key='-USER_DATE_EMAIL-',pad=(5,0),border_width=0,size=(23,0),disabled=True,change_submits=True)],
                            [sg.Button('Editar Perfil', key='-BTN_EDIT-', pad=(5,10)),sg.Push(), sg.Button('Salvar', key='-BTN_SAVE-', pad=(5, 5))]
                            ]
        self._users = baseDeDados
        self.__layout = [
            [sg.Push(), sg.Button('Logoff', key='-BTN_LOGOFF-', button_color='red', enable_events=True)],
            [sg.Frame(self.className, self._col_layout, pad=(0,0), element_justification='left',key='-DATE_FRAME-')],
            [sg.HorizontalSeparator()],
            [sg.Text('Usuários Cadastrados')],
            [sg.Table(values=self._users, 
            headings=['#ID', 'Email', 'Nome', 'Perfil'], auto_size_columns=True, display_row_numbers=True,
            justification='center', num_rows=len(self._users)+1,row_height=30, select_mode='extended',key='-USERS_LIST-')],
            [sg.Checkbox('Deletar Usuários', key='-CHB_DELETAR-',disabled=False, enable_events=True, change_submits=True), sg.Button('Deletar',key='-BTN_DELETAR-', pad=(0,0), disabled=True, change_submits=True,enable_events=True)]
        ] 

    @property
    def layout(self):
        return self.__layout


    def deslogar(self, janela):
        try:
            janela.close()
            tB.toLogin(janela)
        except:
            sg.popup('Não foi possivel chegar a tela de login')


    def editar(self, janela):
        try:
            janela['-USER_DATE_NAME-'].update(disabled=False)
            janela['-USER_DATE_EMAIL-'].update(disabled=False)
        except:
            sg.popup('Janela não encontrada')
    

    def save(self, janela, dados):
        try:
            BancoDeDados = BaseDedados()
            BancoDeDados.edit(dados)
            janela['-USER_DATE_NAME-'].update(disabled=True)
            janela['-USER_DATE_EMAIL-'].update(disabled=True)
        except:
            sg.popup('Janela não encontrada')
