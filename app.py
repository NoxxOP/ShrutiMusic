from flask import Flask
import threading
import os
import subprocess
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Astarr Music Bot Running 🚀"

def run_bot():
    while True:
        print("Starting bot...")
        process = subprocess.Popen(["python3", "-m", "ShrutiMusic"])
        process.wait()  # wait until bot stops
        print("Bot stopped. Restarting in 10 sec...")
        time.sleep(10)

if __name__ == "__main__":
    t = threading.Thread(target=run_bot)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
