import speech_recognition as sr
import set_up_db
class getvoice:
    def getvoice():
        
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Say Something")
            audio = r.listen(source)

        said = r.recognize_google(audio)
        said = said.lower()
        print(said)
        conn, c = set_up_db.start()
       
        c.execute("insert into input_output values ('"+said+"',\"lol\");")
        conn.commit()
        return said
