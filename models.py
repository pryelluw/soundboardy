import json
from audioplayer import AudioPlayer


class SoundEffect:
    '''
    Represents a button in the GUI
    When clicked it plays the sound
    Stores button config state such as position
    and filename to play
    '''
    def __init__(self, filename, position=0):
        self.filename = filename
        self.position = position

    @property
    def name(self):
        return self.filename.split('.')[0]

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
        self.effects = []

    def load_config(self):
        with open('config.json', 'r') as f:
            return json.loads(f.read())


    def prepare(self):
        config = self.load_config()
        for sound_effect in config:
            se = SoundEffect(
                sound_effect.get('filename'),
                sound_effect.get('position')
            )
            print(se.__dict__)
            self.effects.append(se)
        
        print(self.effects)
        
        if not self.effects:
            raise ValueError('Could not load effects!')
        
