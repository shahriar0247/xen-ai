import outputs.text_to_speech.say as say
import processing.Direct_Logic.gettingtime as gettingtime
from processing.QA_Pipeline.transformers import ask, train


def talkings(said):

    if 'time' in said:
        hours, minutes = gettingtime.time()
        say.say("The time is " + hours + " " + minutes)

    elif 'date' in said:
        date, month = gettingtime.date()
        say.say("the date is " + date + " of " + month)

    elif said == 'who are you':
        say.say("Hello I am zen and i am created by ahmed shah rear")

    else:
        pass
        qa_(said)


questions_starters = ['who', "what", "when", "why", "how"]


def qa_(said):

    try:
        if said.startswith("learn"):
            train(said.replace("learn", ""))
        elif said.split(" ")[0] in questions_starters:

            say.say(ask(said))
    except:
        pass