from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class comment(db.Model):
    comment_id = db.Column(db.Integer, nullable=False, primary_key=True)


class profile(db.Model):
    user_id = db.Column(db.Integer, nullable=False, primary_key=True)