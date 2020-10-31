from getvoice import getvoice
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

def do(said):


    open_cmd(said)
    search(said)
    program_functions(said)
    talkings(said)



def listen():
    said = getvoice.getvoice()
    action = threading.Thread(target=do, args=[said])
    action.start()

def listen_for_flask():
    said = getvoice.getvoice()

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

if __name__ == "__main__":
    with open("opening", "w") as opening:
        opening.write("false")
    
    
    keep_listening()

     


