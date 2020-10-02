import speech_recognition as sr

def detectVoice(name):
    r = sr.Recognizer()

with sr.Microphone() as source:
    print('Started:')
    audio = r.listen(source)

if name in r.recognize_google(audio):
    print('detected')

if __name__ == '__main__':
    name = print('Enter your name: ')
    detectVoice(name)