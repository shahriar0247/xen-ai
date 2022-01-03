import time
import say
import gettingtime
import os
from urllib.parse import quote
import subprocess
import getpass
from speech_recognition import UnknownValueError
import threading
import multiprocessing
import terminate_program
# from talkings import talkings
import open_any_program
from search import search
from program_functions import program_functions
from open_program import open_cmd
import speech_recognition as sr
import database
import gettingtime
from debug import debug

stop_listening = None

def do(said):
    debug(11)
    open_cmd(said)
    debug(12)
    search(said)
    debug(13)
    program_functions(said)
    debug(14)



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
    except UnknownValueError:
        debug("Unknown Value Error")
    
def listen():
    print("listening")
    r = sr.Recognizer() 
    with sr.Microphone() as source2:

        r.adjust_for_ambient_noise(source2, duration=0.2)
            

        audio2 = r.listen(source2)
    callback2(r, audio2)



def start_listening():
    try:
        listen()
    except UnknownValueError:
        debug("Unknown Value Error")

def keep_listening():
    while True:
        try:
            listen()
        except KeyboardInterrupt:
            debug("Keyboard Interrupt")
            break
        except UnknownValueError:
            debug("Unknown Value Error")

def keep_inputing():
    while True:
        try:
            said = input("Write something: ")
            action = threading.Thread(target=do, args=[said]).start()
        except KeyboardInterrupt:
            debug(KeyboardInterrupt)
            break


def start():
    debug(2)
    with open("opening", "w") as opening:
        opening.write("false")
    debug(3)
    keep_listening()




def listening_background():
    debug(4)
    r = sr.Recognizer()
    m = sr.Microphone()
    debug(5)
    with m as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    debug(6)
    global stop_listening
    stop_listening = r.listen_in_background(m, callback2)
    debug(7)
    say.say("Hello sir")


def callback2(r, audio):
    debug(8)
    try:
        said = r.recognize_google(audio)
        print(said)
        debug(9)
        debug(said)
        said = said.lower()
        debug(said)
        threading.Thread(target=do, args=[said]).start()
        debug(10)
        threading.Thread(target=database.save, args=[said]).start()
    except UnknownValueError:
        pass

if __name__ == "__main__":
    debug(1)
    start()
    debug("done")
    time.sleep(1000)


