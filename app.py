from flask import Flask
import threading
import os
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot Running 🚀"

def run_bot():
    while True:
        print("Starting bot...")
        os.system("python3 -m ShrutiMusic")
        print("Bot stopped. Restarting in 30 sec...")
        time.sleep(30)

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
