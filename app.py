from flask import Flask, redirect, render_template, request

app = Flask(__name__) #static_url_path='/static' (??) (ignore)

# placeholder lists of dictionaries till sql implementation
users = []  # each user has a 'name' and 'status'
posts = []  # posts have a 'title', 'caption' and 'song'
songlist = []  # songs have a 'title' and 'artist'



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
    # TODO figure out which post is being viewed, and find the corresponding user. 
    # TODO then find the song being listed in the post
    # TODO input these to the template
    return render_template('viewpost.html', user= users[0], post= posts[0], song=songlist[0])

@app.post('/createpost')
def createpost():
    return render_template('createpost.html')


@app.get('/createpost')
def createpost():
    return render_template('createpost.html')


@app.post('/submitSignUp')
def createUser():

    return home()


if __name__ == "__main__":
    app.run(debug=True)