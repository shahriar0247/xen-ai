import win32com.client as wincl
import pythoncom
import time
from pywintypes import com_error
from gtts import gTTS 
import os 
import time
from playsound import playsound
from urllib.request import urlopen, URLError
import multiprocessing
import shutil
import threading


def say(text):
    # say_process(text)
    multiprocessing.Process(target=say_process, args=[text]).start()
        
def say_process(text):
    if internet_on():
        say_online(text)
    else:
        say_offline(text)

def say_online(text):
    gtts_object = gTTS(text=text)
    set_temp_dir()
    filename = "temp/" + str(time.time()) + ".mp3"
    gtts_object.save(filename) 
    playsound(filename) 

def say_offline(text):
    pythoncom.CoInitialize()
    speak = wincl.Dispatch("SAPI.SpVoice")
    try:
        speak.Speak(text)
    except com_error:
        time.sleep(1)
        speak.Speak(text)
        
def set_temp_dir():
    try:
        if os.path.isdir("temp"):
            shutil.rmtree('temp')
            os.mkdir("temp")
            return True
        else:
            os.mkdir("temp")
            return True
        return False
    except Exception as e:
        print(e)
        return False


def internet_on():
    try:
        urlopen('http://216.58.192.142', timeout=1)
        return True
    except URLError as err: 
        return False