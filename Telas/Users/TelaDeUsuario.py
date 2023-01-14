from PySimpleGUI import PySimpleGUI as sg
from Telas import TelasIniciais as tli

class TelaDeUsuario:
    def __init__(self):
        self.className = self.__class__.__name__
        sg.theme('TanBlue')
        self._col_layout = [[sg.T('#ID'),sg.Input('0000001', key='-USER_DATE_ID-',pad=(5,0),border_width=0,size=(23,0),disabled=True,change_submits=True)],
                            [sg.T('Nome:'),sg.Input('Exemplo', key='-USER_DATE_NAME-',pad=(5,0),border_width=0,size=(23,0),disabled=True,change_submits=True)],
                            [sg.T('Email:'),sg.Input('Exemplo1@email.com',key='-USER_DATE_EMAIL-',pad=(5,0),border_width=0,size=(23,0),disabled=True,change_submits=True)],
                            [sg.Button('Editar Perfil', key='-BTN_EDIT-', pad=(5,10)),sg.Push(), sg.Button('Salvar', key='-BTN_SAVE-', pad=(5, 5))]
                            ]
        self._users = [
            ['000001', 'Exemplo1', 'exemplo1@email.com'],
            ['000002', 'Exemplo2', 'exemplo2@email.com'],
            ['000003', 'Exemplo3', 'exemplo3@email.com'],
            ['000004', 'Exemplo4', 'exemplo4@email.com'],
            ['000005', 'Exemplo5', 'exemplo5@email.com']
        ]
        self.__layout = [
            [sg.Push(), sg.Button('Logoff', key='-BTN_LOGOFF-', button_color='red', enable_events=True)],
            [sg.Frame(self.className, self._col_layout, pad=(0,0), element_justification='left',key='-DATE_FRAME-')],
            [sg.HorizontalSeparator()],
            [sg.Text('Usuários Cadastrados')],
            [sg.Table(values=self._users, 
            headings=['#ID', 'Nome', 'Email'], auto_size_columns=True, display_row_numbers=True,
            justification='center', num_rows=len(self._users)+1,row_height=30, select_mode='extended',key='-USERS_LIST-')],
            [sg.Checkbox('Deletar Usuários', key='-CHB_DELETAR-',disabled=False, enable_events=True, change_submits=True), sg.Button('Deletar',key='-BTN_DELETAR-', pad=(0,0), disabled=True, change_submits=True,enable_events=True)]
        ] 

    @property
    def layout(self):
        return self.__layout


    def deslogar(self, janela):
        janela.close()
        janela = tli.Login()


    def editar(self, janela):
        janela['-USER_DATE_ID-'].update(disabled=False)
        janela['-USER_DATE_NAME-'].update(disabled=False)
        janela['-USER_DATE_EMAIL-'].update(disabled=False)
    
    def save(self, janela):
        janela['-USER_DATE_ID-'].update(disabled=True)
        janela['-USER_DATE_NAME-'].update(disabled=True)
        janela['-USER_DATE_EMAIL-'].update(disabled=True)
