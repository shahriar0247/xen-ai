import say
import gettingtime

def talkings(said):
    if 'time' in said :
        hours, minutes = gettingtime.time()
        say.say("The time is " + hours + " " + minutes)
        
    if 'date' in said:
        date, month = gettingtime.date()
        say.say("the date is " + date + " of " + month)
    
    if said == 'who are you':
        say.say("Hello I am zen and i am created by ahmed shah rear")

  