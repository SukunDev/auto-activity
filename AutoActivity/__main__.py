# __main__.py

import random
from .chrome import Chrome
from .code import Code
from .handler import Handler
from .mouse import Mouse
from .activity import Activity

class AutoActivity(Activity):
    """AutoActivity class"""

    def __init__(self):
        """init for AutoActivity"""
        super().__init__()
        self.handler = Handler()
        self.__chrome = Chrome(self.handler)
        self.__code = Code(self.handler)
        self.mouse = Mouse(self.handler)
        self.callback = None

        self.handler.onMessage(self.onMessageHandler)
        self.process_name = []
        self.randomTabSwitch = random.randint(1, 5)
        self.sentences = [
            "TODO: create some function",
            "TODO: create logic",
            "TODO: add some data",
            "TODO: searching some bug",
            "TODO: fixing issue",
        ]

    def onMessageHandler(self, message):
        """Callback internal untuk menangani pesan masuk"""
        if self.callback:
            self.callback(message)
        else:
            print(f"[Default] Received message: {message}")

    def onMessage(self, func):
        """Decorator untuk mendaftarkan callback"""
        self.callback = func
        return func

    def chrome(self):
        for _ in range(self.randomTabSwitch):
            if not self.is_active: break
            self.mouse.startTimer(2)

            if not self.is_active: break
            self.mouse.switchTab()

            if not self.is_active: break
            self.mouse.startTimer(10)

    def code(self):
        for _ in range(self.randomTabSwitch):
            if not self.is_active: break
            self.mouse.startTimer(2)

            if not self.is_active: break
            self.mouse.switchTab()

            if not self.is_active: break
            self.mouse.startTimer(2)

            if not self.is_active: break
            self.mouse.typeDeleteText(self.sentences)

            if not self.is_active: break
            self.mouse.startTimer(10)

    def start(self, process_name=[]):
        self.process_name = process_name
        Activity.is_active = True
        while self.is_active:
            for app in self.process_name:
                if not self.is_active: break
                self.mouse.startTimer(10)

                if not self.is_active: break
                if self.isProcessOnFront(app):
                    if app == "chrome":
                        self.chrome()
                    elif app == "code":
                        self.code()
                else:
                    if not self.is_active: break
                    if app == "chrome":
                        self.__chrome.run()
                        self.chrome()
                    elif app == "code":
                        self.__code.run()
                        self.code()

                if not self.is_active: break
                self.mouse.startTimer(10)

    def stop(self):
        Activity.is_active = False
