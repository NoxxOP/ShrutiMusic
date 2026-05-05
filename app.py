from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Astarr Music Bot Running 🚀"

def run_bot():
    # tumhara bot yaha se start hoga
    os.system("python3 -m ShrutiMusic")

if __name__ == "__main__":
    # bot ko background me run karo
    threading.Thread(target=run_bot).start()
    
    # flask server (Render ke liye)
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
