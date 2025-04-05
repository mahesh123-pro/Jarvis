import os
import eel
from engine.features import *
from engine.command import *
from engine.auth import recoganize

def start():
    print("[INFO] Initializing Eel...")
    eel.init("www")

    playAssistantSound()

    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")
        flag = recoganize.AuthenticateFace()
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Failed")

    print("[INFO] Launching Chrome App Mode...")
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    print("[INFO] Jarvis is running. Waiting for browser interaction...")
    eel.start('index.html', mode=None, host='localhost', block=True)

start()
