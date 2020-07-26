<h2> Xen AI </h2>

<h3> Features </h3>
<ol>
<li>Open any program in start menu except for windows 10 applications
</li>
<li>Open "stackoverflow" in chrome (to open stackoverflow.com in chrome/firefox)</li>
<li>Supports more then one command at a time</li>
<li> Ask for date and time </li>
</ol>
<h3> Requirements </h3>

<ol>
<li>Windows 7 and above (tested only on Windows 10 tell me about others)</li>
<li>Tested on python 3.6 and 3.6.8 (may support any python 3.6). Doesnt support python 3.7 and above due to modules</li>
<li>Need python modules <ul> <li>pyttsx3=2.71 (newer versions of pyttsx was not installing for unknown reason)</li>
<li>pywin32</li>
<li>SpeechRecognition</li>
  <li>PyAudio</li>
  <li>Flask</li>
</ul>
<p>Run requirements.bat file to automatically install modules with pip</p>
</ol>
<h3> Installation </h3>

<ol>
<li>Run the flask_server.py file with "python flask_server.py" or "python3.6 flask_server.py"</li>
</ol>

<h3> Note </h3>
<p> If you just want to run the python file without flask/gui (webserver), add "keep_listening()" function at the bottom of "main.py" file and run the "main.py" file </p>
