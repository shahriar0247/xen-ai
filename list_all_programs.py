from getvoice import getvoice
import subprocess
import os
import say


def listall(list_path):
    all_folders = []
    all_files = []
    for root,folders,files in os.walk(list_path):

        for eachfile in files:
            all_files.append(os.path.join(root,eachfile))
    
 
    print(all_files)

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
        os.system("\"" + applist[applist2.index(applist3[0])].replace(".\\","") + "\"")
    elif len(applist3) == 0:
        say.say("I cant find any application named " + lol)
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


#lol =  getvoice.getvoice()
#lol = lol.replace("open ","")
#lol = input()
#lol = lol.lower()

#listing_app(lol)
listall("test")       

     
   