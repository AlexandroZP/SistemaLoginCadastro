from PySimpleGUI import PySimpleGUI as sg

class TelasDeUsuario:
    def deslogar(self):
        pass

#Tela do Cliente
class TelaDeCliente(TelasDeUsuario):
    def __init__(self):
        # Layout
        sg.theme('TanBlue')
        self.layout = [
            [sg.Text('Usuário'), sg.Text('Exemplo', background_color='white', text_color='black',size=(40,1))],
            [sg.Text('Email'), sg.Text('Exemplo@email.com', background_color='white', text_color='black',size=(40,1))],
            [sg.MenubarCustom(menu_definition = [['&Editar Perfil', []]])]
        ]
        # Janela
        self.janela = sg.Window('Logado como Cliente', self.layout)

#Tela do Admin
class TelaDeAdmin(TelasDeUsuario):
        def __init__(self):
            # Layout
            sg.theme('TanBlue')
            self.__col_layout = [[sg.T('#ID'),sg.Text('0000001', background_color='white', text_color='black')],
                                [sg.T('Nome:'),sg.Text('Exemplo', background_color='white', text_color='black')],
                                [sg.T('Email:'),sg.Text('Exemplo@email.com', background_color='white', text_color='black')]]
            __users = [
                ['000001', 'Exemplo1', 'exemplo1@email.com'],
                ['000002', 'Exemplo2', 'exemplo2@email.com'],
                ['000003', 'Exemplo3', 'exemplo3@email.com'],
                ['000004', 'Exemplo4', 'exemplo4@email.com'],
                ['000005', 'Exemplo5', 'exemplo5@email.com']
            ]
            self.layout = [
                [sg.Frame('Administrador',self.__col_layout, pad=(0,0))],
                [sg.Text('Usuários Cadastrados')],
                [sg.Table(values=__users, 
                headings=['#ID', 'Nome', 'Email'], auto_size_columns=True, display_row_numbers=True,
                justification='center', num_rows=len(__users)+1,row_height=30)],
                [sg.Checkbox('Deletar Usuários'), sg.Button('Deletar', pad=(0,0))]
            ]
            # Janela
            self.janela = sg.Window('Administrador', self.layout, auto_size_text=False, default_element_size=(20,1), keep_on_top=True)