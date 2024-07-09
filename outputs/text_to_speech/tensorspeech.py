import torch
from TTS.api import TTS

def init_speech():
    print('failed')
    global tts
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device) 
    print(TTS().list_models())
    print('success')


def inference(text):

    output_path = "./temp/audio_output.wav"
    tts.tts_to_file(text=text,
                file_path="output.wav",
                speaker_wav="/path/to/target/speaker.wav",
                language="en")
    wav = tts.tts(text="Hello world!", speaker_wav=output_path, language="en")

    return output_path  




