import speech_recognition
import tempfile
from gtts import gTTS
from pygame import mixer

def speak(sentence, lang):
    mixer.init()
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence, lang=lang)
        tts.save("{}.mp3".format(fp.name))
        mixer.music.load('{}.mp3'.format(fp.name))
        mixer.music.play()