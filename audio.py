from audioplayer import AudioPlayer


def play(filename):
    # Playback stops when the object is destroyed (GC'ed), so save a reference to the 
    # object for non-blocking playback.
    path = f'files/{filename}'
    AudioPlayer(path).play()
