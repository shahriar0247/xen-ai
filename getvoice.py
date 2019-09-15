
def getvoice():
    import speech_recognition as sr    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

    said = r.recognize_google(audio)
    said = said.lower()
    return said
