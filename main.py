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
from talkings import talkings
import open_any_program
from search import search
from program_functions import program_functions
from open_program import open_cmd
import speech_recognition as sr
import database
import gettingtime

def do(said):
    print(11)
    open_cmd(said)
    print(12)
    search(said)
    print(13)
    program_functions(said)
    print(14)
    talkings(said)


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
        print("Unknown Value Error")
    
def listen():
    pass

def start_listening():
    try:
        listen()
    except UnknownValueError:
        print("Unknown Value Error")

def keep_listening():
    while True:
        try:
            listen()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
        except UnknownValueError:
            print("Unknown Value Error")

def keep_inputing():
    while True:
        try:
            said = input("Write something: ")
            action = threading.Thread(target=do, args=[said]).start()
        except KeyboardInterrupt:
            print(KeyboardInterrupt)
            break


def start():
    print(2)
    with open("opening", "w") as opening:
        opening.write("false")
    print(3)
    listening_background()




def listening_background():
    print(4)
    r = sr.Recognizer()
    m = sr.Microphone()
    print(5)
    with m as source:
        r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening
    print(6)
    stop_listening = r.listen_in_background(m, callback2)
    print(7)
    say.say("Hello sir")


def callback2(r, audio):
    print(8)
    try:
        said = r.recognize_google(audio)
        print(9)
        print(said)
        said = said.lower()
        print(said)
        threading.Thread(target=do, args=[said]).start()
        print(10)
        threading.Thread(target=database.save, args=[said]).start()
    except UnknownValueError:
        pass

if __name__ == "__main__":
    print(1)
    start()
    print("done")
    time.sleep(1000)


