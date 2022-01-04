import os
import sqlite3
import getpass
import subprocess
from inputs.speech_to_text.getvoice import getvoice
import outputs.text_to_speech.say as say
import inflect

ALL_PROGRAM = []
conn = None
cursor = None
p = inflect.engine()

def create_db():
    global conn
    global cursor
    conn = sqlite3.connect("programlist.db")
    cursor = conn.cursor()

def create_table():
    try:
        cursor.execute("""CREATE TABLE program_list (
            program_name text,
            program_loc text

            )""")
    except sqlite3.OperationalError as e:
        cursor.execute("DROP TABLE program_list;")
        cursor.execute("""CREATE TABLE program_list (
            program_name text,
            program_loc text

            )""")

    conn.commit()
    return 

def list_all_files(list_path):
    all_files = []
    for root,folders,files in os.walk(list_path):
        for eachfile in files:
            all_files.append(os.path.join(root,eachfile))
 

    return all_files

def list_main_programs_dir():

    main_folder_applist_with_path = list_all_files(os.environ['WINDIR'] + "\..\ProgramData\Microsoft\Windows\Start Menu\Programs")
    

    main_folder_app_names = []

    for a in main_folder_applist_with_path:
        app_name = a.split("\\")[-1].lower()
        main_folder_app_names.append(app_name)

        cursor.execute("INSERT INTO program_list VALUES ('"+ app_name +"','"+ a +"')")
        conn.commit()

   

def list_user_programs_dir():

    user_folder_applist_with_path = list_all_files("C:/Users/" + getpass.getuser() + "/AppData/Roaming/Microsoft/Windows/Start Menu/Programs")
    

    user_folder_app_names = []

    for a in user_folder_applist_with_path:
        app_name = a.split("\\")[-1].lower()
        user_folder_app_names.append(app_name)

        cursor.execute("INSERT INTO program_list VALUES ('"+ app_name +"','"+ a +"')")
        conn.commit()

   


def get_data_in_array():
    global ALL_PROGRAM
    try:
        ALL_PROGRAM = cursor.execute("SELECT * FROM program_list").fetchall()
    except sqlite3.OperationalError:
        say.say("Program database is empty")
        get_programs_to_db()
        ALL_PROGRAM = cursor.execute("SELECT * FROM program_list").fetchall()
    
   
def get_requested_program_loc(program_name):
    programs_with_same_name = []
    for a in ALL_PROGRAM:
        if program_name in a[0]:
            programs_with_same_name.append([a[0], a[1]])
    return programs_with_same_name

def specify_program(programs_with_same_name):
    if len(programs_with_same_name) == 0:
        say.say("I cant find the application")
        return 0,0
    elif len(programs_with_same_name) == 1:
        open_program(programs_with_same_name[0][0],programs_with_same_name[0][1])
        return 0,0
    else:
        
        a = 0
        c = 0
        programs_to_open = "Which one do you want to open? "
        for b in programs_with_same_name:
            a = a+1
            programs_to_open = programs_to_open + ("number " + str(a)+ " " + b[0].replace(".lnk","") + ", ")

        say.say_process(programs_to_open)
        program_requested = getvoice.getvoice()

        if program_requested.startswith("open "):
            program_requested = program_requested.replace("open ","",1)
           
        return program_requested, programs_with_same_name
       

def open_program(program_name,program_loc):
    program_loc = program_loc.replace("\\","\\\\")
    subprocess.Popen(program_loc, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
    say.say("opening " + program_name.replace(".lnk", ""))
    return "sucess"

numbers = ["1","2","3","4","5","6","7","8","9","0"]

def getting_specified_program(requested, program_list):
    
        
    for program in program_list:
        if requested == program[0].replace(".lnk",""):
            open_program(program[0],program[1])
            return

    for program in program_list:
        if requested in program[0].replace(".lnk",""):
            open_program(program[0],program[1]) 
            return
    
    say.say("failed")

def get_programs_to_db():
    
    say.say("adding programs to database")
    create_db()
    create_table()
    list_main_programs_dir()
    list_user_programs_dir()
    conn.close()
    say.say("programs added to database")


def start_program(program_name):
    create_db()
    get_data_in_array()
    programs_with_same_name = get_requested_program_loc(program_name)
    program_requested, programs_with_same_name = specify_program(programs_with_same_name)
    if program_requested != 0:
        getting_specified_program(program_requested, programs_with_same_name)
