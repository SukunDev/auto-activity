from AutoActivity import AutoActivity

# Inisialisasi objek AutoActivity
auto = AutoActivity()

# Menggunakan decorator untuk mendaftarkan handler pesan
@auto.onMessage
def handle_message(message):
    print(f"[Main] Received message: {message}")

# Mulai aktivitas otomatis
auto.start(["chrome", "code"])
