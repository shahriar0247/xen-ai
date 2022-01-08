import sqlite3
import datetime

conn = sqlite3.connect("database/commands.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS input_output (input text, output text)")
conn.close()


def start():
    conn = sqlite3.connect("database/commands.db")
    c = conn.cursor()
    return conn, c


def save(said):
    conn, c = start()
    c.execute("insert into input_output values (?,?);",
              (said, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")))
    conn.commit()
    conn.close()