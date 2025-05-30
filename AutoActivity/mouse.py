# mouse.py

from .activity import Activity
import pyautogui
import random
import time


class Mouse(Activity):
    """Mouse class"""

    def __init__(self, handler):
        """init for Mouse"""
        super().__init__()
        self.handler = handler

    def __smoothMove(self, x1, y1, x2, y2, duration=1) -> None:
        steps = 50  # lebih banyak step
        for i in range(steps):
            if not self.is_active: return
            t = i / steps
            # Interpolasi halus dengan easing (linear → bisa diganti)
            x = x1 + (x2 - x1) * t
            y = y1 + (y2 - y1) * t
            pyautogui.moveTo(x, y)
            time.sleep(duration / steps)

    def __randomMouseMove(self) -> None:
        if not self.is_active: return
        screen_width, screen_height = pyautogui.size()
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_height)
        current_x, current_y = pyautogui.position()
        self.__smoothMove(current_x, current_y, random_x, random_y, duration=random.uniform(0.01, 0.3))

    def __randomScroll(self) -> None:
        if not self.is_active: return
        scroll_amount = random.randint(-500, 500)
        pyautogui.scroll(scroll_amount)

    def __safeSleep(self, duration):
        """Sleep pendek yang bisa dibatalkan dengan stop()"""
        end_time = time.time() + duration
        while time.time() < end_time:
            if not self.is_active:
                break
            time.sleep(0.1)

    def startTimer(self, sleep_time) -> None:
        self.handler.handler(f"Random Mouse Event {sleep_time} seconds")
        start_time = time.time()
        while time.time() - start_time < sleep_time and self.is_active:
            action = random.choice(['move', 'scroll'])

            if action == 'move':
                self.__randomMouseMove()
            elif action == 'scroll':
                self.__randomScroll()

            self.__safeSleep(random.uniform(0.5, 2))

    def clickCenterScreen(self) -> None:
        if not self.is_active: return
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width / 2
        center_y = screen_height / 2
        self.handler.handler(f"Click Center Screen")
        pyautogui.click(center_x, center_y)

    def switchTab(self):
        if not self.is_active: return
        pyautogui.keyDown('ctrl')
        for i in range(random.randint(1, 5)):
            if not self.is_active: break
            pyautogui.press('tab')
            self.__safeSleep(0.1)
        pyautogui.keyUp('ctrl')

    def typeDeleteText(self, sentences) -> None:
        if not self.is_active: return
        self.clickCenterScreen()
        self.handler.handler("Start Typing on VS Code")
        sentence = random.choice(sentences)
        self.handler.handler(f"Typing Text {sentence}")

        self.__safeSleep(0.5)
        pyautogui.hotkey('ctrl', 'end')
        self.__safeSleep(0.5)
        pyautogui.hotkey('enter')
        self.__safeSleep(0.5)
        pyautogui.hotkey('ctrl', '/')
        self.__safeSleep(0.5)

        if not self.is_active: return
        pyautogui.write(sentence, interval=0.1)
        self.startTimer(5)

        if not self.is_active: return
        self.handler.handler(f"Deleting Text {sentence}")
        self.__safeSleep(0.5)
        pyautogui.press('backspace', presses=len(sentence), interval=0.1)
        self.__safeSleep(0.5)
        pyautogui.hotkey('ctrl', '/')
        self.__safeSleep(0.5)
        pyautogui.hotkey('backspace')
        self.__safeSleep(0.5)
        pyautogui.hotkey('ctrl', 'home')
    
    def stopUpworkTimeTracker(self):
        pyautogui.hotkey('ctrl', 'alt', '[')
