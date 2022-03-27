from flask import Flask, redirect, render_template, request

app = Flask(__name__) #static_url_path='/static' (??) (ignore)

# placeholder lists of dictionaries till sql implementation
users = []  # each user has a 'name' and 'status'
posts = []  # posts have a 'title', 'caption' and 'song'
# songs have a 'title' 'link' and 'artist'
songdict = {'song1': {'title':'song1', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song1art'}, 
            'song2': {'title':'song2', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song2art'}, 
            'AAAAA': {'title':'SCALKS', 'link':'https://www.youtube.com/watch?v=lxoprelYHdo', 'artist':'formula1music'}}




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
    return render_template('viewpost.html', user=users[0], post=posts[0], song=songdict[0])

@app.post('/createpost')
def createpost():
    # TODO grab inputs from the form
    # TODO change into values, add to database
    return viewpost()


@app.get('/createpost')
def createpost_page():
    return render_template('createpost.html', selection=songdict)


@app.post('/submitSignUp')
def createUser():
    return home()


if __name__ == "__main__":
    app.run(debug=True)