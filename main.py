from getvoice import getvoice
import say
import gettingtime
import os
from urllib.parse import quote
import subprocess
import getpass
import open_any_program
from speech_recognition import UnknownValueError
import threading
import multiprocessing
import terminate_program


def open_program(said):
            say.say("Okay")
            if "in" in said:
                said1 = said.replace("open", "")
                if "and" in said1:
                    said1 = said1.split("and")
                
                    
                else:
                    said1 = [said1, "empty"]
                i = 0
                while i < len(said1):
                    said1[i] = said1[i].replace(".com","")
                    said1[i] = said1[i].replace("www.","")
                    if "chrome" in said1[i]:
                        said1[i] = said1[i].replace("chrome", "")
                        said1[i] = said1[i].replace("in", "")
                        said1[i] = said1[i].replace("browser", "")
                        said1[i] = said1[i].replace(" ", "")
                        said1[i] = "www." + said1[i] + ".com"
                        said1[i] = "start chrome " + said1[i]
                        os.system(said1[i])
                        
                    if "firefox" in said1[i]:
                        said1[i] = said1[i].replace("firefox", "")
                        said1[i] = said1[i].replace("in", "")
                        said1[i] = said1[i].replace("browser", "")
                        said1[i] = said1[i].replace(" ", "")
                        said1[i] = "www." + said1[i] + ".com"
                        said1[i] = "start firefox " + said1[i]
                        os.system(said1[i])
                    
                    if "edge" in said1[i]:
                        said1[i] = said1[i].replace("edge", "")
                        said1[i] = said1[i].replace("microsoft", "")
                        said1[i] = said1[i].replace("in", "")
                        said1[i] = said1[i].replace("browser", "")
                        said1[i] = said1[i].replace(" ", "")
                        said1[i] = "https://www." + said1[i] + ".com"
                        said1[i] = "start microsoft-edge:" + said1[i]
                        os.system(said1[i])
                    i = i + 1
                    return "sucess"
            else:
                if "computer" in said or "pc" in said:
                    os.system("explorer ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
                    return "sucess"
                if "document" in said:
                    os.system("explorer shell:document")
                    return "sucess"
                if "download" in said:
                    os.system("explorer shell:downloads")
                    return "sucess"
                if "desktop" in said:
                    os.system("explorer shell:Desktop")
                    return "sucess"
                if "music" in said:
                    os.system("explorer shell:Music")
                    return "sucess"
                if "video" in said:
                    os.system("explorer shell:Video")
                    return "sucess"
            
                return open_any_program.start_program(said.replace("open ",""))
        
            say.say("I cant find any application named " + said.replace("open ","") + ". Do you want reset the program database")
        



def do(said):
    if 'open' in said:
        try:
            opening = open("opening", "r")
            if opening.read() == "true":
                opening.close()
                return
            else:
                opening.close()
                opening = open("opening", "w")
                opening.write("true")
                opening.close()
                open_program(said)
                opening = open("opening", "w")
                opening.write("false")
                opening.close()
                
                
        except:
            open_program(said)


    if said == 'who are you':
        say.say("Hello I am zen and i am created by ahmed shah rear")

    if 'time' in said :
        hours, minutes = gettingtime.time()
        say.say("The time is " + hours + " " + minutes)
    if 'date' in said:
        date, month = gettingtime.date()
        say.say("the date is " + date + " of " + month)

    if 'search' in said:
        search_for = said.split("search ")[1]
        if search_for[:3] == "for":
            search_for = search_for.replace("for","",1)

        search_for = quote(search_for)
        if "google" in said:
            search_for = search_for.replace("in%20google%20", "", 1)
            search_for = search_for.replace("google%20", "", 1)
            if search_for.startswith("for%20"):
                search_for = search_for.replace("for%20", "", 1)
            os.system("start https://www.google.com/search?q=" + search_for)
        elif "bing" in said:
            search_for = search_for.replace("in%20bing%20", "", 1)
            search_for = search_for.replace("bing%20", "", 1)
            if search_for.startswith("for%20"):
                search_for = search_for.replace("for%20", "", 1)
            os.system("start https://www.bing.com/search?q=" + search_for)
        elif "yahoo" in said:
            search_for = search_for.replace("in%20yahoo%20", "", 1)
            search_for = search_for.replace("yahoo%20", "", 1)
            if search_for.startswith("for%20"):
                search_for = search_for.replace("for%20", "", 1)
            os.system("start https://search.yahoo.com/search?p=" + search_for)
    if said.startswith("terminate"):
        terminate_program.terminate(said.replace("terminate",""))
    if said == "get all programs":
        open_any_program.get_programs_to_db()


def listen():
    said = getvoice.getvoice()
    action = threading.Thread(target=do, args=[said])
    action.start()

def listen_for_flask():
    said = getvoice.getvoice()

    try:
        try:
            with open("listening", "r") as a:
                if a.read() == "true":
                    action = threading.Thread(target=do, args=[said])
                    action.start()
        except FileNotFoundError as e:
            action = threading.Thread(target=do, args=[said])
            action.start()
    except UnknownValueError:
        print("Unknown Value Error")
    
   

def start_listening():
    try:
        listen()
    except UnknownValueError:
        print("Unknown Value Error")

def keep_listening():
    while True:
        try:
            listen()
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
            break
        except UnknownValueError:
            print("Unknown Value Error")

if __name__ == "__main__":
    keep_listening()

     


