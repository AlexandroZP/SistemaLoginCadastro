from PySimpleGUI import PySimpleGUI as sg
from Telas.Users.TelaDeUsuario import TelaDeUsuario
from services.connectBDMySQL import BaseDedados



   


class Administrador(TelaDeUsuario):
    def __init__(self, user):
        super().__init__(user)
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
                    Administrador.save(self, self.janela, [values['-USER_DATE_ID-'], values['-USER_DATE_NAME-'], values['-USER_DATE_EMAIL-']])  
                case '-BTN_DELETAR-': 
                    list = self._users
                    list_2 = []
                    bancoDeDados = BaseDedados()
                    removeList = values['-USERS_LIST-'][:]
                    removeList.sort(reverse=True)
                    for index in removeList:
                        list_2.append(list[index])
                        list.pop(index)
                    print(list)
                    list_2.sort(reverse=True)
                    print(list_2)
                    bancoDeDados.delete(list_2)
                    self.janela['-USERS_LIST-'].update(values=list)
                    
                    
 
                
            if values['-CHB_DELETAR-'] == True:
                self.janela['-BTN_DELETAR-'].update(disabled=False)
            else:
                self.janela['-BTN_DELETAR-'].update(disabled=True)
                
            







        
        