import PySimpleGUI as sg

sg.theme('DarkBrown4')

layout = [  [sg.Text('Space Hotel Reservation System')],
            [sg.Text('Please enter your relevant information. '), sg.InputText(), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]


window = sg.Window('Cozmoz Space Hotel Booking', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    print('You entered ', values)

window.close()

#testing