import keyboard
import os
import tkinter as tk
from tkinter import scrolledtext
import time
import threading
from AutoActivity import AutoActivity

auto = AutoActivity()
running = False
start_time = 0
selected_apps = {}

def update_timer():
    """Update tampilan timer setiap detik."""
    global start_time, running
    while running:
        elapsed_time = int(time.time() - start_time)
        minutes = elapsed_time // 60
        seconds = elapsed_time % 60
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        time.sleep(1)

def log_message(message):
    """Menambahkan log ke dalam UI."""
    log_text.config(state=tk.NORMAL)
    log_text.insert(tk.END, message + "\n")
    log_text.config(state=tk.DISABLED)
    log_text.yview(tk.END)

def handle_message(message):
    """Handler pesan dari AutoActivity."""
    root.after(0, lambda: log_message(message))  # Pastikan berjalan di thread utama

# Pastikan event listener terhubung sekali saat inisialisasi
auto.onMessage(handle_message)

def start_program():
    """Memulai subprocess dan timer."""
    global running, start_time
    if running:
        return  # Hindari memulai program lebih dari sekali
    
    apps = [app for app in selected_apps if selected_apps[app].get()]
    if not apps:
        log_message("Setidaknya Anda harus memilih satu program.")
        return
    
    log_message("Program dimulai.")
    running = True
    start_time = time.time()
    threading.Thread(target=update_timer, daemon=True).start()
    
    auto.start(apps)

def stop_program():
    """Menghentikan proses dan reset timer."""
    global running
    if not running:
        return  # Hindari menghentikan jika tidak berjalan
    
    auto.stop()
    running = False
    timer_label.config(text="00:00")
    log_message("Program dihentikan.")

# Setup UI
root = tk.Tk()
root.title("Program Control")
root.geometry("350x550")

# Timer Label
timer_label = tk.Label(root, text="00:00", font=("Arial", 20))
timer_label.pack(pady=10)

# Tombol Start & Stop
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

start_button = tk.Button(button_frame, text="Start / F5", command=start_program, width=10)
start_button.pack(side=tk.LEFT, padx=5)

stop_button = tk.Button(button_frame, text="Stop / F6", command=stop_program, width=10)
stop_button.pack(side=tk.RIGHT, padx=5)

# Checkbox untuk aplikasi
checkbox_frame = tk.LabelFrame(root, text="Pilih Aplikasi yang akan dibuka:")
checkbox_frame.pack(padx=10, pady=10, fill=tk.BOTH)

selected_apps['chrome'] = tk.BooleanVar()
selected_apps['figma'] = tk.BooleanVar()
selected_apps['vscode'] = tk.BooleanVar()

chrome_checkbox = tk.Checkbutton(checkbox_frame, text="Google Chrome", variable=selected_apps['chrome'])
chrome_checkbox.pack(anchor='w')

figma_checkbox = tk.Checkbutton(checkbox_frame, text="Figma", variable=selected_apps['figma'])
figma_checkbox.pack(anchor='w')

vscode_checkbox = tk.Checkbutton(checkbox_frame, text="VS Code", variable=selected_apps['vscode'])
vscode_checkbox.pack(anchor='w')

# Log Area
log_text = scrolledtext.ScrolledText(root, height=5, state=tk.DISABLED)
log_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Bind keyboard hotkeys
keyboard.add_hotkey("F5", start_program)
keyboard.add_hotkey("F6", stop_program)

# Jalankan aplikasi
root.mainloop()