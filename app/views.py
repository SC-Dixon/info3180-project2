"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

from app import app, db, login_manager
from flask import render_template,make_response, request, jsonify, send_file, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from flask_wtf.csrf import generate_csrf
import datetime
from flask_login import login_user, logout_user, current_user, login_required
from app.models import Posts,Likes,Follows,Users
from app.forms import RegisterForm, LoginForm, PostForm
from werkzeug.security import check_password_hash
import os

###
# Routing for your application.
###

@app.route('/')
def index():
    return jsonify(message="This is the beginning of our API")


@app.route('/api/v1/users/<user_id>/posts', methods=['GET'])
def get_userposts(user_id):
    try:
        if request.method == "GET":
            user_posts = db.session.query(Posts).filter_by(user_id=user_id).all()

            posts = []

            for post in user_posts:
                post_data = {
                    'id': post.id,
                    'caption': post.caption,
                    'photo': post.photo,
                    'created_on': post.created_on
                }
                posts.append(post_data)

            return jsonify({'posts': posts})
    except:
        return jsonify({"errors": "Request Failed"}), 401
    
@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_userprofile(user_id):
    try:
        if request.method == "GET":
            user_profile = db.session.query(Users).filter_by(id=user_id).all()

            posts = []

            for profile in user_profile:
                profile_data = {
                    'id': profile.id,
                    'username': profile.username,
                    'firstname': profile.firstname,
                    'lastname': profile.lastname,
                    'email': profile.email,
                    'location': profile.location,
                    'biography': profile.biography,
                    'profile_photo': profile.profile_photo,
                    'joined_on': profile.joined_on
                }
                posts.append(profile_data)

            return jsonify({'User': posts})
    except Exception as e:
        return jsonify({"errors": str(e)}), 401

@app.route('/api/users/<user_id>/follow', methods=['POST'])
@login_required
def follow_user(user_id):
    current_user = current_user()
    target_user = Users.query.filter_by(id=user_id).first()

    if target_user is None:
        return jsonify({'error': 'User not found'}), 404

    follow = Follows.query.filter_by(follower_id=current_user.id, user_id=target_user.id).first()

    if follow is not None:
        return jsonify({'error': 'Already following this user'}), 400

    follow = Follows(follower_id=current_user.id, user_id=target_user.id)
    db.session.add(follow)
    db.session.commit()

    return jsonify({'message': 'Successfully followed user'}), 200

@app.route('/api/v1/posts', methods=['GET'])
def get_allposts():
    try:
        if request.method == "GET":
            #Retrieve data from the database
            posts = db.session.query(Posts).all()
            data = []
            
            for post in posts:
                data.append ({
                    'id': post.id,
                    'caption': post.caption,
                    'photo': post.photo,
                    'user_id': post.user_id,
                    'created_on': post.created_on
                })
            return jsonify (data=data), 200 
    except:
        return jsonify({"errors": "Request Failed"}), 401
    
@app.route('/api/v1/posts/<post_id>/like', methods=['POST'])
@login_required
def like_post(post_id):
    post = Posts.query.get(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404

    like = Likes.query.filter_by(post_id=post_id, user_id=current_user.id).first()
    if like:
        return jsonify({'error': 'Like already exists'}), 400

    new_like = Likes(post_id=post_id, user_id=current_user.id)
    db.session.add(new_like)
    db.session.commit()

    return jsonify({'success': 'Like added successfully'}), 201

@app.route('/api/v1/register', methods=['POST'])
def register():

    form = RegisterForm()
        
    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
        firstname = form.firstname.data
        lastname = form.lastname.data
        email = form.email.data
        location = form.location.data
        biography = form.biography.data
        profile_photo = form.profile_photo.data
        securedprofile_photo = secure_filename(profile_photo.filename)
        joined_on = datetime.datetime.now()

        profile_photo.save(os.path.join(app.config['UPLOAD_FOLDER'], securedprofile_photo))

        newuser =  Users(username, password, firstname, lastname, email, location, biography, profile_photo)
        db.session.add(newuser)
        db.session.commit()
        
        
        return jsonify({
            "message": "User Successfully added",
            "username": newuser.username,
            "password": newuser.password,
            "firstname": newuser.firstname,
            "lastname": newuser.lastname,
            "email": newuser.email,
            "location": newuser.location,
            "biography": newuser.biography,
            "profile_photo": newuser.profile_photo,
            "joined_on": newuser.joined_on
        }),200    
       
    return jsonify({
            "errors": form_errors(form) 
            }),400

@app.route('/api/v1/auth/login', methods=['POST'])
def login():
    form = LoginForm()

    # change this to actually validate the entire form submission
    # and not just one field
    if form.validate_on_submit():
        # Get the username and password values from the form.
        username = form.username.data
        password = form.password.data

        # Using your model, query database for a user based on the username
        # and password submitted. Remember you need to compare the password hash.
        # You will need to import the appropriate function to do so.
        # Then store the result of that query to a `user` variable so it can be
        # passed to the login_user() method below.
        user = db.session.execute(db.select(Users).filter_by(username=username)).scalar()

        if user is not None and check_password_hash(user.password, password):

        # Gets user id, load into session
            login_user(user)

        # Remember to flash a message to the user
            return jsonify({
            "message": "User Login Successful."
        }),200 

            #return redirect(url_for("upload"))  # The user should be redirected to the upload form instead
        else:
            jsonify({
            "danger": "Username or Password is incorrect."
        })

    return jsonify({
            "errors": form_errors(form) 
            }),400


# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
@login_manager.user_loader
def load_user(id):
    return db.session.execute(db.select(Users).filter_by(id=id)).scalar()


@app.route('/api/v1/auth/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({
            "message": "User Logout Successful."
        }),200 

@app.route('/api/v1/users/<user_id>/posts', methods=['POST'])
@login_required
def add_post(user_id):

    form = PostForm()
        
    if form.validate_on_submit():

        photo = form.photo.data
        securedphoto = secure_filename(photo.filename)
        caption = form.caption.data
        
        joined_on = datetime.datetime.now()

        photo.save(os.path.join(app.config['UPLOAD_FOLDER'], photo))

        newpost =  Posts(caption, photo, user_id)
        db.session.add(newpost)
        db.session.commit()
        
        
        return jsonify({
            "message": "New Post Successfully Created.",
            "caption": newpost.caption,
            "photo": newpost.photo,
            "created_on": newpost.created_on
        }),200    
       
    return jsonify({
            "errors": form_errors(form) 
            }),400

@app.route("/api/v1/photos/<filename>")
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']),filename)


###
# The functions below should be applicable to all Flask apps.
###

# Here we define a function to collect form errors from Flask-WTF
# which we can later use



def form_errors(form):
    error_messages = []
    """Collects form errors"""
    for field, errors in form.errors.items():
        for error in errors:
            message = u"Error in the %s field - %s" % (
                    getattr(form, field).label.text,
                    error
                )
            error_messages.append(message)

    return error_messages

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


#@app.errorhandler(404)
#def page_not_found(error):
#    """Custom 404 page."""
#    return render_template('404.html'), 404
