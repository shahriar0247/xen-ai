from getvoice import getvoice
import say
import gettingtime
import os
from urllib.parse import quote

said = getvoice.getvoice()
#said = input()



if 'open' in said or "start" in said:
    
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
    else:
        if "computer" in said or "pc" in said:
            os.system("explorer ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
        if "document" in said:
            os.system("explorer shell:document")
        if "download" in said:
            os.system("explorer shell:downloads")
        if "desktop" in said:
            os.system("explorer shell:Desktop")
        if "music" in said:
            os.system("explorer shell:Music")
        if "video" in said:
            os.system("explorer shell:Video")
        if "chrome" in said:
            os.system("start chrome")
        if "firefox" in said:
            os.system("start firefox")
        if "control panal" in said:
            os.system("control")
            
    say.say("Opening " + said.replace("open ",""))

    
    




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
       
        search_for = search_for.replace("in%20google", "", 1)
        search_for = search_for.replace("google", "", 1)
        os.system("start https://www.google.com/search?q=" + search_for)
    elif "bing" in said:
        search_for = search_for.replace("in%20bing", "", 1)
        search_for = search_for.replace("bing", "", 1)
        os.system("start https://www.bing.com/search?q=" + search_for)
    print(search_for)
