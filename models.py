import json
from audioplayer import AudioPlayer


class SoundEffect:
    '''
    Represents a button in the GUI
    When clicked it plays the sound
    Stores button config state such as position
    and filename to play
    '''
    def __init__(self, filename, name, position=0):
        self.filename = filename
        self.name = name
        self.position = position

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
        self.config.load_config()
        self.se1 = SoundEffect(self.config.settings.get('1').get('filename'), self.config.settings.get('1').get('name'), 1)
        self.se2 = SoundEffect(self.config.settings.get('2').get('filename'), self.config.settings.get('2').get('name'), 2)
        self.se3 = SoundEffect(self.config.settings.get('3').get('filename'), self.config.settings.get('3').get('name'), 3)
        self.se4 = SoundEffect(self.config.settings.get('4').get('filename'), self.config.settings.get('4').get('name'), 4)
        self.se5 = SoundEffect(self.config.settings.get('5').get('filename'), self.config.settings.get('5').get('name'), 5)
        self.se6 = SoundEffect(self.config.settings.get('6').get('filename'), self.config.settings.get('6').get('name'), 6)


class Config:
    def __init__(self, settings=None):
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
    
    def settings_by_index(self, index='1'):
        return self.settings[index]['filename'], self.settings[index]['name']

    def update(filename, name, index=1):
        '''index = int 1-6'''
        if index not in [1,2,3,5,6]:
            return
        if not filename:
            return
        if not name:
            return
         
        self.base_settings[index]['filename'] = filename
        self.base_settings(index)['name'] = name

    def to_json(self):
        return json.dumps(self.settings)

    def load_config(self):
        with open('config.json', 'r') as f:
            self.base_settings = json.loads(f.read())

    def write_config(self):
        with open('config.json', 'w') as f:
            f.write(self.to_json())
