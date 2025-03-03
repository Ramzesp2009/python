import speech_recognition as sr
import sys
import webbrowser
import pyttsx3

def talk(words):
    print(words)
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

talk("Ich bin dein Virtueller Freund.Was kann ich für dict tun?")

def command():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Du kannst sagen.")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        task = r.recognize_google(audio, language="de-DE").lower()  # r.recognize_google(audio, language="ru-RU)
        print("Du hast gesagt: " + task)
    except sr.UnknownValueError:
        talk("Ich habe dich nicht verstanden")
        task = command()
    return task

def makeSomething(task):
    if "mach website auf" in task:
        talk("Das wird gemacht")
        url = 'https://google.com'
        webbrowser.open(url)
    elif 'stop' in task:
        talk("Ok, kein Problem.")
        sys.exit()
    elif 'wie heisst du' in task:
        talk('Mein Name ist Helper')


while True:
    makeSomething(command())


