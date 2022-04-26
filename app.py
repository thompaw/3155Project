from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request
from models import db
from blueprints.user_profile_blueprint import router as user_profile_router
from blueprints.post_blueprint import router as post_router
import os
import spot
app = Flask(__name__) #static_url_path='/static' (??) (ignore)

# database connection stuffs below
load_dotenv()
import sqlalchemy
engine = sqlalchemy.engine.URL.create(   #This is just the URI but separated. It all combines into variable engine.
    drivername="mysql",
    username="root",
    password=os.getenv('PASS'),          #put your sql server password in the .env file
    host="localhost",
    port = "3306",
    database="Project"
)
app.config['SQLALCHEMY_DATABASE_URI'] = engine
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# placeholder lists of dictionaries till sql implementation

# each user has a 'name' and 'status'
users = {'testuser': {'name':'brian', 'status':'in pain'}}

posts = {}  # posts have a 'title', 'caption' and 'song'

# songs have a 'title' 'link' and 'artist'
songdict = {'song1': {'title':'song1', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song1art'}, 
            'song2': {'title':'song2', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song2art'}, 
            'AAAAA': {'title':'SCALKS', 'link':'https://www.youtube.com/watch?v=lxoprelYHdo', 'artist':'formula1music'}}


@app.get('/')
def index():
    # TODO pull recent posts to display on the front page
    return render_template('index.html', user=users['testuser'], postlist=posts)


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
    return render_template('single_user_profile.html')

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

    try:
        post_caption = request.args.get('post_caption')
    except Exception:
        post_caption = None
    
    songid = request.args.get('song_select')

    post = {'title':post_title, 'caption':post_caption, 'song':songid}

    posts['agony'] = post
    
    # TODO change into values, add to database
    return viewpost()

@app.get('/songsearch')
def songsearch():
    return render_template('songsearch.html')

@app.get('/createpost') #mightbe useless now
def createpost_page():
    query = request.args.get('songname')
    
    results = spot.output(query)
    #print(results)
    return render_template('createpost.html', selection=results['tracks']['items'])


@app.post('/submitSignUp')
def createUser():
    return home()


if __name__ == "__main__":
    app.run(debug=True)

app.register_blueprint(user_profile_router)
app.register_blueprint(post_router)
