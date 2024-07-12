import speech_recognition
import pyaudio
import webbrowser

sr = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()

with mic:
    request = sr.listen(source = mic) #voice
    text = sr.recognize_google(request, language = 'en').lower() #voice -> text 
    print(text)

if text == 'open google' or text == 'open google please' or text == 'please open google':
    print('okay')
    webbrowser.open('https://www.google.co.uk/')

elif text == 'open youtube' or text == 'please open youtube' or text == 'open youtube please':
    print('okay')
    webbrowser.open('https://www.youtube.com/')

elif text == 'voice hello':
    print('Hello')


#webbrowser.open('https://www.youtube.com/')

#assist has a voice 

