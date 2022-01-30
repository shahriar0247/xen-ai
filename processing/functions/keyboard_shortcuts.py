from pynput.keyboard import Key, Controller

keyboard = Controller()

alt_keywords = [
    "south", "olX", "alt", "ox", "hot", "alter", "alt", "Oppo", "author"
]


def shortcut(said):
    control = False
    shift = False
    alt = False
    tab = False
    win_key = False

    if "control" in said:
        control = True
        said = said.replace("control ", "")
        keyboard.press(Key.ctrl)
    if "windows key" in said:
        win_key = True
   
        said = said.replace("windows key ", "")
        print(said)
        keyboard.press(Key.cmd)

    if "shift" in said:
        said = said.replace("shift ", "")
        shift = True
        keyboard.press(Key.shift)

    for a in alt_keywords:
        if a in said:
            said = said.replace(a + " ", "")
            if alt != True:
                keyboard.press(Key.alt)
            alt = True

    if "tab" in said:
        said = said.replace("tab ", "")
        tab = True
        keyboard.press(Key.tab)

    if said[0] == "f":
        keys = [
            Key.f1, Key.f2, Key.f3, Key.f4, Key.f5, Key.f6, Key.f7, Key.f8,
            Key.f9, Key.f10, Key.f11, Key.f12
        ]
        index_of_key = int(said[1]) - 1
        keyboard.press(keys[index_of_key])
        keyboard.release(keys[index_of_key])
        print(keys[index_of_key])
    else:
        keyboard.press(said)
        keyboard.release(said)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release(Key.alt)
    keyboard.release(Key.tab)
    keyboard.release(Key.cmd)
