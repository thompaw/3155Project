import email
from logging import NullHandler
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --CREATE TABLE user_profile(
# user_id int NOT NULL AUTO_INCREMENT, 
# [name] varchar(30) NOT NULL,
# [password] varchar(30) NOT NULL, 
# email varchar(50) NOT NULL, 
# PRIMARY KEY (user_id)
# );

class User_Profile(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    # Print out string for User information
    def __repr__(self):
        return f'User_profile({self.user_id}, {self.name}, {self.password}, {self.email})'


# CREATE TABLE song( /* song table, holds the id as well as title and artist information. */
#     song_id int NOT NULL AUTO_INCREMENT, 
#     artist varchar(255) NOT NULL,
#     song_name varchar(40) NOT NULL,
#     PRIMARY KEY (song_id)
# );

class Song(db.Model):
    song_id = db.Column(db.Integer, primary_key=True)
    artist = db.Column(db.String(30), nullable=False)
    song_name = db.Column(db.String(40), nullable=False)

    # Print out string for Song information
    def __repr__(self):
        return f'song({self.song_id}, {self.artist}, {self.song_name})'

# --CREATE TABLE post(
#     post_id int NOT NULL AUTO_INCREMENT, 
#     user_id int NOT NULL, 
#     caption varchar(255) NOT NULL,
#     song_id int NOT NULL,
#     PRIMARY KEY(post_id),
#     FOREIGN KEY (user_id) REFERENCES user_profile(user_id),
#     FOREIGN KEY (song_id) REFERENCES song(song_id)
# );

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User_Profile.user_id), nullable=False)
    song_id = db.Column(db.Integer, db.ForeignKey(Song.song_id), nullable=False)
    caption = db.Column(db.String(255), nullable=False)

    # Print out string for Post information
    def __repr__(self):
        return f'post({self.post_id}, {self.user_id}, {self.song_id}, {self.caption})'    

# CREATE TABLE comment(
#     comment_id int NOT NULL AUTO_INCREMENT, 
#     user_id int NOT NULL, 
#     post_id int NOT NULL, 
#     content varchar(255) NOT NULL, 
#     PRIMARY KEY (comment_id),
#     FOREIGN KEY (user_id) REFERENCES user_profile(user_id)
# );

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User_Profile.user_id), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(Post.post_id), nullable=False)
    content = db.Column(db.String(255), nullable=False)

    # Print out string for Comment information
    def __repr__(self):
        return f'comment({self.follower_id}, {self.following_id})'


# --CREATE TABLE post_user( /* table for the m to m relation that comes with user/post. keeps the user and post id. */
#     user_id int NOT NULL, 
#     post_id int NOT NULL, 
#     PRIMARY KEY (user_id, post_id),
#     FOREIGN KEY (user_id) REFERENCES user_profile(user_id), 
#     FOREIGN KEY (post_id) REFERENCES post(post_id)
# );

class Post_User(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(User_Profile.user_id), primary_key=True, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey(Post.post_id), primary_key=True, nullable=False)

    # Print out string for Post_User information
    def __repr__(self):
        return f'follower-following({self.follower_id}, {self.following_id})'


# --CREATE TABLE follower (
#     follower_id int NOT NULL, 
#     following_id int NOT NULL,
#     FOREIGN KEY (follower_id) REFERENCES user_profile(user_id),
#     PRIMARY KEY (follower_id, following_id),
#     FOREIGN KEY (following_id) REFERENCES user_profile(user_id)
# );

class Follower(db.Model):
    follower_id = db.Column(db.Integer, db.ForeignKey(User_Profile.user_id), primary_key=True, nullable=False)
    following_id = db.Column(db.Integer, db.ForeignKey(User_Profile.user_id), primary_key=True, nullable=False)
    
    # Print out string for Follower-Following information
    def __repr__(self):
        return f'follower-following({self.follower_id}, {self.following_id})'