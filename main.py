
import speech_recognition as sr # pip install speech_recognition
import pyttsx3    # pip install pyttsx3
import pywhatkit    # pip install pywhatkit
import datetime    # pip install speech_recognition
import wikipedia    # pip install wikipedia

listener = sr.Recognizer()
engin=pyttsx3.init()
voices = engin.getProperty('voices')
engin.setProperty('voice',voices[0].id)


def talk(text):
    engin.say(text)
    #engin.say('i am here sir......')
    #engin.say('how can i help you......')
    engin.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..........')
            voice=listener.listen(source)
            command = listener.recognize_google(voice)
            command=command.lower()
            if 'jarvis' in command:
                command=command.replace('jarvis','')
                print(command)

    except:
        pass
    return command





def run_jarvis():
    command=take_command()
    if 'play' in command:
        song = command.replace('play', '')
        print(song)
        talk('playing')
        print('playing..............',song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=command.replace('time','')
        time=datetime.datetime.strftime('%I:%M %p')
        talk('Current time is '+time)
    elif 'who is ' in command:
        person=command.replace('who is ','')
        info=wikipedia.summary(person,1)
        talk(info)

while True:
    run_jarvis()