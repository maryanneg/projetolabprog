import PySimpleGUI as sg


#layout
sg.theme('green')
layout = [  [sg.Text('Turma 1', font=('arial',32), justification='center', size=(55, 2))],
            [sg.Text('alunosalunosalunosalunos'*50, font=('arial',15), justification='center', size=(55, 21))],
            [sg.Button('Anterior', size=(10, 1)), sg.Button('Próximo', size=(10, 1))]  ]

#Janela
tela = sg.Window('Turmas', layout, element_justification='c', keep_on_top=True, size=(900, 650))

#Ler os eventos
while True:
    eventos, valores = tela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    #elif eventos == 'Anterior':
        #ele volta uma tela
    #elif eventos == 'Próximo':
        #ele pula uma tela