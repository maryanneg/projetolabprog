import PySimpleGUI as sg
import csv
def tela_upload():
    sg.theme('Green')
    layout = [  [sg.Text('Tela de Upload', font=('arial',15),justification='center', size=(50, 1))],
            [sg.Text('Escolha o Arquivo',size=(15,5)), sg.Input('',key='upload'),sg.FileBrowse()],
            [sg.Button('Enviar'), sg.Button('Cancelar')] ]
    return sg.Window('Tela de Upload', layout = layout, finalize=True)
def tela_dados():
    layout = [[sg.Text('Tela de Dados', font=('arial', 15), justification='center', size=(50, 1))]


              ]
    return sg.Window('Dados do Arquivo', layout = layout, finalize= True)
janela1, janela2 = tela_upload(), None
while True:
    janela, eventos, valores = sg.read_all_windows()
    if janela == janela1 and eventos == sg.WINDOW_CLOSED and eventos == 'Cancelar':
        break
    if  janela ==janela1 and eventos == 'Enviar':

        if valores['upload']:
            print('Envio Concluido')
            janela2 = tela_dados()
            janela1.hide()
            with open(valores['upload']) as arquivo_csv:
                leitor = csv.reader(arquivo_csv, delimiter=',')
                for coluna in leitor:
                        print(coluna)
