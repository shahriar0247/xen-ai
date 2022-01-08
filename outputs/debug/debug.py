def debug(text, type=None):
    if type == "init":
        print("--- Init: " + text + " ---")
    if type == "said":
        print("/////////// " + text + " ///////////")
    print(text)
