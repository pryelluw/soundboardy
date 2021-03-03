import json
from audioplayer import AudioPlayer


class SoundEffect:
    '''
    Represents a button in the GUI
    When clicked it plays the sound
    Stores button config state such as position
    and filename to play
    '''
    def __init__(self, filename, name):
        self.filename = filename
        self.name = name

    def play(self):
        # Playback stops when the object is destroyed (GC'ed), so save a reference to the 
        # object for non-blocking playback.
        path = f'files/{self.filename}'
        self.player = AudioPlayer(path)
        self.player.play()


class SoundBoard:
    '''
    Has all config info in order to run app
    '''
    def __init__(self):
        self.config = Config()

    def prepare(self):
        self.config.load()
        self.se1 = SoundEffect(self.config.settings.get('1').get('filename'), self.config.settings.get('1').get('name'))
        self.se2 = SoundEffect(self.config.settings.get('2').get('filename'), self.config.settings.get('2').get('name'))
        self.se3 = SoundEffect(self.config.settings.get('3').get('filename'), self.config.settings.get('3').get('name'))
        self.se4 = SoundEffect(self.config.settings.get('4').get('filename'), self.config.settings.get('4').get('name'))
        self.se5 = SoundEffect(self.config.settings.get('5').get('filename'), self.config.settings.get('5').get('name'))
        self.se6 = SoundEffect(self.config.settings.get('6').get('filename'), self.config.settings.get('6').get('name'))

    def update(self):
        self.se1.filename = self.config.settings_by_index(index='1')['filename']
        self.se1.name = self.config.settings_by_index(index='1')['name']

        self.se2.filename = self.config.settings_by_index(index='2')['filename']
        self.se2.name = self.config.settings_by_index(index='2')['name']

        self.se3.filename = self.config.settings_by_index(index='3')['filename']
        self.se3.name = self.config.settings_by_index(index='3')['name']

        self.se4.filename = self.config.settings_by_index(index='4')['filename']
        self.se4.name = self.config.settings_by_index(index='4')['name']

        self.se5.filename = self.config.settings_by_index(index='5')['filename']
        self.se5.name = self.config.settings_by_index(index='5')['name']

        self.se6.filename = self.config.settings_by_index(index='6')['filename']
        self.se6.name = self.config.settings_by_index(index='6')['name']


class Config:
    def __init__(self, settings=None):
        self.default_name = 'default'
        self.default_filename = 'test.mp3'
        self.base_settings = {
        	"1": {
        		"filename": "",
        		"name": ""
        	},
        	"2": {
        		"filename": "",
        		"name": ""
        	},
        	"3": {
        		"filename": "",
        		"name": ""
        	},
        	"4": {
        		"filename": "",
        		"name": ""
        	},
        	"5": {
        		"filename": "",
        		"name": ""
        	},
        	"6": {
        		"filename": "",
        		"name": ""
        	}
        } if not settings else settings

    @property
    def settings(self):
        return self.base_settings
    
    def truncate_name(self, name):
        # only names 20 chars long
        if not name:
            return self.default_name

        elif len(name) <= 20:
            return name

        return name[0:20] 
    
    def settings_by_index(self, index='1'):
        return self.settings[index]

    def update(self, filename, name, index='1'):
        '''index = int 1-6'''
        if index not in ['1', '2', '3', '4', '5', '6']:
            return
        # check filename ends with mp3
        elif filename[-3:] not in ['mp3', 'MP3'] or not filename:
            filename = self.default_filename
        elif not name:
            name = self.default_name

        self.base_settings[index]['filename'] = filename
        self.base_settings[index]['name'] = self.truncate_name(name)

    def to_json(self):
        return json.dumps(self.settings)

    def load(self):
        with open('config.json', 'r') as f:
            self.base_settings = json.loads(f.read())

    def save(self):
        with open('config.json', 'w') as f:
            f.write(self.to_json())
