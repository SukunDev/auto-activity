import pyautogui
import random
from .mouse import Mouse
from .logging import Logger
import time

class Code:
    def __init__(self, sentence = []):
        """Construct form VS Code"""
        self.mouse = Mouse()
        self.log = Logger()
        self.sentence = sentence
        self.tabsSwitchCount = 0
        self.randomTabSwitch = random.randint(1, 4)
        if len(sentence) < 1:
            self.sentence = [
                "TODO: create some function",
                "TODO: create logic",
                "TODO: add some data",
                "TODO: searching some bug",
                "TODO: fixing issue",
            ]

    def __typeDeleteText(self) -> None:
        self.mouse.clickCenterScreen()
        self.log.info("Start Typing on VS Code")
        sentence = random.choice(self.sentence)
        self.log.info(f"Typing Text {sentence}")
        pyautogui.keyDown('ctrl')
        for i in range(random.randint(1,5)):
            pyautogui.press('tab')
            time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', 'end')
        time.sleep(0.5)
        pyautogui.hotkey('enter')
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', '/')
        time.sleep(0.5)
        pyautogui.write(sentence, interval=0.1)
        self.mouse.startTimer(5)
        self.log.info(f"Deleting Text {sentence}")
        time.sleep(0.5)
        pyautogui.press('backspace', presses=len(sentence), interval=0.1)
        time.sleep(0.5)
        pyautogui.hotkey('ctrl', '/')
        time.sleep(0.5)
        pyautogui.hotkey('backspace')
    
    def run(self):
        for i in range(self.randomTabSwitch):
            self.__typeDeleteText()
            self.mouse.startTimer(30)


