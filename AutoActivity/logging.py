import logging

class Logger:
    def __init__(self, log_file='activity.log', level=logging.DEBUG):
        # Menyiapkan format log dan handler
        self.logger = logging.getLogger(__name__)

        # Cek jika handler sudah ada
        if not self.logger.hasHandlers():
            self.logger.setLevel(level)

            # Membuat formatter untuk log
            log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            formatter = logging.Formatter(log_format)

            # Membuat file handler untuk menyimpan log ke file
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            # Membuat console handler untuk menampilkan log di konsol
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            # Menambahkan handler ke logger
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
