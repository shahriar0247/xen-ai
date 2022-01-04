import outputs.text_to_speech.say as say
import processing.Direct_Logic.gettingtime as gettingtime
# from charlie import charlie3

def talkings(said):
    
    if 'time' in said :
        hours, minutes = gettingtime.time()
        say.say("The time is " + hours + " " + minutes)
        
    elif 'date' in said:
        date, month = gettingtime.date()
        say.say("the date is " + date + " of " + month)
    
    elif said == 'who are you':
        say.say("Hello I am zen and i am created by ahmed shah rear")
    
    else:
        pass
        # charlie(said)

questions_starters = ['who', "what", "when", "why", "how"]

# def charlie(said):
    

#     try:
#         if said.startswith("learn"):
#             charlie3.train(said.replace("learn", ""))
#         elif said.split(" ")[0] in questions_starters:
            
#             say.say(charlie3.ask(said))
#     except:
#         pass