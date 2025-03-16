# handler.py

from .activity import Activity


class Handler(Activity):
    """Handler class"""

    def __init__(self):
        """init for Handler"""
        super().__init__()
        self._on_message_handler = None

    def handler(self, message):
        if self._on_message_handler:
            self._on_message_handler(message)
        else:
            raise Exception("No message handler registered")

    def onMessage(self, func):
        def wrapper(event):
            func(event)

        self._on_message_handler = wrapper
        return wrapper