from flask import Flask
import threading
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Astarr Music API is running 🚀"

def run_bot():
    import main  # 👈 yaha apna bot file name daalo

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
