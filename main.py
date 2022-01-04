from output.debug.debug import debug
import time
from processing.Direct_Logic.action import do
from input.getvoice import listen
from input.live_transcription import background_listen_2
from speech_recognition import UnknownValueError
import threading

stop_listening = None

def start_listening():
    try:
        listen()
    except UnknownValueError:
        pass

def keep_listening():
    while True:
        try:
            listen()
        except KeyboardInterrupt:
            
            break
        except UnknownValueError:
            pass

def keep_inputing():
    while True:
        try:
            said = input("Write something: ")
            action = threading.Thread(target=do, args=[said]).start()
        except KeyboardInterrupt:
            
            break


def start():
    
    with open("opening", "w") as opening:
        opening.write("false")
    print("started listening")
    
    background_listen_2()


if __name__ == "__main__":
    print('hi')
    debug(time.perf_counter())
    start()
    time.sleep(1000)


