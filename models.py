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
    def load_config(self):
        with open('config.json', 'r') as f:
            return json.loads(f.read())

    def prepare(self):
        config = self.load_config()
        self.se1 = SoundEffect(config.get('1').get('filename'), config.get('1').get('name'), 1)
        self.se2 = SoundEffect(config.get('2').get('filename'), config.get('2').get('name'), 2)
        self.se3 = SoundEffect(config.get('3').get('filename'), config.get('3').get('name'), 3)
        self.se4 = SoundEffect(config.get('4').get('filename'), config.get('4').get('name'), 4)
        self.se5 = SoundEffect(config.get('5').get('filename'), config.get('5').get('name'), 5)
        self.se6 = SoundEffect(config.get('6').get('filename'), config.get('6').get('name'), 6)
        
        