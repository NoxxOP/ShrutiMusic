from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Astarr Music Bot Running 🚀"

def run_bot():
    os.system("python3 -m ShrutiMusic")

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000))) 
