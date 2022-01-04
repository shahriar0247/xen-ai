import sqlite3
import processing.Direct_Logic.gettingtime as gettingtime


conn = sqlite3.connect("commands.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS input_output (input text, output text)")
conn.close()


def start():
    conn = sqlite3.connect("commands.db")
    c = conn.cursor()
    return conn, c

def save(said):
    conn,c = start()
    date = str(gettingtime.date())
    time = str(gettingtime.time())
    c.execute("insert into input_output values (?,?);", (said,  time + " " + date))
    conn.commit()
    conn.close()