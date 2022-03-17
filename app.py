from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def home():
    return render_template('index.html')


@app.get('/home')
def index():
    return render_template('home.html')


@app.get('/signin')
def sign():
    return render_template('signin.html')

@app.get('/signup')
def sign():
    return render_template('signup.html')

@app.get('/profile')
def sign():
    return render_template('profile.html')


@app.get('/viewpost')
def sign():
    return render_template('viewpost.html')


@app.get('/createpost')
def sign():
    return render_template('createpost.html')


if __name__ == "__main__":
    app.run(debug=True)