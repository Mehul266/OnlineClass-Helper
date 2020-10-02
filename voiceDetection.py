import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Started:')
    audio = r.listen(source)

if 'Mehul' in r.recognize_google(audio):
    print('detected')