import PySimpleGUI as sg
import csv

def listagem_dados(lista, tamanho):


    for u in range(0, tamanho):
        print(lista[u])

    for i in range(2):
        for j in range(2):
            print(i,j)

    columm_layout = [
        [sg.Text(str(lista[i]), size=(8, 1), justification='right', key=(i))] +
        [sg.Input(size=(10, 1), pad=(1, 1), justification='right', key=(i, j)) for j in range(0,2) ]
        for i in range(tamanho)]

    return columm_layout

def tela_upload():
    sg.theme('DarkGreen3')
    layout = [  [sg.Text('Tela de Upload', font=('arial',15),justification='center', size=(50, 1))],
            [sg.Text('Escolha o Arquivo',size=(15,1)), sg.Input('',key='upload'),sg.FileBrowse()],
            [sg.Button('Enviar'), sg.Button('Cancelar')] ]
    return sg.Window('Tela de Upload', layout = layout, finalize=True)

def tela_dados(columm_layout):
    layout = [
        [sg.Text('Tela de Dados', font=('arial', 15), justification='center', size=(50, 1))],
        # [sg.Listbox('Aguarde um momento',size=(100,20), key='-OUT-')],

        [sg.Col(columm_layout, size=(800, 600), scrollable=True)],
        [sg.Button('Gerar'), sg.Button('Cancelar')]]
    return sg.Window('Dados do Arquivo', layout = layout, finalize= True)

janela1, janela2 = tela_upload(), None
lista = []
lista_pdf = []
while True:
    janela, eventos, valores = sg.read_all_windows()

    if janela == janela1 and eventos == sg.WINDOW_CLOSED and eventos == 'Cancelar':
        break

    if  janela == janela1 and eventos == 'Enviar':

        if valores['upload']:
            print('Envio Concluido')

            with open(valores['upload']) as arquivo_csv:
                leitor = csv.reader(arquivo_csv, delimiter=',')


                janela1.hide()
                janela1.close()

                dados = ''
                contador = 0
                for coluna in leitor:

                    if contador == 0:
                        contador = contador + 1
                        continue

                    lista.append(coluna[0])
                dados = listagem_dados(lista, len(lista))
                janela2 = tela_dados(dados)

    if janela == janela2 and eventos == sg.WINDOW_CLOSED or eventos == 'Cancelar':
        break
    if janela == janela2  and eventos == 'Gerar':

        # PEGA DADOS DA TELA E OS COLOCA NUM ARRAY PARA LISTAGEM DO PDF
        for i in range(len(lista)):
            dados_alunos = []
            dados_alunos.append(lista[i])
            for j in range(2):
                dados_alunos.append(valores[i,j])
                print(valores[i,j])
            dados_alunos.append(str(int(dados_alunos[1]) + int(dados_alunos[2])))
            lista_pdf.append(dados_alunos)

        print(lista_pdf)


