import PySimpleGUI as sg
from models import SoundBoard


soundboard = SoundBoard()
soundboard.prepare()


# menu buttons
menu_def = [
    ['Config', ['Setup']]
]



#sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Menu(menu_def, text_color="white")], # white because of OSX dark mode
    [sg.Button('', size=(4,2), key='1', button_color=('yellow','yellow')), sg.Text(soundboard.se1.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='2', button_color=('red','red')), sg.Text(soundboard.se2.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='3', button_color=('blue','blue')), sg.Text(soundboard.se3.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='4', button_color=('green','green')), sg.Text(soundboard.se4.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='5', button_color=('black','black')), sg.Text(soundboard.se5.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='6', button_color=('grey','grey')), sg.Text(soundboard.se6.name, font=('Default', 14))],
]



# Create the Window
window = sg.Window('SOUNDBOARDY', layout, size=(300,300))


# Event Loop to process "events" and get the "values" of the inputs

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break

    if event == '1':
        soundboard.se1.play()
    elif event == '2':
        soundboard.se2.play()
    elif event == '3':
        soundboard.se3.play()
    elif event == '4':
        soundboard.se4.play()
    elif event == '5':
        soundboard.se5.play()
    elif event == '6':
        soundboard.se6.play()

window.close()

