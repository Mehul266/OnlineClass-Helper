import speech_recognition as sr

r1 = sr.Recognizer()
r2 = sr.Recognizer()


with sr.Microphone() as source:
    print('Started:')
    audio = r2.listen(source)

if 'facebook' in r1.recognize_google(audio):
    print('detected')