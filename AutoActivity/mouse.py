from .logging import Logger
import pyautogui
import random
import time


class Mouse:
    def __init__(self):
        """Consruct for Mouse Class"""
        self.log = Logger()

    def __smoothMove(self, x1, y1, x2, y2, duration=1) -> None:
        steps = 50
        for i in range(steps):
            x = x1 + (x2 - x1) * (i / steps)
            y = y1 + (y2 - y1) * (i / steps)
            self.log.info(f"Pos X: {x} Y: {y}")
            pyautogui.moveTo(x, y)
            time.sleep(duration / steps)

    def __randomMouseMove(self) -> None:
        screen_width, screen_height = pyautogui.size()
        random_x = random.randint(0, screen_width)
        random_y = random.randint(0, screen_height)
        current_x, current_y = pyautogui.position()
        self.__smoothMove(current_x, current_y, random_x, random_y, duration=random.uniform(1, 3))

    def __randomScroll(self) -> None:
        scroll_amount = random.randint(-10, 10)
        pyautogui.scroll(scroll_amount)

    def startTimer(self, sleep_time) -> None:
        self.log.info(f"Random Mouse Event {sleep_time} seconds")
        start_time = time.time()
        while time.time() - start_time < sleep_time:
            action = random.choice(['move', 'scroll'])
            
            if action == 'move':
                self.__randomMouseMove()
            elif action == 'scroll':
                self.__randomScroll()
            
            time.sleep(random.uniform(0.5, 2))
    
      
    def clickCenterScreen(self) -> None:
        screen_width, screen_height = pyautogui.size()
        center_x = screen_width / 2
        center_y = screen_height / 2
        self.log.info(f"Click Center Screen")
        pyautogui.click(center_x, center_y)




