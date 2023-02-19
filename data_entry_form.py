import PySimpleGUI as sg
import sqlite3

#note: table called 'name' exists, with rows first_name and last_name both text type

conn = sqlite3.connect('space_hotel_db.db')
c = conn.cursor()

sg.theme('DarkBrown4')

layout = [  [sg.Text('Space Hotel Reservation System')],
            [sg.Text('Please enter your relevant information. '), sg.InputText(), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]


window = sg.Window('Cozmoz Space Hotel Booking', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    first_last = [(values[0], values[1])]
    c.executemany("INSERT INTO name VALUES (?, ?)", first_last)

window.close()

c.execute("SELECT * FROM name")
print(c.fetchall())

conn.commit()
conn.close()