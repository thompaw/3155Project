from flask import Flask, redirect, render_template, request

app = Flask(__name__)

@app.get('/')
def index():
    return render_template('index.html')


@app.get('/home')
def home():
    return render_template('home.html')


@app.get('/signin')
def signin():
    return render_template('signin.html')

@app.get('/signup')
def signup():
    return render_template('signup.html')

@app.get('/profile')
def profile():
    return render_template('profile.html')


@app.get('/viewpost')
def viewpost():
    return render_template('viewpost.html')


@app.get('/createpost')
def createpost():
    return render_template('createpost.html')


@app.post('/submitSignUp')
def createUser():

    return home()


if __name__ == "__main__":
    app.run(debug=True)