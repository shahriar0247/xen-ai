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
from pydub.playback import play
import subprocess

def speed_change(sound, speed=1.0):
    # Manually override the frame_rate. This tells the computer how many
    # samples to play per second
    sound_with_altered_frame_rate = sound._spawn(sound.raw_data, overrides={
         "frame_rate": int(sound.frame_rate * speed)
      })
     # convert the sound with altered frame rate to a standard frame rate
     # so that regular playback programs will work right. They often only
     # know how to play audio at standard frame rate (like 44.1k)
    return sound_with_altered_frame_rate.set_frame_rate(sound.frame_rate)



def say(text):
    
    print(text)
    say_process(text)
    #multiprocessing.Process(target=say_process, args=[text]).start()
        
def say_process(text):
    if internet_on():
        
        say_online(text)
    else:
        say_offline(text)

def say_online(text):
    
    gtts_object = gTTS(text=text)
    set_temp_dir()
    filename = "temp/output2.mp3"
    
    gtts_object.save(filename)
    lol = subprocess.Popen("ffmpeg -i "+filename+" "+filename+".wav", shell=True, stdout=subprocess.PIPE)
    filename = filename + ".wav"
    
    sped_up_sound = AudioSegment.from_file(filename).speedup(1.5, 150, 25)
    
    play(sped_up_sound)
    



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



