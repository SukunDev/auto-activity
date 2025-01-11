import pyautogui
import random
from .mouse import Mouse
from .logging import Logger

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
        for i in range(random.randint(1,3)):
            pyautogui.hotkey('ctrl', 'tab', interval=0.1)

            self.mouse.startTimer(1)

        pyautogui.hotkey('ctrl', 'end')
        pyautogui.hotkey('enter')
        pyautogui.hotkey('ctrl', '/')
        pyautogui.write(sentence, interval=0.1)
        self.mouse.startTimer(5)
        self.log.info(f"Deleting Text {sentence}")
        pyautogui.press('backspace', presses=len(sentence), interval=0.1)
        pyautogui.hotkey('ctrl', '/')
        pyautogui.hotkey('backspace')
    
    def run(self):
        for i in range(self.randomTabSwitch):
            self.__typeDeleteText()
            self.mouse.startTimer(30)


