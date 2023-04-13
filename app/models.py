# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime

class Posts(db.Model):
    __tablename__ = 'Posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    caption = db.Column(db.String(500))
    photo = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    created_on = db.Column(db.DateTime)

    def __init__(self, caption, photo, user_id):
        self.name = caption
        self.age = photo
        self.user_id = user_id

    def __repr__(self):
        return '<Posts %r>' % (self.caption)

class Likes(db.Model):
    __tablename__ = 'Likes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey('Posts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def __init__(self, post_id, user_id):
        self.post_id = post_id
        self.user_id = user_id

    def __repr__(self):
        return '<Likes %r>' % (self.id)

class Follows(db.Model):
    __tablename__ = 'Follows'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('Users.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'))

    def __init__(self, follower_id, user_id):
        self.follower_id = follower_id
        self.user_id = user_id

    def __repr__(self):
        return '<Follows %r>' % (self.id)

class Users(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200))
    password = db.Column(db.String(200))
    firstname = db.Column(db.String(200))
    lastname = db.Column(db.String(200))
    email = db.Column(db.String(200))
    location = db.Column(db.String(200))
    biography = db.Column(db.String(500))
    profile_photo = db.Column(db.String(200))
    joined_on = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, username, password, firstname, lastname, email, location, biography, profile_photo):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.location = location
        self.biography = biography
        self.profile_photo = profile_photo
        self.joined_on = datetime.utcnow()

    def __repr__(self):
        return '<Users %r>' % (self.username)
