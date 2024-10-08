from flask import Flask, render_template
from waitress import serve


app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('start.html')

@app.route("/innenputz")
def innenputz():
    return render_template('innenputz.html')

@app.route("/aussenputz")
def aussenputz():
    return render_template('aussenputz.html')

@app.route("/klinkerriemchen")
def klinkerriemchen():
    return render_template('klinkerriemchen.html')

@app.route("/kontakt")
def kontakt():
    return render_template('kontakt.html')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=4000)
