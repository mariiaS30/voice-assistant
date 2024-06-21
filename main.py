import speech_recognition
import pyaudio

sr = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

with mic:
    request = sr.listen(source = mic) #voice
    text = sr.recognize_google(request, language = 'en') #voice -> text 
    print(text)

