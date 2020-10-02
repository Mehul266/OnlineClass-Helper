from voiceDetection import detectVoice
from notification import email_alert

name = input("Enter your name: ")

while True:
    if detectVoice( name):
        email_alert()
        
