import pyautogui
import random
from .logging import Logger
from .mouse import Mouse

class Chrome:
    def __init__(self):
        """Construct for Chrome class"""
        self.log = Logger()
        self.mouse = Mouse()
        self.tabsSwitchCount = 0
        self.randomTabSwitch = random.randint(1, 4)

    def __switchTab(self):
        self.log.info("Switching Tab Chrome")
        pyautogui.hotkey('ctrl', 'tab')
    
    def run(self):
        for i in range(self.randomTabSwitch):
            self.__switchTab()
            self.mouse.startTimer(30)

    