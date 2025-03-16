# activity.py

import pygetwindow as gw
import psutil

class Activity:
    """Activity class"""
    is_active = False
    process = None

    def __init__(self):
        """init for Activity"""

    def isProcessRunning(self, process_name) -> bool:
        """Cek apakah proses berjalan berdasarkan nama"""
        for process in psutil.process_iter(['pid', 'name']):
            try:
                if process_name.lower() in process.info['name'].lower():
                    return True
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return False

    def bringWindowToFront(self, window_title) -> None:
        """Membawa jendela ke depan berdasarkan judulnya"""
        windows = [w for w in gw.getWindowsWithTitle(window_title) if window_title.lower() in w.title.lower()]
        if windows:
            window = windows[0]
            window.activate()
            window.maximize()

    def isProcessOnFront(self, window_title) -> bool:
        """Cek apakah jendela dengan judul tertentu sedang berada di depan (aktif)"""
        active_window = gw.getActiveWindow()
        if active_window and window_title.lower() in active_window.title.lower():
            return True
        return False
