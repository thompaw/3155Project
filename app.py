from genericpath import exists
from dotenv import load_dotenv
from flask import Flask, redirect, render_template, request, abort, session
from models import Userprofile, db
from blueprints.user_profile_blueprint import router as user_profile_router
from blueprints.post_blueprint import router as post_router
from blueprints.comment_blueprint import router as comment_router
import os
from flask_bcrypt import Bcrypt
import spot
import sqlalchemy


app = Flask(__name__) #static_url_path='/static' (??) (ignore)
bcrypt = Bcrypt(app)

# database connection stuffs below
load_dotenv()

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('CLEARDB_DATABASE_URL', 'sqlite:///test.db')
app.config['SQLALCHEMY_TRACK_MODRIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')

db.init_app(app)

# placeholder lists of dictionaries till sql implementation

# each user has a 'name' and 'status'
users = {'testuser': {'name':'brian', 'status':'in pain'}}

posts = {}  # posts have a 'title', 'caption' and 'song'

# songs have a 'title' 'link' and 'artist'
songdict = {'song1': {'title':'song1', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song1art'}, 
            'song2': {'title':'song2', 'link':'https://www.youtube.com/watch?v=5qap5aO4i9A', 'artist':'song2art'}, 
            'AAAAA': {'title':'SCALKS', 'link':'https://www.youtube.com/watch?v=lxoprelYHdo', 'artist':'formula1music'}}


# NOT IN USER SESSION

# no session home page
@app.get('/')
def get_index_page():
    # if user is in session then redirect to home feed
    if 'user' in session:
            return redirect('/home')
        
    return render_template('index.html')

# signup page
@app.get('/signup')
def get_signup_page():
    # if user is in session then redirect to home feed
    if 'user' in session:
        return redirect('/home')

    return render_template('signup.html')

# signup page (add new user to database)
@app.post('/signup')
def signup():
    username = request.form.get('username', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')

    if username == '' or email == '' or password == '':
        abort(400)

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = Userprofile(user_name=username, user_email=email, user_password=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/signin')

# signin page
@app.get('/signin')
def get_sigin_page():
    # if user is in session then redirect to home feed
    if 'user' in session:
        return redirect('/home')
    
    return render_template('signin.html')

# signin page (start session)
@app.post('/signin')
def signin():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    existing_user = Userprofile.query.filter_by(user_name=username).first()
    print(existing_user)

    if not existing_user or existing_user.user_id == 0:
        return redirect('/fail')

    if not bcrypt.check_password_hash(existing_user.user_password, password):
        return redirect('/fail')

    session['user'] = {
        'username': username,
        'user_id': existing_user.user_id
    }

    return redirect('/home')

# log out (end session)   
@app.post('/logout')
def logout():
    # if user is not logged in then abort
    if 'user' not in session:
        abort(401)

    # delete the user session
    del session['user']

    # redirect to landing page
    return redirect('/')

# fail page when credentials don't work (both signin and signup)
@app.get('/fail')
def fail():
    if 'user' in session:
        return redirect('/home')

    return render_template('fail.html')


# IN USER SESSION

# user session home page feed
@app.get('/home')
def get_home_page():
    # if user is not logged in then abort
    if 'user' not in session:
        abort(401)
    
    # TODO pull recent posts to display on the front page
    return render_template('home.html', user=users['testuser'], postlist=posts, user_in_session = session['user']['user_id'], user_in_session_name = session['user']['username'])

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

@app.get('/post/songsearch')
def songsearch():
    return render_template('songsearch.html')

@app.get('/post/createpost') 
def createpost_page():
    query = request.args.get('songname')
    
    results = spot.output(query)
    #print(results)
    return render_template('createpost.html', selection=results['tracks']['items'])

if __name__ == "__main__":
    app.run(debug=True)

app.register_blueprint(user_profile_router)
app.register_blueprint(post_router)
app.register_blueprint(comment_router)
