import say
import os
import open_any_program
import time

def open_cmd(said):
    if 'open' in said or "start" in said:
        try:
            open_check(said)
        except:
            time.sleep(1)
            open_check(said)


def open_check(said):
        
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

def open_program(said):
           
            said = said.replace("open ", "")
            said = said.replace("start ", "")
            
            if ".com" in said or " dot com" in said:
                said.replace(" dot com", ".com")
         
                os.system("explorer http://" + said)
                return 

            elif "in" in said:

          
                said = said.replace(".com","")
                said = said.replace("www.","")
                said = said.replace("in", "")
                said = said.replace("browser", "")

                if "chrome" in said:
                    said = said.replace("chrome", "")
                    said = said.replace(" ", "")
                    said = "www." + said + ".com"
                    said = "start chrome " + said
                    os.system(said)
                    
                if "firefox" in said:
                    said = said.replace("firefox", "")
                    said = said.replace(" ", "")
                    said = "www." + said + ".com"
                    said = "start firefox " + said
                    os.system(said)
                
                if "edge" in said:
                    said = said.replace("edge", "")
                    said = said.replace("microsoft", "")
                    said = said.replace(" ", "")
                    said = "https://www." + said + ".com"
                    said = "start microsoft-edge:" + said
                    os.system(said)

                return 

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
            
                return open_any_program.start_program(said)
        
            say.say("I cant find any application named " + said)
  
