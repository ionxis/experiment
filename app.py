from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return {
        "code: 300,
        "message" : "unauthorized"
    }

if __name__ == "__main__":
    app.run(debug=True)
