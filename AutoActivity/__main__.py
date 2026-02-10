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
            "TODO: create basic function",
            "TODO: add simple logic",
            "TODO: add more data",
            "TODO: search for bugs",
            "TODO: fix issues",
            "TODO: improve code",
            "TODO: refactor code",
            "TODO: add validation",
            "TODO: handle errors",
            "TODO: update documentation",
            "TODO: write tests",
            "TODO: clean up code",
            "TODO: review code",
            "TODO: simplify process",
            "TODO: check performance",
            "TODO: optimize logic",
            "TODO: update structure",
            "TODO: reorganize files",
            "TODO: remove unused code",
            "TODO: add comments",
            "TODO: test edge cases",
            "TODO: verify results",
            "TODO: update variables",
            "TODO: rename functions",
            "TODO: split large function",
            "TODO: merge similar code",
            "TODO: check dependencies",
            "TODO: update config",
            "TODO: add default values",
            "TODO: improve naming",
            "TODO: check input",
            "TODO: check output",
            "TODO: reduce duplication",
            "TODO: improve readability",
            "TODO: standardize format",
            "TODO: review logic flow",
            "TODO: prepare sample data",
            "TODO: add fallback logic",
            "TODO: improve structure",
            "TODO: finalize changes",
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
            self.mouse.startTimer(10)

            if not self.is_active: break
            self.mouse.switchTab()

            if not self.is_active: break
            self.mouse.startTimer(30)

    def code(self):
        for _ in range(self.randomTabSwitch):
            if not self.is_active: break
            self.mouse.startTimer(10)

            if not self.is_active: break
            self.mouse.switchTab()

            if not self.is_active: break
            self.mouse.startTimer(10)

            if not self.is_active: break
            self.mouse.typeDeleteText(self.sentences)

            if not self.is_active: break
            self.mouse.startTimer(30)

    def start(self, process_name=[]):
        self.process_name = process_name
        Activity.is_active = True
        while self.is_active:
            for app in self.process_name:
                if not self.is_active: break
                self.mouse.startTimer(30)

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
                self.mouse.startTimer(30)

    def stop(self):
        Activity.is_active = False
