from outputs.debug.debug import debug

sf, tf, TFAutoModel, AutoProcessor = [None, None, None, None]


def init_speech():
    global sf
    global tf
    global TFAutoModel
    global AutoProcessor
    import soundfile as sf
    import tensorflow as tf
    from tensorflow_tts.inference import TFAutoModel
    from tensorflow_tts.inference import AutoProcessor

    global fastspeech2
    global mb_melgan
    global processor
    # initialize fastspeech2 model.
    fastspeech2 = TFAutoModel.from_pretrained(
        "tensorspeech/tts-fastspeech2-ljspeech-en")

    # initialize mb_melgan model
    mb_melgan = TFAutoModel.from_pretrained(
        "tensorspeech/tts-mb_melgan-ljspeech-en")

    # inference
    processor = AutoProcessor.from_pretrained(
        "tensorspeech/tts-fastspeech2-ljspeech-en")
    inference("Hello sir")
    debug("Speech", "init")


def inference(text):
    input_ids = processor.text_to_sequence(text)
    # fastspeech inference

    mel_before, mel_after, duration_outputs, _, _ = fastspeech2.inference(
        input_ids=tf.expand_dims(
            tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
        speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
        speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
        f0_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
        energy_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
    )

    # melgan inference
    audio_before = mb_melgan.inference(mel_before)[0, :, 0]
    audio_after = mb_melgan.inference(mel_after)[0, :, 0]
    print(type(audio_after))
    # save to file

    sf.write('./temp/audio_before.wav', audio_before, 22050, "PCM_16")
    sf.write('./temp/audio_after.wav', audio_after, 22050, "PCM_16")
    return './temp/audio_after.wav'
