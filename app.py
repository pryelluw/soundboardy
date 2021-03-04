import PySimpleGUI as sg
from models import SoundBoard


soundboard = SoundBoard()
soundboard.prepare()

# menu buttons
menu_def = [
    ['Settings', ['Update']]
]

settings_layout =  [
    [sg.Text('Protip: Labels have a 20 character limit including spaces', text_color='black')],
    [sg.Text('Sound Effect #1')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file1', default_text=soundboard.config.settings_by_index('1')['filename']), 
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse1')], # Note - file_types IS NOT SUPPORTED ON MAC
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label1', default_text=soundboard.config.settings_by_index('1')['name'])],
    [sg.Text('_' * 68)],
    [sg.Text('Sound Effect #2')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file2', default_text=soundboard.config.settings_by_index('2')['filename']),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse2')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label2', default_text=soundboard.config.settings_by_index('2')['name'])],
    [sg.Text('_' * 68)],
    [sg.Text('Sound Effect #3')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file3', default_text=soundboard.config.settings_by_index('3')['filename']),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse3')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label3', default_text=soundboard.config.settings_by_index('3')['name'])],
    [sg.Text('_' * 68)],
    [sg.Text('Sound Effect #4')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file4', default_text=soundboard.config.settings_by_index('4')['filename']),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse4')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label4', default_text=soundboard.config.settings_by_index('4')['name'])],
    [sg.Text('_' * 68)],
    [sg.Text('Sound Effect #5')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file5', default_text=soundboard.config.settings_by_index('5')['filename']),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse5')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label5', default_text=soundboard.config.settings_by_index('5')['name'])],
    [sg.Text('_' * 68)],
    [sg.Text('Sound Effect #6')],
    [sg.Text('MP3 File', size=(8, 1)), sg.Input(key='file6', default_text=soundboard.config.settings_by_index('6')['filename']),
        sg.FileBrowse(file_types=(('MP3', '*.mp3')), key='browse6')],
    [sg.Text('Label', size=(8, 1)), sg.Input(key='label6', default_text=soundboard.config.settings_by_index('6')['name'])],
    [sg.Text('_' * 68)],
    [sg.Submit(), sg.Cancel()]
]

app_layout = [
    [sg.Menu(menu_def, text_color="white")], # white because of OSX dark mode
    [sg.Button('', size=(4,2), key='button1', button_color=('yellow','yellow')), sg.Text(soundboard.se1.name, key='text1', font=(20, 15))],
    [sg.Button('', size=(4,2), key='button2', button_color=('red','red')), sg.Text( soundboard.se2.name, key='text2', font=(20, 15))],
    [sg.Button('', size=(4,2), key='button3', button_color=('blue','blue')), sg.Text(soundboard.se3.name, key='text3', font=(20, 15))],
    [sg.Button('', size=(4,2), key='button4', button_color=('green','green')), sg.Text(soundboard.se4.name, key='text4', font=(20, 15))],
    [sg.Button('', size=(4,2), key='button5', button_color=('black','black')), sg.Text(soundboard.se5.name, key='text5', font=(20, 15))],
    [sg.Button('', size=(4,2), key='button6', button_color=('grey','grey')), sg.Text(soundboard.se6.name, key='text6', font=(20, 15))],
]

# settings config window
settings_window = sg.Window('Settings', settings_layout, finalize=True, disable_close=False, disable_minimize=False,)
settings_window.hide()

# main app window
app_window = sg.Window('Soundboardy', app_layout, size=(350,310))

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = app_window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':	# if user closes window or clicks cancel
        break

    # open settings
    if event == 'Update':       
        settings_window.un_hide()
        settings_event, settings_values = settings_window.read()

        if settings_event == sg.WIN_CLOSED:
            break

        if settings_event == 'Cancel':
            settings_window.hide()

        elif settings_event == 'Submit':
            # update each directly and save to file
            # no loop for performance and keeping it simple
            soundboard.config.update(settings_values.get('file1'), settings_values.get('label1'), '1')
            soundboard.config.update(settings_values.get('file2'), settings_values.get('label2'), '2')
            soundboard.config.update(settings_values.get('file3'), settings_values.get('label3'), '3')
            soundboard.config.update(settings_values.get('file4'), settings_values.get('label4'), '4')
            soundboard.config.update(settings_values.get('file5'), settings_values.get('label5'), '5')
            soundboard.config.update(settings_values.get('file6'), settings_values.get('label6'), '6')
            soundboard.config.save()
            soundboard.update()

            # update settings window widgets with new config
            settings_window['file1'].update(value=soundboard.se1.filename)
            settings_window['label1'].update(value=soundboard.se1.name)
            settings_window['file2'].update(value=soundboard.se2.filename)
            settings_window['label2'].update(value=soundboard.se2.name)
            settings_window['file3'].update(value=soundboard.se3.filename)
            settings_window['label3'].update(value=soundboard.se3.name)
            settings_window['file4'].update(value=soundboard.se4.filename)
            settings_window['label4'].update(value=soundboard.se4.name)
            settings_window['file5'].update(value=soundboard.se5.filename)
            settings_window['label5'].update(value=soundboard.se5.name)
            settings_window['file6'].update(value=soundboard.se6.filename)
            settings_window['label6'].update(value=soundboard.se6.name)

            # update app window widgets with new config
            app_window['text1'].update(value=soundboard.se1.name)
            app_window['text2'].update(value=soundboard.se2.name)
            app_window['text3'].update(value=soundboard.se3.name)
            app_window['text4'].update(value=soundboard.se4.name)
            app_window['text5'].update(value=soundboard.se5.name)
            app_window['text6'].update(value=soundboard.se6.name)

            settings_window.hide()

    # play sounds according to button clicked
    # note that sounds do not block eahc other
    if event == 'button1':
        soundboard.se1.play()
    elif event == 'button2':
        soundboard.se2.play()
    elif event == 'button3':
        soundboard.se3.play()
    elif event == 'button4':
        soundboard.se4.play()
    elif event == 'button5':
        soundboard.se5.play()
    elif event == 'button6':
        soundboard.se6.play()

settings_window.close()
app_window.close()
