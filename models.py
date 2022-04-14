import email
from logging import NullHandler
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table for the user's profile, contains their id, name, password, and email.
class userprofile(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(30), nullable=False)
    user_pass = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    # Print out string for User information
    def __repr__(self):
        return f'userprofile({self.user_id}, {self.user_name}, {self.user_pass}, {self.email})'


# Song table, holds the id as well as title and artist information.
class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist = db.Column(db.String(30), nullable=False)
    song_name = db.Column(db.String(40), nullable=False)

    # Print out string for Song information
    def __repr__(self):
        return f'song({self.song_id}, {self.artist}, {self.song_name})'


# Post table, keeps the id, user id, caption, and song id.
class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(userprofile.user_id), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(Song.song_id), nullable=False)
    caption = db.Column(db.String(255), nullable=False)

    # Print out string for Post information
    def __repr__(self):
        return f'post({self.post_id}, {self.user_id}, {self.song_id}, {self.caption})'    


# Comment table, keeps comment id, user id, post id, and the conent of the comment.
class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(userprofile.user_id), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(Post.post_id), nullable=False)
    content = db.Column(db.String(255), nullable=False)

    # Print out string for Comment information
    def __repr__(self):
        return f'comment({self.follower_id}, {self.following_id})'


# JUNCTION TABLE
# Table for the m to m relation that comes with user/post. keeps the user and post id.
class Post_User(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(userprofile.user_id), primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(Post.post_id), primary_key=True, nullable=False)

    # Print out string for Post_User information
    def __repr__(self):
        return f'follower-following({self.follower_id}, {self.following_id})'


# JUNCTION TABLE
# Table for determining followers, used to track who follows who.
class Follower(db.Model):
    follower_id = db.Column(db.Integer, db.ForeignKey(userprofile.user_id), primary_key=True, nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey(userprofile.user_id), primary_key=True, nullable=False)
    
    # Print out string for Follower-Following information
    def __repr__(self):
        return f'follower-following({self.follower_id}, {self.following_id})'