import sqlite3

def start():
    conn = sqlite3.connect("commands.db")
    c = conn.cursor()

    c.execute("CREATE TABLE IF NOT EXISTS input_output (input text, output text)")
    
    conn.commit()
    return conn, c