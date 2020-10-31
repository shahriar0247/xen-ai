import sys
import os

if __name__ == "__main__":
    os.chdir("app")
    if (sys.argv[1] == "flask"):
        os.system("python flask_server.py")
    elif sys.argv[1] == "cli":
        from app.main import start
        os.system("python main.py")
        start()

