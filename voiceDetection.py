import speech_recognition as sr

def detectVoice(name):
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening')
        audio = r.listen(source)
    try:
        if name in r.recognize_google(audio, language='en-IN'):
            print('detected')
            return 1
    except:
        print("Something is not right...")
    

if __name__ == '__main__':
    name = input('Enter your name: ')
    detectVoice(name)