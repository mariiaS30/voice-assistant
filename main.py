import speech_recognition
import pyaudio
import webbrowser
import pyttsx3


sr = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()
voice = pyttsx3.init()
voice.setProperty('rate', 130)


with mic:
    request = sr.listen(source = mic) #voice
    text = sr.recognize_google(request, language = 'en').lower() #voice -> text 
    print(text)

if text == 'open google' or text == 'open google please' or text == 'please open google':
    voice.say('okay')
    voice.runAndWait()
    webbrowser.open('https://www.google.co.uk/')

elif text == 'open youtube' or text == 'please open youtube' or text == 'open youtube please':
    voice.say('okay')
    voice.runAndWait()
    webbrowser.open('https://www.youtube.com/')

elif text == 'voice hello':
    voice.say('Hello')
    voice.runAndWait()


#webbrowser.open('https://www.youtube.com/')
 

