import PySimpleGUI as sg

layout = [  [sg.Text('My Window')],
            [sg.Input(visible=False, enable_events=True, key='-FILENAME-'), sg.FileSaveAs(target='-FILENAME-'),],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == '-FILENAME-':
        if not values['-FILENAME-']:
            sg.popup('you cancelled operation')
        else:
            sg.popup(f'you chose {values["-FILENAME-"]}')
window.close()