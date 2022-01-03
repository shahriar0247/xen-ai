import sys
import os
from flask import Flask, render_template, request
import main
import threading
import time
import multiprocessing


if getattr(sys, 'frozen', False):

    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')

    debug(template_folder)
    debug(static_folder)

    app = Flask(__name__, template_folder=template_folder,
                static_folder=static_folder)
else:
    app = Flask(__name__)


with open("threadon", "w") as a:
    a.write("false")
with open("listening", "w") as a:
    a.write("false")
with open("opening", "w") as a:
    a.write("false")



def listen_properly():
    while True:
        time.sleep(1/10)
        with open("listening", "r") as a:
            if a.read() == "true":
                main.start_listening()
            else:
                pass


@app.route('/', methods=['POST', "GET"])
def flasking():
    if request.method == "GET":
        threadon = open("threadon", "r")
        if threadon.read() == "false":
            threading.Thread(target=listen_properly).start()
            threadon.close()
            threadon = open("threadon", "w+")
            threadon.writelines("true")
            threadon.close()
            debug("starting thread")
            return render_template("main.html", listening="false")
    else:
        will_listen = request.form['listen_form_text']
        if (will_listen == "Start listening"):
            debug("Lol")
            with open("listening", "w") as a:
                a.write("true")
            listening = "true"
        else:
            debug("22")
            with open("listening", "w") as a:
                a.write("false")
            listening = "false"
        debug(listening)
        return render_template("main.html", listening=listening)


def start_flask_server():
    app.run(host='127.0.0.1', port=5000, debug=True)


if __name__ == "__main__":
    start_flask_server()
