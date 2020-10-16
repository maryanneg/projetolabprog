import PySimpleGUI as sg
import csv
sg.theme('Green')
layout = [  [sg.Text('Tela de Upload', font=('arial',15),justification='center', size=(50, 1))],
            [sg.Text('Escolha o Arquivo',size=(15,5)), sg.Input('',key='upload'),sg.FileBrowse()],
            [sg.Button('Enviar'), sg.Button('Cancelar')] ]


tela = sg.Window('Tela de Upload', layout)

while True:
    eventos, valores = tela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    elif eventos == 'Cancelar':
        break
    if  eventos == 'Enviar':
        if valores['upload']:
            print('Envio Concluido', valores['upload'])
            with open(valores['upload']) as arquivo_csv:
                leitor = csv.reader(arquivo_csv, delimiter=',')
                for coluna in leitor:
                    print(coluna)