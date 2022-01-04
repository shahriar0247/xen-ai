from processing.Direct_Logic.open_program import open_cmd
from processing.Direct_Logic.program_functions import program_functions
from processing.Direct_Logic.search import search
from outputs.debug.debug import debug
import time

from processing.Direct_Logic.talkings import talkings

def do(said):
    debug(time.perf_counter())

    said = (said.lower())
    
    open_cmd(said)
    
    search(said)
    
    program_functions(said)
    
    talkings(said)
