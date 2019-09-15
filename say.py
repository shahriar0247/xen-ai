import pyttsx3

def say(texttosay):
    engine = pyttsx3.init()

    engine.setProperty('rate', 160)
    engine.setProperty('volume',1.0)
    engine.say(texttosay)
    engine.runAndWait()
    engine.stop()