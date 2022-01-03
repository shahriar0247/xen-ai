import say
import gettingtime
from charlie import charlie3
from debug import debug

def talkings(said):
    debug(15)
    if 'time' in said :
        hours, minutes = gettingtime.time()
        say.say("The time is " + hours + " " + minutes)
        
    elif 'date' in said:
        date, month = gettingtime.date()
        say.say("the date is " + date + " of " + month)
    
    elif said == 'who are you':
        say.say("Hello I am zen and i am created by ahmed shah rear")
    
    else:
        charlie(said)

questions_starters = ['who', "what", "when", "why", "how"]

def charlie(said):
    debug(16)

    try:
        if said.startswith("learn"):
            charlie3.train(said.replace("learn", ""))
        elif said.split(" ")[0] in questions_starters:
            debug(17)
            say.say(charlie3.ask(said))
    except:
        pass