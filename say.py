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
import pyttsx3
import subprocess
import soundfile as sf
import pyrubberband as pyrb
import sys
from pydub import AudioSegment



def say(text):
    print(19)
    say_process(text)
    #multiprocessing.Process(target=say_process, args=[text]).start()
        
def say_process(text):
    if internet_on():
        print(20)
        say_online(text)
    else:
        say_offline(text)

def say_online(text):
    print(21)
    gtts_object = gTTS(text=text)
    set_temp_dir()
    filename = "temp/output2.mp3"
    print(22)
    gtts_object.save(filename)
    os.system("ffmpeg -i "+filename+" "+filename+".wav")

    filename = filename + ".wav"
    filename = change_speed(filename)
    print(23) 
    playsound(filename) 
    print(24)



def say_offline(text):
    pythoncom.CoInitialize()
    speak = wincl.Dispatch("SAPI.SpVoice")
    try:
        speak.Speak(text)
    except com_error:
        time.sleep(1)
        speak.Speak(text)
        
def say_offline2(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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

def change_speed(filename):
    y, sr = sf.read(filename)
    filename = filename + "3"
    # Play back at 1.5X speed
    y_stretch = pyrb.time_stretch(y, sr, 1.5)
    # Play back two 1.5x tones
    y_shift = pyrb.pitch_shift(y, sr, 1.5)
    sf.write(filename, y_stretch, sr, format='wav')
    return filename

def internet_on():
    try:
        urlopen('https://google.com', timeout=1)
        return True
    except URLError as err: 
        return False



