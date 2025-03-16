# code.py

from .activity import Activity


class Code(Activity):
    """Code class"""
    name = "code"

    def __init__(self, handler):
        """init for Code"""
        super().__init__()
        self.handler = handler
    
    def run(self):
        """Menjalankan Chrome activity"""
        print(self.is_active)
        self.bringWindowToFront(self.name)
    
