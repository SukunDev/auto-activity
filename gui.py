import tkinter as tk
from tkinter import scrolledtext, messagebox, ttk
from AutoActivity import AutoActivity
import threading
import time
import os
import platform

auto = AutoActivity()

@auto.onMessage
def handle_message(message):
    log_message(f"[Main] {message}")

def log_message(msg):
    log_text.config(state='normal')
    log_text.insert(tk.END, msg + "\n")
    log_text.yview(tk.END)
    log_text.config(state='disabled')

def get_selected_apps():
    apps = []
    if chrome_var.get():
        apps.append("chrome")
    if vscode_var.get():
        apps.append("code")
    return apps

def get_total_seconds():
    try:
        hour = int(hour1.get()) * 10 + int(hour2.get())
        minute = int(min1.get()) * 10 + int(min2.get())
        return hour * 3600 + minute * 60
    except ValueError:
        return 0

def countdown_timer(seconds):
    while seconds > 0 and running_flag[0]:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        log_message(f"[Timer] Remaining: {timer_display}")
        time.sleep(1)
        seconds -= 1

    if running_flag[0]:
        auto.stop()
        log_message("[Timer] Time's up! AutoActivity stopped.")
        if shutdown_var.get():
            log_message("[System] Shutting down the system...")
            shutdown_system()
        if stop_upwork_var.get():
            log_message("[System] (Coming Soon) Stop Upwork Time Tracker...")
            auto.mouse.stopUpworkTimeTracker()

def shutdown_system():
    if platform.system() == "Windows":
        os.system("shutdown /s /t 5")
    elif platform.system() == "Linux":
        os.system("shutdown now")
    elif platform.system() == "Darwin":
        os.system("sudo shutdown -h now")
    else:
        log_message("[Error] Shutdown not supported on this OS.")

def start_activity():
    selected_apps = get_selected_apps()
    total_seconds = get_total_seconds()

    if total_seconds == 0:
        messagebox.showwarning("Input Error", "Please input a valid time greater than 00:00.")
        return

    if not selected_apps:
        messagebox.showwarning("Input Error", "Please select at least one application.")
        return

    running_flag[0] = True
    mins = total_seconds // 60
    log_message(f"[System] Starting AutoActivity for {mins} minute(s) with: {selected_apps}")

    threading.Thread(target=auto.start, args=(selected_apps,), daemon=True).start()
    threading.Thread(target=countdown_timer, args=(total_seconds,), daemon=True).start()

def stop_activity():
    running_flag[0] = False
    auto.stop()
    log_message("[System] AutoActivity stopped manually.")

# ================= GUI Setup ================= #
root = tk.Tk()
root.title("Auto Activity Controller")
root.geometry("420x630")
root.resizable(False, False)

tab_control = ttk.Notebook(root)

# ================= TAB 1: Scheduler ================= #
tab_main = tk.Frame(tab_control)
tab_control.add(tab_main, text="Scheduler")

tk.Label(tab_main, text="Auto Activity Scheduler", font=("Arial", 14, "bold")).pack(pady=(10, 0))

tk.Label(tab_main, text="Set Timer (HH:MM)", font=("Arial", 12)).pack(pady=(10, 0))
time_frame = tk.Frame(tab_main)
hour1 = tk.Spinbox(time_frame, from_=0, to=9, width=2, font=("Arial", 14), justify='center')
hour2 = tk.Spinbox(time_frame, from_=0, to=9, width=2, font=("Arial", 14), justify='center')
min1 = tk.Spinbox(time_frame, from_=0, to=5, width=2, font=("Arial", 14), justify='center')
min2 = tk.Spinbox(time_frame, from_=0, to=9, width=2, font=("Arial", 14), justify='center')
hour1.pack(side="left")
hour2.pack(side="left")
tk.Label(time_frame, text=":", font=("Arial", 14)).pack(side="left", padx=2)
min1.pack(side="left")
min2.pack(side="left")
time_frame.pack(pady=5)

tk.Label(tab_main, text="Select Applications", font=("Arial", 12)).pack(pady=(10, 0))
checkbox_frame = tk.Frame(tab_main)
chrome_var = tk.BooleanVar()
vscode_var = tk.BooleanVar()
tk.Checkbutton(checkbox_frame, text="Chrome", variable=chrome_var).pack(side='left', padx=5)
tk.Checkbutton(checkbox_frame, text="VS Code", variable=vscode_var).pack(side='left', padx=5)
tk.Checkbutton(checkbox_frame, text="Figma (Coming Soon)", state='disabled').pack(side='left', padx=5)
checkbox_frame.pack(pady=(5, 0))

tk.Label(tab_main, text="* Figma integration is not available yet", font=("Arial", 9, "italic"), fg="gray").pack(pady=(0, 5))

btn_frame = tk.Frame(tab_main)
tk.Button(btn_frame, text="Start", command=start_activity, width=12, bg="#28a745", fg="white").pack(side='left', padx=10)
tk.Button(btn_frame, text="Stop", command=stop_activity, width=12, bg="#dc3545", fg="white").pack(side='left', padx=10)
btn_frame.pack(pady=10)

tk.Label(tab_main, text="Shortcut: F5 = Start, F6 = Stop", font=("Arial", 10, "italic"), fg="gray").pack(pady=(0, 5))

log_text = scrolledtext.ScrolledText(tab_main, state='disabled', height=10, font=("Courier New", 10))
log_text.pack(fill='both', expand=True, padx=10, pady=10)

# ================= TAB 2: Settings ================= #
tab_settings = tk.Frame(tab_control)
tab_control.add(tab_settings, text="Settings")

tk.Label(tab_settings, text="Settings", font=("Arial", 14, "bold")).pack(pady=(20, 10))

shutdown_var = tk.BooleanVar()
tk.Checkbutton(
    tab_settings,
    text="Shutdown PC after completion",
    variable=shutdown_var
).pack(anchor='w', padx=20)

stop_upwork_var = tk.BooleanVar()
tk.Checkbutton(
    tab_settings,
    text="Stop Upwork Time Tracker after completion",
    variable=stop_upwork_var,
    # state='disabled'
).pack(anchor='w', padx=20, pady=(5, 0))

tk.Label(
    tab_settings,
    text="* need to activate keyboard shortcut on settings",
    font=("Arial", 9, "italic"),
    fg="gray"
).pack(anchor='w', padx=20, pady=(0, 10))

# ================= TAB 3: About ================= #
tab_about = tk.Frame(tab_control)
tab_control.add(tab_about, text="About")

tk.Label(tab_about, text="About This App", font=("Arial", 14, "bold")).pack(pady=(20, 10))
tk.Label(tab_about, text="Auto Activity Scheduler", font=("Arial", 12)).pack(pady=(0, 5))
tk.Label(tab_about, text="Created by: SukunDev", font=("Arial", 11)).pack()
tk.Label(tab_about, text="GitHub:", font=("Arial", 11, "underline")).pack(pady=(10, 0))

link = tk.Label(tab_about, text="https://github.com/SukunDev", fg="blue", cursor="hand2")
link.pack()

def open_github(event):
    import webbrowser
    webbrowser.open_new("https://github.com/SukunDev")

link.bind("<Button-1>", open_github)

# ================= FINALIZE ================= #
tab_control.pack(expand=1, fill="both")
running_flag = [False]
root.bind('<F5>', lambda event: start_activity())
root.bind('<F6>', lambda event: stop_activity())
root.mainloop()
