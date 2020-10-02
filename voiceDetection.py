import speech_recognition as sr

def detectVoice(name):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Started:')
        audio = r.listen(source)

    if name in r.recognize_google(audio):
        print('detected')
        return 1
    

if __name__ == '__main__':
    name = input('Enter your name: ')
    detectVoice(name)