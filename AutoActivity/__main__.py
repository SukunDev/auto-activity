import pygetwindow as gw
import pyautogui
import psutil
import sys
import keyboard
import time
import threading

from .mouse import Mouse
from .logging import Logger
from .chrome import Chrome
from .code import Code
from .config import *

class AutoActivity:
    TrackerTime = 0
    def __init__(self, process_name = []):
        """constructor Auto Activity"""
        self.mouse = Mouse()
        self.log = Logger()
        self.chrome = Chrome()
        self.code = Code()
        self.process_name = process_name
        if len(process_name) < 1:
            self.process_name = ["chrome", "code"]

        for process in self.process_name:
            if not self.__isProcessRunning(process):
                self.log.error(f"Please Open {process} Before running this script")
                sys.exit()
                break
            if process not in PROCESS_LIST:
                self.log.error(f"Currently not support your proccess")
                sys.exit()

    def __isProcessRunning(self, process_name) -> bool:
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if process_name.lower() in process.info['name'].lower():
                    self.log.info(f"Proccess {process_name} is running")
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False
    
    def __bringWindowToFront(self, window_title) -> None:
        windows = [w for w in gw.getWindowsWithTitle(window_title) if window_title.lower() in w.title.lower()]
        if windows:
            self.log.info(f"Activate Process {window_title}")
            window = windows[0]
            window.activate()
            window.maximize()

    def wait_for_keypress(self):
        """Wait for F5 key press to start and F6 to stop"""
        self.log.info("Press F5 to start...")
        keyboard.wait('F5')  # Wait for F5 key press
        self.log.info("F5 pressed. Starting AutoActivity...")


    def stop(self):
        time.sleep(AutoActivity.TrackerTime * 60)
        pyautogui.hotkey('ctrl', 'alt', '[')

    def run(self):
        AutoActivity.TrackerTime = input("Masukkan waktu dalam menit: ")
        AutoActivity.TrackerTime = int(AutoActivity.TrackerTime)


        self.wait_for_keypress()  # Wait for F5 key press to begin
        key_thread = threading.Thread(target=self.stop, daemon=True)
        key_thread.start()

        self.mouse.startTimer(15)
        isLoop = True
        while isLoop:
            # Check for F6 press to stop immediately
            if keyboard.is_pressed('F6'):
                self.log.info("F6 pressed. Stopping AutoActivity...")
                isLoop = False
                break

            for process in self.process_name:
                # Check for F6 press before each process execution
                if keyboard.is_pressed('F6'):
                    self.log.info("F6 pressed. Stopping AutoActivity...")
                    isLoop = False
                    break

                self.__bringWindowToFront(process)
                if process == "chrome":
                    self.chrome.run()
                elif process == "code":
                    self.code.run()
