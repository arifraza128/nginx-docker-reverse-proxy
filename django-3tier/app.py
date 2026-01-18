from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "3 Tier App running with Docker + Nginx "

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
