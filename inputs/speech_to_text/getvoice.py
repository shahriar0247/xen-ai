import threading
import speech_recognition as sr
import data_handling.database as database
import processing.Direct_Logic.gettingtime as gettingtime
from outputs.text_to_speech.say import say


def getvoice():
        r = sr.Recognizer()
        with sr.Microphone() as source:
                
                audio = r.listen(source)
        
        said = r.recognize_google(audio)
        said = said.lower()
        return said

def listening_background():
    
    r = sr.Recognizer()
    m = sr.Microphone()
    
    with m as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    
    global stop_listening
    stop_listening = r.listen_in_background(m, callback2)
    


def callback2(r, audio):
    
    try:
        said = r.recognize_google(audio)
        print(said)
        
        
        said = said.lower()
        
        threading.Thread(target=do, args=[said]).start()
        
        threading.Thread(target=database.save, args=[said]).start()
    except sr.UnknownValueError:
        pass






def listen_for_flask():
    said = listening_background()

    try:
        try:
            with open("listening", "r") as a:
                if a.read() == "true":
                    action = threading.Thread(target=do, args=[said])
                    action.start()
        except FileNotFoundError as e:
            action = threading.Thread(target=do, args=[said])
            action.start()
    except sr.UnknownValueError:
        pass
    
def listen():
    
    r = sr.Recognizer() 
    with sr.Microphone() as source2:

        r.adjust_for_ambient_noise(source2, duration=0.2)
            

        audio2 = r.listen(source2)
    callback2(r, audio2)
