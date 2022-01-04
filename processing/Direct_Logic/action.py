from processing.Direct_Logic.open_program import open_cmd
from processing.Direct_Logic.program_functions import program_functions
from search import search
from talkings import talkings
from output.debug.debug import debug
import time

def do(said):
    debug(time.perf_counter())

    said = (said.lower())
    
    open_cmd(said)
    
    search(said)
    
    program_functions(said)
    
    talkings(said)
