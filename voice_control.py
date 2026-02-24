import speech_recognition as sr
import pyautogui
import os
import time


class VoiceController:

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.running = True
        self.command = ""   # ✅ VERY IMPORTANT (Fix)

        self.languages = ["en-IN", "hi-IN", "te-IN"]

    # =====================================
    # LISTEN FUNCTION
    # =====================================
    def listen(self):
        print("🎤 Multilingual Voice Assistant Started")

        while self.running:
            try:
                with self.microphone as source:
                    self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                    print("Listening...")
                    audio = self.recognizer.listen(source)

                text = self.recognize_multilingual(audio)

                if text:
                    self.command = text.lower()   # ✅ STORE COMMAND
                    print("You said:", self.command)

                    self.execute(self.command)

            except:
                continue

    # =====================================
    # MULTI LANGUAGE RECOGNITION
    # =====================================
    def recognize_multilingual(self, audio):
        for lang in self.languages:
            try:
                return self.recognizer.recognize_google(audio, language=lang)
            except:
                continue
        return None

    # =====================================
    # EXECUTION ENGINE
    # =====================================
    def execute(self, command):

        # -------- OPEN APPS --------
        if "open chrome" in command:
            os.system("start chrome")

        elif "open vs code" in command:
            os.system("code")

        elif "open notepad" in command:
            os.system("start notepad")

        # -------- VS CODE --------
        elif "open new terminal" in command:
            pyautogui.hotkey("ctrl", "`")

        # -------- MOUSE --------
        elif "click" in command:
            pyautogui.click()

        elif "double click" in command:
            pyautogui.doubleClick()

        elif "scroll up" in command:
            pyautogui.scroll(500)

        elif "scroll down" in command:
            pyautogui.scroll(-500)

        # -------- SCREENSHOT --------
        elif "screenshot" in command:
            filename = f"screenshot_{int(time.time())}.png"
            pyautogui.screenshot(filename)
            print("Screenshot saved:", filename)

        elif "stop assistant" in command:
            self.running = False

    def stop(self):
        self.running = False
