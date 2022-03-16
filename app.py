from flask import Flask, redirect, render_template, request

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')

@app.get('/home')
def home():
    return render_template('home.html')

@app.get('/signpage')
def sign():
    return render_template('signpage.html')


if __name__ == "__main__":
    app.run(debug=True)