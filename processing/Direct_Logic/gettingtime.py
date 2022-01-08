import datetime


def time():
    time = datetime.datetime.now().time()
    hours, minutes = time.hour, time.minute
    minutes = str(minutes)
    if hours > 12:
        hours = hours - 12
        minutes = minutes + " P M"
    else:
        minutes = minutes + " A M"
    hours = str(hours)
    return hours, minutes


def date():
    mydate = datetime.datetime.now()
    date = mydate.strftime('%d')
    month = mydate.strftime("%B")
    date = str(date)

    return date, month