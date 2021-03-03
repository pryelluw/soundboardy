import PySimpleGUI as sg
from models import SoundBoard


soundboard = SoundBoard()
soundboard.prepare()

# menu buttons
menu_def = [
    ['Config', ['Setup']]
]

settings_layout =  [
    [sg.Text('Sound Effect #1')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file1', default_text=soundboard.config.settings_by_index('1')['name']), 
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse1')], # Note - file_types IS NOT SUPPORTED ON MAC
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label1', default_text=soundboard.config.settings_by_index('1')['name'])],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #2')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file2'),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse2')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label2')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #3')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file3'),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse3')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label3')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #4')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file4'),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse4')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label4')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #5')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file5'),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse5')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label5')],
    [sg.Text('_' * 100)],
    [sg.Text('Sound Effect #6')],
    [sg.Text('MP3 Sound File', size=(8, 1)), sg.Input(key='file6'),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse6')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label6')],
    [sg.Text('_' * 100)],
    [sg.Submit(), sg.Cancel()]
]

app_layout = [
    [sg.Menu(menu_def, text_color="white")], # white because of OSX dark mode
    [sg.Button('', size=(4,2), key='button1', button_color=('yellow','yellow')), sg.Text(soundboard.se1.name, key='text1', font=('Default', 14))],
    [sg.Button('', size=(4,2), key='button2', button_color=('red','red')), sg.Text( soundboard.se2.name, key='text2', font=('Default', 14))],
    [sg.Button('', size=(4,2), key='button3', button_color=('blue','blue')), sg.Text(soundboard.se3.name, key='text3', font=('Default', 14))],
    [sg.Button('', size=(4,2), key='button4', button_color=('green','green')), sg.Text(soundboard.se4.name, key='text4', font=('Default', 14))],
    [sg.Button('', size=(4,2), key='button5', button_color=('black','black')), sg.Text(soundboard.se5.name, key='text5', font=('Default', 14))],
    [sg.Button('', size=(4,2), key='button6', button_color=('grey','grey')), sg.Text(soundboard.se6.name, key='text6', font=('Default', 14))],
]

# settings config window
settings_window = sg.Window('Settings', settings_layout, finalize=True)
settings_window.hide()

# main app window
app_window = sg.Window('SOUNDBOARDY', app_layout, size=(300,300))


# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = app_window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break
    
    # open config
    if event == 'Setup':        
        settings_window.un_hide()
        settings_event, settings_values = settings_window.read()


        if settings_event == sg.WIN_CLOSED or settings_event == 'Cancel':
            settings_window.hide()
        
        elif settings_event == 'Submit':
            # update each directly and save to file
            # no loop for performance and keeping it simple
            soundboard.config.update(settings_values.get('file1'), settings_values.get('name1'), '1')
            soundboard.config.update(settings_values.get('file2'), settings_values.get('name2'), '2')
            soundboard.config.update(settings_values.get('file3'), settings_values.get('name3'), '3')
            soundboard.config.update(settings_values.get('file4'), settings_values.get('name4'), '4')
            soundboard.config.update(settings_values.get('file5'), settings_values.get('name5'), '5')
            soundboard.config.update(settings_values.get('file6'), settings_values.get('name6'), '6')
            soundboard.config.save()
            soundboard.update()
            
            # update labels
            app_window['text1'].update(value=soundboard.se1.name)
            app_window['text2'].update(value=soundboard.se2.name)
            app_window['text3'].update(value=soundboard.se3.name)
            app_window['text4'].update(value=soundboard.se4.name)
            app_window['text5'].update(value=soundboard.se5.name)
            app_window['text6'].update(value=soundboard.se6.name)    
            
        settings_window.hide()


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
