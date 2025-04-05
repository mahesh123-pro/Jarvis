import os
import subprocess
import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize

def start():
    eel.init("www")
    playAssistantSound()

    @eel.expose
    def init():
        print("[DEBUG] JS called init()")
        
        # Launch ADB device connection
        try:
            subprocess.call([r'device.bat'])
        except Exception as e:
            print("[ERROR] device.bat failed:", e)
        
        eel.hideLoader()
        speak("Ready for Face Authentication")

        flag = recoganize.AuthenticateFace()
        print(f"[DEBUG] Face authentication flag: {flag}")

        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I Help You")
            eel.hideStart()
            playAssistantSound()

            # Start listening for voice commands
            while True:
                command = takeCommand()
                print("You said:", command)

                if command is None:
                    speak("I didn't catch that. Please say it again.")
                    continue

                if 'exit' in command or 'quit' in command:
                    speak("Goodbye Sir!")
                    break
                else:
                    executeCommand(command)  # Custom function you define

        else:
            speak("Face Authentication Failed")
            print("[DEBUG] Authentication failed.")

    print("[INFO] Launching Chrome App Mode...")
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    print("[INFO] Jarvis is running. Waiting for browser interaction...")
    eel.start('index.html', mode=None, host='localhost', block=True)

start()
