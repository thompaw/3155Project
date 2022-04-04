from flask import Flask, redirect, render_template, request

app = Flask(__name__) #static_url_path='/static' (??) (ignore)

# This is a good idea, having this placeholder for now, but it may be easier in the future
# to put all this into its repository module, so it's easier to refactor later
# placeholder lists of dictionaries till sql implementation

# each user has a 'name' and 'status'
users = {'testuser': {'name':'brian', 'status':'in pain'}

}

posts = {}  # posts have a 'title', 'caption' and 'song'

# songs have a 'title' 'link' and 'artist'
songdict = {'song1': {'title':'song1', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song1art'}, 
            'song2': {'title':'song2', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song2art'}, 
            'AAAAA': {'title':'SCALKS', 'link':'https://www.youtube.com/watch?v=lxoprelYHdo', 'artist':'formula1music'}}


@app.get('/')
def index():
    # TODO pull recent posts to display on the front page
    return render_template('index.html', user=users['testuser'], postlist=posts)

# I'm not sure this route is really necessary
@app.get('/home')
def home():
    return redirect('/')


@app.get('/signin')
def signin():
    return render_template('signin.html')

@app.get('/signup')
def signup():
    return render_template('signup.html')

@app.get('/profile')
def profile():
    return render_template('profile.html')

# Might be better and more uniform to follow the route naming convention in the PPT
@app.get('/viewpost')
def viewpost():
    # TODO figure out which post is being viewed, and find the corresponding user. 
    # TODO then find the song being listed in the post
    # TODO input these to the template
    return render_template('viewpost.html', user=users['testuser'], post=posts['agony'], song=songdict['song1'])

@app.post('/createpost')
def createpost():
    # TODO grab inputs from the form
    post_title = request.args.get('post_title')

    # You can pass a default value of None so you don't have to use a try/except
    # request.args.get('post_caption', None)
    try:
        post_caption = request.args.get('post_caption')
    except Exception:
        post_caption = None
    
    songid = request.args.get('song_select')

    post = {'title':post_title, 'caption':post_caption, 'song':songid}

    posts['agony'] = post
    
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