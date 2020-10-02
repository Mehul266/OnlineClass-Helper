from voiceDetection import detectVoice
from notification import email_alert

name = input("Enter your name: ")
email = input("Enter your email address: ")

while True:
    if detectVoice( name):
        email_alert('OSCAP', 'Your name was detected', email)

