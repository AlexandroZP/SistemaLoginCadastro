from PySimpleGUI import PySimpleGUI as sg


try:
    password = ''
    with open('D:/Estudos/Programação/Projetos/Senha.txt', 'r') as arquivo:
        password = arquivo.read()
except FileNotFoundError:
    password = None