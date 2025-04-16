from .activity import Activity

class Chrome(Activity):
    """Chrome class"""
    name = "chrome"

    def __init__(self, handler):
        """init for Chrome"""
        super().__init__()
        self.handler = handler
    
    def run(self):
        """Menjalankan Chrome activity"""
        self.bringWindowToFront(self.name)
