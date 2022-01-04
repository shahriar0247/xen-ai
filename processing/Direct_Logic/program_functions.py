import processing.Direct_Logic.terminate_program as terminate_program
import processing.Direct_Logic.open_any_program as open_any_program

def program_functions(said):
    if said == "get all programs":
        open_any_program.get_programs_to_db()
    if said.startswith("terminate"):
        terminate_program.terminate(said.replace("terminate",""))
    if said == "restart yourself":
        pass