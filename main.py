from inputs.speech_to_text.getvoice import listen
from inputs.speech_to_text.live_transcription import background_listen_2
from outputs.debug.debug import debug
import time
from outputs.text_to_speech.tensorspeech import init_speech
from processing.functions.action import do
from speech_recognition import UnknownValueError
import threading

from processing.QA_Pipeline.transformers import init_qa_pipeline

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


def init_items_thread():
    threading.Thread(target=init_speech).start()
    threading.Thread(target=init_qa_pipeline).start()
    print("Imported Everything")


if __name__ == "__main__":
    debug(time.perf_counter())
    init_items_thread()
    start()
    time.sleep(1000)
