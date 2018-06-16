#語音轉文字

import speech_recognition
import tempfile
from gtts import gTTS
from pygame import mixer
def listenTo():
    #適用英文
    r = speech_recognition.Recognizer()
    client_id = '***'
    client_key = '***'
    with speech_recognition.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    return r.recognize_houndify(audio, client_id, client_key)