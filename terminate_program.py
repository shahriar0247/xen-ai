import os
# import psutil

# for proc in psutil.process_iter():
#     try:
#         # Get process name & pid from process object.
#         processName = proc.name()
#         processID = proc.pid
#         debug(processName , processID)
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass

def terminate(program_name):
    os.system("taskkill /f /im" + program_name + ".exe")
