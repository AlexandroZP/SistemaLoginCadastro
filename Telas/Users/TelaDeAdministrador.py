from PySimpleGUI import PySimpleGUI as sg
from Telas.Users.TelaDeUsuario import TelaDeUsuario
from connectBD import BaseDedados



   


class Administrador(TelaDeUsuario):
    def __init__(self):
        super().__init__()
        self.janela = sg.Window('Administrador', self.layout, auto_size_text=False, default_element_size=(20,1))
        while True:
            events, values = self.janela.read()
            match(events):
                case None:
                    print('Encerrando...')
                    break
                case '-BTN_LOGOFF-':
                    self.janela.close()
                    Administrador.deslogar(self, self.janela)
                    break
                case '-BTN_EDIT-':
                    Administrador.editar(self, self.janela)
                case '-BTN_SAVE-':
                    Administrador.save(self, self.janela)  
                case '-BTN_DELETAR-': 
                    list = self._users
                    bancoDeDados = BaseDedados()
                    removeList = values['-USERS_LIST-'][:]
                    removeList.sort(reverse=True)
                    for index in removeList:
                        list.pop(index)
                    self.janela['-USERS_LIST-'].update(values=list)
                    bancoDeDados.delete(list)
                    
 
                
            if values['-CHB_DELETAR-'] == True:
                self.janela['-BTN_DELETAR-'].update(disabled=False)
            else:
                self.janela['-BTN_DELETAR-'].update(disabled=True)
                
            







        
        