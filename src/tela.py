import PySimpleGUI as sg

"""
    Simple Form (a one-shot data entry window)
    Use this design pattern to show a form one time to a user that is "submitted"
"""
MAX_COL = 5

columm_layout =  [
        [sg.Text(str(j), size=(4, 1), justification='right' ) ] +
        [sg.Input(size=(10, 1), pad=(  1, 1), justification='right', key=("nota" , j)) ]
        for j in range(MAX_COL)]

layout = [[sg.Text('Please enter your Name, Address, Phone')],
          [sg.Col(columm_layout, size=(800, 600), scrollable=True)],
          [sg.Button('Submit'), sg.Button('Cancel')]]

window = sg.Window('Simple Data Entry Window', layout)
event, values = window.read(close=True)

if event == 'Submit':
    # print('The events was ', event, 'You input', values['-NAME-'], values['-ADDRESS-'], values['-PHONE-'])

    for i in range(5):
        print(values["nota", i])
    pass
else:
    print('User cancelled')

