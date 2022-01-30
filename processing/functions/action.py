from outputs.debug.debug import debug
import time

from processing.Direct_Logic.talkings import talkings
from processing.functions.keyboard_shortcuts import shortcut
from processing.functions.open_program import open_cmd
from processing.functions.program_functions import program_functions
from processing.functions.search import search
from processing.functions.keyboard_shortcuts import alt_keywords

hotkey_hotword = alt_keywords
hotkey_hotword.append("control")
hotkey_hotword.append("shift")
hotkey_hotword.append("windows key")


def do(said):
    said = (said.lower())
    debug(time.perf_counter())

    if any(ext in said for ext in hotkey_hotword):
        shortcut(said)

    open_cmd(said)

    search(said)

    program_functions(said)

    talkings(said)
