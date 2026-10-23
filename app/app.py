from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Self-Healing Web Application is Running!"

@app.route('/health')
def health():
    return "Self-Healing Web Application is Healthy"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
