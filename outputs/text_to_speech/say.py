import win32com.client as wincl
import pythoncom
import time
from pywintypes import com_error
from gtts import gTTS

from outputs.text_to_speech.tensorspeech import inference 
import time
from playsound import playsound
from urllib.request import urlopen, URLError
import pyttsx3
from io import BytesIO
from pydub import AudioSegment
from pydub.playback import play
import socket
import os

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
    say_ai(text)
    #multiprocessing.Process(target=say_process, args=[text]).start()

def say_ai(text):
    start = (time.perf_counter())
    inference(text)
    end = (time.perf_counter())
    print(end-start)
    playsound("temp/audio_after.wav")
    os.remove("temp/audio_after.wav")

def say_process(text):
    

    if internet_on():
        say_online(text)
    else:
        say_offline(text)

def say_online(text):
    gtts_object = gTTS(text=text)
    

    mp3_fp = BytesIO()
    print(time.perf_counter())
    gtts_object.write_to_fp(mp3_fp)    
    print(time.perf_counter())
    mp3_fp.seek(0)
    song = AudioSegment.from_file(mp3_fp, format="mp3")
    
    play(song)    
    





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


def internet_on():
    try:
        ip = socket.gethostbyname('www.google.com')
        return True
    except socket.gaierror:
        return False
    


