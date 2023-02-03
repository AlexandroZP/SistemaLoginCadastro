from PySimpleGUI import PySimpleGUI as sg


try:
    password = ''
    with open('D:/Estudos/Programação/Projetos/SenhaMySQL.txt', 'r') as arquivo:
        password = arquivo.read()
except FileNotFoundError:
    password = None