from getvoice import getvoice
import say
import gettingtime
import os
from urllib.parse import quote
import subprocess


said = getvoice.getvoice()

#said = input()


global open_success
open_success = False

def listall(list_path):
   
    all_files = []
    for root,folders,files in os.walk(list_path):

        for eachfile in files:
            all_files.append(os.path.join(root,eachfile))
    
 
    return all_files

def listing_app(lol):
    os.chdir("C:\ProgramData\Microsoft\Windows\Start Menu\Programs")
    applist = listall(".")
    applist2 = []
    for a in applist:
        applist2.append(a.split("\\")[-1].lower())


    finding_app(applist, applist2,lol)
        

def finding_app(applist, applist2,lol):
    applist3 = []  
    for a in applist2:
        if lol in a or a in lol:
            applist3.append(a)
    opening_app(applist, applist2,applist3, lol)

    

def opening_app(applist, applist2,applist3, lol):
    
    if len(applist3) == 1:
        cmd = "\"" + applist[applist2.index(applist3[0])].replace(".\\","") + "\""
        subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        global open_success
        open_success = True
        return None
    elif len(applist3) == 0:
        pass 
    else:
        say.say("Which one do you want to open")
        a = 0
        c = 0
        for b in applist3:
            a = a+1
            say.say("number" + str(a) + b.replace(".lnk",""))
        lol =  getvoice.getvoice()
        lol = lol.replace("open ","")
        #lol = input()
        lol = lol.lower()
        finding_app(applist, applist2,lol)


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
            open_success = True
    else:
        if "computer" in said or "pc" in said:
            os.system("explorer ::{20D04FE0-3AEA-1069-A2D8-08002B30309D}")
            open_success = True
        if "document" in said:
            os.system("explorer shell:document")
            open_success = True
        if "download" in said:
            os.system("explorer shell:downloads")
            open_success = True
        if "desktop" in said:
            os.system("explorer shell:Desktop")
            open_success = True
        if "music" in said:
            os.system("explorer shell:Music")
            open_success = True
        if "video" in said:
            os.system("explorer shell:Video")
            open_success = True
       
        listing_app(said.replace("open ","").replace("start ",""))
    if open_success == True:        
        say.say("Opening " + said.replace("open ","").replace("start",""))
    else:
        say.say("I cant find any application named " + said.replace("open ","").replace("start",""))
    

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

