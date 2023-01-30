from PySimpleGUI import PySimpleGUI as sg
from Telas.Users.TelaDeUsuario import TelaDeUsuario

class Cliente(TelaDeUsuario):
    def __init__(self, user):
        super().__init__(user)
        self.janela = sg.Window('Cliente', self.layout, auto_size_text=False, default_element_size=(20,1),finalize=True)
        while True:
            if self.janela == Cliente:
                self.janela['-CHB_DELETAR-'].update(disabled=True)
            events, values = self.janela.read()
            match(events):
                case None:
                    break
                case '-BTN_LOGOFF-':
                    Cliente.deslogar(self, self.janela)
                    break
                case '-BTN_EDIT-':
                    Cliente.editar(self, self.janela, [values['-USER_DATE_ID-'], values['-USER_DATE_NAME-'], values['-USER_DATE_EMAIL-']])
                case '-BTN_SAVE-':
                    Cliente.save(self, self.janela)
        
           