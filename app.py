import PySimpleGUI as sg
from models import SoundBoard


soundboard = SoundBoard()
soundboard.prepare()

# menu buttons
menu_def = [
    ['Config', ['Setup']]
]

# button colors
colors = (
    'red',
    'blue',
    'yellow',
    'green',
    'black',
    'grey'
)

settings_layout =  [
    [sg.Text('Sound Effect #1')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file1'), sg.FileBrowse()],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label1') ],
    [sg.Text('Color'), sg.Combo(values=colors, default_value=colors[0], size=(10, 10), text_color='black', key='color1')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #2')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file2'), sg.FileBrowse()],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label2')],
    [sg.Text('Color'), sg.Combo(values=colors, default_value=colors[0], size=(10, 10), text_color='black', key='color2')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #3')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file3'), sg.FileBrowse()],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label3')],
    [sg.Text('Color'), sg.Combo(values=colors, default_value=colors[0], size=(10, 10), text_color='black', key='color3')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #4')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file4'), sg.FileBrowse()],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label4')],
    [sg.Text('Color'), sg.Combo(values=colors, default_value=colors[0], size=(10, 10), text_color='black', key='color4')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #5')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file5'), sg.FileBrowse()],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label5')],
    [sg.Text('Color'), sg.Combo(values=colors, default_value=colors[0], size=(10, 10), text_color='black', key='color5')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #6')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file6'), sg.FileBrowse()],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label6')],
    [sg.Text('Color'), sg.Combo(values=colors, default_value=colors[0], size=(10, 10), text_color='black', key='color6')],
    [sg.Text('_' * 100)],
    [sg.Submit(), sg.Cancel()]
]

app_layout = [
    [sg.Menu(menu_def, text_color="white")], # white because of OSX dark mode
    [sg.Button('', size=(4,2), key='1', button_color=('yellow','yellow')), sg.Text(soundboard.se1.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='2', button_color=('red','red')), sg.Text(soundboard.se2.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='3', button_color=('blue','blue')), sg.Text(soundboard.se3.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='4', button_color=('green','green')), sg.Text(soundboard.se4.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='5', button_color=('black','black')), sg.Text(soundboard.se5.name, font=('Default', 14))],
    [sg.Button('', size=(4,2), key='6', button_color=('grey','grey')), sg.Text(soundboard.se6.name, font=('Default', 14))],
]

# settings window
settings_window = sg.Window('Settings', settings_layout)

# main app window
app_window = sg.Window('SOUNDBOARDY', app_layout, size=(300,300))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = app_window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    
    # open config
    if event == 'Setup':
        settings_event, settings_values = settings_window.read()
        print(settings_event, settings_values)
        
        
        
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

app_window.close()
