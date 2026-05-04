from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Astarr Music Bot Running 🚀"

def run_bot():
    while True:
        try:
            os.system("python3 -m ShrutiMusic")
        except Exception as e:
            print(f"Bot crashed: {e}")

if __name__ == "__main__":
    threading.Thread(target=run_bot, daemon=True).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
