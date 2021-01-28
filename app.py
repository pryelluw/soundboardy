import PySimpleGUI as sg
from models import SoundBoard


soundboard = SoundBoard()



#sg.theme('DarkAmber')	# Add a touch of color
# All the stuff inside your window.
layout = [[sg.Button('play', size=(10,10), font=('Default', 14), key='_PLAY_1_')], [sg.Exit()] ]



# Create the Window
window = sg.Window('SOUNDBOARDY', layout, size=(800,750))


# Event Loop to process "events" and get the "values" of the inputs
soundboard.prepare()
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break


    
    if event == '_PLAY_1_':
        print('clicked')
        print(soundboard)
        for effect in soundboard.effects:
            print(effect.__dict__)
            if effect.position == 1:
                effect.play()
            
window.close()

