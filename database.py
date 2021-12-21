import sqlite3
import gettingtime


conn = sqlite3.connect("commands.db")
c = conn.cursor()



def start():
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS input_output (input text, output text)")
    conn.commit()
    return conn, c

def save(said):
    global conn
    global c
    date = str(gettingtime.date())
    time = str(gettingtime.time())
    c.execute("insert into input_output values (?,?);", (said,  time + " " + date))
    conn.commit()